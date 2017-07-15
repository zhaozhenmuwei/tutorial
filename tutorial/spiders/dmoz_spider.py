import scrapy

class DmozSpider(scrapy.spiders.Spider):
	
	# 爬虫名字
    name = "dmoz"
	
	#爬虫主域名
    allowed_domains = ["dmoz.org"]
	
	
	#开始url
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
	
	#启动时候登录回调
	# def start_requests(self):
	# 	return [scrapy.FormRequest("http://www.example.com/login",
	# 	                           formdata={'user': 'john', 'pass': 'secret'},
	# 	                           callback=self.logged_in)]
	#
	# def logged_in(self, response):
	# 	# here you would extract links to follow and return Requests for
	# 	# each of them, with another callback
	# 	pass

	#解析response
    def parse(self, response):
		for sel in response.xpath('//ul/li'):
			item = DmozItem()
			item.title = sel.xpath('a/text()').extract()
			item.link = sel.xpath('a/@href').extract()
			item.desc = sel.xpath('text()').extract()
			yield item
			self.log('A response from %s just arrived!' % response.url)
			
	#回调循环
	# def parse(self, response):
	# 	sel = scrapy.Selector(response)
	# 	for h3 in response.xpath('//h3').extract():
	# 		yield MyItem(title=h3)
	#
	# 	for url in response.xpath('//a/@href').extract():
	# 		yield scrapy.Request(url, callback=self.parse)
	
	#规则抓取
		
	# class scrapy.contrib.spiders.Rule(link_extractor, callback=None, cb_kwargs=None, follow=None, process_links=None, process_request=None)
	
	# class MySpider(CrawlSpider):
	# 	name = 'example.com'
	# 	allowed_domains = ['example.com']
	# 	start_urls = ['http://www.example.com']
	#
	# 	rules = (
	# 		# 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
	# 		Rule(LinkExtractor(allow=('category\.php',), deny=('subsection\.php',))),
	#
	# 		# 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
	# 		Rule(LinkExtractor(allow=('item\.php',)), callback='parse_item'),
	# 	)
	#
	# 	def parse_item(self, response):
	# 		self.log('Hi, this is an item page! %s' % response.url)
	#
	# 		item = scrapy.Item()
	# 		item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
	# 		item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
	# 		item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
	# 		return item
		
		# from scrapy.contrib.loader import ItemLoader
		# from myproject.items import Product
		#
		# def parse(self, response):
		# 	l = ItemLoader(item=Product(), response=response)
		# 	l.add_xpath('name', '//div[@class="product_name"]')
		# 	l.add_xpath('name', '//div[@class="product_title"]')
		# 	l.add_xpath('price', '//p[@id="price"]')
		# 	l.add_css('stock', 'p#stock]')
		# 	l.add_value('last_updated', 'today')  # you can also use literal values
		# 	return l.load_item()