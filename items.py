import json, requests
from lxml import html

class Item:
	def __init__(self, html_tree):
		self.url = None
		self.owner = None
		self.parse_item(html_tree)

	def __str__(self):
		return str({'url': self.url})

	def parse_item(self, html_tree):
		"""Parses the given html tree and sets url and owner properties

		Args:
			html_tree(lxml.html): html tree of the anchor element
		"""
		my_dict = json.loads(html_tree.attrib['data-hydro-click'])
		payload = my_dict['payload']
		owner = html_tree.attrib['href'].split('/')[1]	# split the href link
		item_url = payload['result']['url']
		self.url = item_url
		self.owner = owner


class Repository(Item):
	def __init__(self, html_tree):
		Item.__init__(self, html_tree)
		self.language_stats = self.get_language_stats(self.url)

	def __str__(self):
		return str({'url': self.url, 'extra': {'owner': self.owner, 'language_stats': self.language_stats} })

	def get_language_stats(self, repo_url):
		"""Gets the repository url, makes GET request, parses language stats

		Args:
			repo_url(str): repository url
		Returns:
			languages(dict): languages with percentages
		"""
		repo_page = requests.get(repo_url, timeout=10).content
		lang_list = html.fromstring(repo_page).xpath("//span[@class = 'Progress ']")[0].getchildren()
		languages = {}
		for lang in lang_list:
			lang = lang.attrib['aria-label'].split(" ")
			languages[lang[0]] = lang[1]

		return languages


class Issue(Item):
	def __init__(self, html_tree):
		Item.__init__(self, html_tree)


class Wiki(Item):
	def __init__(self, html_tree):
		Item.__init__(self, html_tree)
