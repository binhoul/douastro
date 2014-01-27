from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class DmozSpider(BaseSpider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = ['http://www.google.com/']
#    for num in range(0,50,25):
#        start_urls.append("http://www.douban.com/group/128828/discussion?start=%s" % str(num) )
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        urls = hxs.select('//div[contains(@class, "content")]//a[contains(@onclick,"gbar")]').re("http://www.douban.com/group/topic/\d+")
        print urls
        urlstr = '\n'.join(urls)
        #filename = response.url.split("/")[-2]
        filename = 'group-urls'
        open(filename, 'wb').write(urlstr)
