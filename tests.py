import unittest
from items import *
from crawler import Crawler


class TestGithubCrawler(unittest.TestCase):

	def setUp(self):
		self.example_repo = {"keywords": ["openstack", "nova", "css"],
						  "proxies": ["194.126.37.94:8080", "13.78.125.167:8080"],
						  "type": "Repositories"}
		self.example_wiki = {"keywords": ["python", "django-rest-framework", "jwt"],
						  "proxies": ["195.138.83.218:53281", "109.245.239.125:35659"],
						  "type": "Wikis"}
		self.example_issue = {"keywords": ["react", "redux", "js"],
						  "proxies": ["80.78.74.133:55443", "185.34.17.248:58137"],
						  "type": "Issues"}


	def test_repo(self):
		crawler = Crawler(self.example_repo)

		self.assertTrue(crawler.items, True)
		for item in crawler.items:
			self.assertEqual(type(item), Repository)

	def test_wiki(self):
		crawler = Crawler(self.example_wiki)

		self.assertTrue(crawler.items, True)
		for item in crawler.items:
			self.assertEqual(type(item), Wiki)

	def test_issue(self):
		crawler = Crawler(self.example_issue)

		self.assertTrue(crawler.items, True)
		for item in crawler.items:
			self.assertEqual(type(item), Issue)
