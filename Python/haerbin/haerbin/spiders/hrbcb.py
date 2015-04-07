# -*- coding: utf-8 -*-
import scrapy
import bs4
from bs4 import BeautifulSoup

import sys

reload(sys)
sys.setdefaultencoding('utf-8')



class HrbcbSpider(scrapy.Spider):
    name = "hrbcb"
    allowed_domains = ["www.hrbcb.com.cn"]
    start_urls = (
        'http://www.hrbcb.com.cn/card/card5.jsp',
    )

    def parse(self, response):
        htmlResponse = ''.join(response.body)
        soup = BeautifulSoup(htmlResponse)
        ''' silly method, but worked
        cardDiv = soup.find(id="card").find_all("p")
        for li in cardDiv:
            #print "type is " + str(type(li))
            tmpStr =  str(li)
            print tmpStr.replace("span","").replace("p", "").replace("br","").replace("<","").replace(">","").replace("/","").replace("class","").replace('"',"").replace("hometitle","").replace("=","").replace(" " , "")'''


        for item in soup.find_all('p'):
            for des in item.descendants:
                if isinstance(des, bs4.element.NavigableString):
                    print unicode(des.strip())
