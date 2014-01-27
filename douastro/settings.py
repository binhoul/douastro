# Scrapy settings for douastro project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'douastro'

SPIDER_MODULES = ['douastro.spiders']
NEWSPIDER_MODULE = 'douastro.spiders'
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True
COOKIES_DEBUG = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douastro (+http://www.yourdomain.com)'
