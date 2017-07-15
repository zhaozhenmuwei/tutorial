import MySQLdb
from bs4 import BeautifulSoup
from urllib import unquote
from scrapy import Spider
from scrapy.selector import Selector
from MySpider.items import tbThumbItem
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class lofter_spider(Spider):
	#爬虫名称
	name = 'lofter_spider'
	
	#限定域名
	allow_domains = ['lofter.com']
	
	#初始url
	start_urls = [
		"http://www.lofter.com/selections?act=qbview_20130930_06"]
	
	
	#初始化工作
	def start_requests(self):
		# db = MySQLdb.connect("localhost", "root", "*******", "spider")
		# cursor = db.cursor()
		# sql = "select user_id from tb_model"
		# count = cursor.execute(sql)
		# results = cursor.fetchmany(count）
		
		#登录获取cookie
		cookie_jar = CookieJar()
		
		requests = []
		
		request = Request('http://passport.www.lofter.com/dl/l',
				callback=self.pre_parse_album,method='post', meta={'user_id': user_id[0]})
			requests.append(request)
		return requests

# FormRequeset


def post_login(self, response):
	print 'Preparing login'
	# 下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
	xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]

	# FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
	# 登陆成功后, 会调用after_login回调函数
	return [FormRequest.from_response(response,
	                                  formdata={
		                                  '_xsrf': xsrf,
		                                  'email': '123456',
		                                  'password': '123456'
	                                  },
	                                  callback=self.after_login
	                                  )]

	def per_parse_cookie(self, response):
	
	
	
	
	def pre_parse_album(self, response):
		sel = Selector(response)
		total_page = sel.xpath("//input[@name='totalPage']/@value").extract()[0]
		user_id = response.meta['user_id']
		requests = []
		for i in range(1, int(total_page)):
			request = Request(
				"https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id=%s&page=%s" % (
				str(user_id), str(i)), callback=self.parse_album, meta={'user_id': user_id})
			requests.append(request)
		return requests
	
	def urldecode(self, query):
		d = {}
		a = query.split('&')
		for s in a:
			if s.find('='):
				k, v = map(unquote, s.split('='))
				try:
					d[k].append(v)
				except KeyError:
					d[k] = [v]
		
		return d
	
	def parse_album(self, response):
		sel = Selector(response)
		tbThumbItems = []
		thumb_url_list = sel.xpath("//div[@class='mm-photo-cell-middle']//h4//a/@href").extract()
		thumb_name_list = sel.xpath("//div[@class='mm-photo-cell-middle']//h4//a/text()").extract()
		user_id = response.meta['user_id']
		for i in range(0, len(thumb_url_list) - 1):
			thumbItem = tbThumbItem()
			thumbItem['thumb_name'] = thumb_name_list[i].replace('\r\n', '').replace(' ', '')
			thumbItem['thumb_url'] = thumb_url_list[i]
			thumbItem['thumb_userId'] = str(user_id)
			temp = self.urldecode(thumbItem['thumb_url'])
			thumbItem['thumb_id'] = temp['album_id'][0]
			tbThumbItems.append(thumbItem)
		return tbThumbItems