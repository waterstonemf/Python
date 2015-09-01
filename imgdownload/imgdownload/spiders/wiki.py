import scrapy
import re
from imgdownload.items import WikiImage
import sys
from scrapy.http import Request

class WikiSpider(scrapy.Spider):
	reload(sys)
	sys.setdefaultencoding('utf-8')

	name = "wiki"
	allowed_domains = ["en.wikipedia.org"]
	start_urls = ['https://en.wikipedia.org/wiki/Image',]
	
	def parse(self, response):
		item = WikiImage()
		images = response.xpath('//img/@src').extract()
		for img in images:
			print img
		


