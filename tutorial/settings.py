# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': '*/*',
  'Accept-Encoding':'gzip',
  'Accept-Language': 'zh-CN,zh;q=0.8',
  'Connection':'keep-alive',
  'Content-Length':'176',
  'Content-Type':'text/plain',
  'Cookie':'usertrack=ezq0plkuhZej3c2qCJ5jAg==; firstentry=%2Flogin.do%3FX-From-ISP%3D2|http%3A%2F%2Fwww.lofter.com%2F; JSESSIONID-WLF-XXD=fb63bfab814cee829cea50044e93a0d77ad6cacb7a846012fc5b9dd7b75c3cdce10964075fd2f5b40df8ca4573897a84bb13912ae49db438b503bdc0162c948e3e362c8f4b1d2ab45b721df862fdb03779d227521c160ef97866e94442ecd67bd09e7cb7f900f70e9a34555da1363abd12f994a5f731b205058b796f1e4a0a1eab3febeb; fastestuploadproxydomainkey=upload|1500086675199; _ntes_nnid=c943261e1440d20ca4791211b7493ad6,1500086676159; NTES_SESS=5MS6KyrjMjw1I1neVM46eHxcGWEwdVAdaoy.OHPytlTTxaw1xYbLveQtrcEPfb17TZgW4aE1L7Fz7fipZl8ndxveTV6ALSxsU_UHtUs_pjzoLc0eAo8LOdHvo3NtXliylqZ6n.hngd2by_ayY01pfeZiZH1HxtoCweUmSSKG_A_W1sDxEM2A11.M.aEE24BUy; NTES_PASSPORT=vhlj1xeimZOptFEOOR6bWLXzuefHinI7R9QgrjO91ElyqC5iqgFBt64Nd.ZWwFiIuOfUMCZiBIcTIwkYOaR_Vqm4KSJyJR0F60xYjeNQ9nNUNydxcHuNpm4OizskcX_eVwZBnezGk8FvUVLhG919mrNrU; S_INFO=1500086686|0|##|hzwubinbin@corp.netease.com; P_INFO=hzwubinbin@corp.netease.com|1500086686|1|lofter|00&99|zhj&1498462567&study#zhj&330100#10#0#0|&0|study_client|hzwubinbin@corp.netease.com; LOFTER-PHONE-LOGIN-FLAG=0; NTESLOFTSI=E3FBCE3CA760AC84E2F8A8A3C574AE73.hzabj-lofter8-8010; regtoken=2000; noAdvancedBrowser=0; reglogin_isLoginFlag=1; __utma=61349937.1084940817.1500086676.1500086683.1500091554.2; __utmb=61349937.21.9.1500092410626; __utmc=61349937; __utmz=61349937.1500086683.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.1084940817.1500086676; _gid=GA1.2.121683025.1500086676',
  'Host':'www.lofter.com',
  'Origin':'http://www.lofter.com',
  'Referer:':'http://www.lofter.com/selections?act=qbview_20130930_06',
  'User-Agent:':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tutorial.pipelines.TutorialPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
