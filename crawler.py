import sys, random
import requests
from lxml import html, etree
import json
from items import *


class Crawler:
	def __init__(self, data):
		self.html_tree = self.make_request(data)
		self.items = self.parse_search_result(self.html_tree)


	def make_request(self, data):
		"""Gets the json file content to read the input and make the get request

		Args:
			filename(str): filename (or path) with json input inside
		Returns:
			html_tree(lxml.html): the html tree obtained from the content of get request
		"""

		keywords = data['keywords']
		random_index = random.randint(0,len(data['proxies'])-1) 	# choose proxy randomly
		proxies = data['proxies'][random_index]
		self.object_type = data['type']

		proxies = {
			"http": "http://"+proxies
		}
		# prepare the request url
		url = "https://github.com/search?q=" + '+'.join(keywords) + '&type=' + self.object_type.lower()
		# make the GET request and decode
		content = requests.get(url, proxies=proxies, timeout=10).content.decode('utf-8')
		# return as an html tree
		return html.fromstring(content)

	def parse_search_result(self, tree):
		"""Gets the html_tree and depending on the object_type given in the input, gathers the 
		item list using the html tags and elements.

		Args:
			tree(lxml.html): the html tree obtained from the content of get request
		Returns:
			items(list): the list of the items created. Possible item types: Repository, Issue, Wiki
		"""
		items = []
		if self.object_type=='Repositories':
			item_list = tree.xpath("//ul[@class = 'repo-list']")[0].getchildren()
			for item in item_list:
				anchor = item.xpath("//a[@class = 'v-align-middle']")[0]
				new_repo = Repository(anchor)
				if new_repo: items.append(new_repo)		# control NoneType
				item.clear()		# we need to refresh the tree


		elif self.object_type=='Issues':
			item_list = tree.xpath("//div[@class = 'issue-list']/div")[0].getchildren()
			for item in item_list:
				anchor = item.xpath("//div[@class = 'f4 text-normal']/a")[0]
				new_issue = Issue(anchor)
				if new_issue: items.append(new_issue)		# control NoneType
				item.clear()		# we need to refresh the tree


		elif self.object_type=='Wikis':
			item_list = tree.xpath("//div[@id = 'wiki_search_results']/div")[0].getchildren()
			for item in item_list:
				anchor = item.xpath("//div[@class = 'f4 text-normal']/a")[0]
				new_wiki = Wiki(anchor)
				if new_wiki: items.append(new_wiki)		# control NoneType
				item.clear()		# we need to refresh the tree

		return items


if __name__=='__main__':
	# check if the jsonfile is given
	if len(sys.argv)<2:
		print('please give json file name')
	else:
		json_file = sys.argv[1]
		# read the input from file
		with open(json_file) as f:
			data = json.load(f)
		# send it to the Crawler while creating an object
		crawler = Crawler(data)

		# print the items
		for item in crawler.items:
			print(item)

