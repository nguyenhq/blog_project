#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import re
import schedule
import time
from datetime import datetime
from celery import celery
from celery.schedules import django_crontab

def job():
    # product "Sony 55inch"
    # htmlfile = urllib.request.urlopen("http://www.bestbuy.com/site/sony-55-class-54-6-diag--led-2160p-smart-4k-ultra-hd-tv-with-high-dynamic-range-black/4804403.p?skuId=4804403")
    # htmltext = htmlfile.read()
    # regex = '<meta id="schemaorg-offer-price" itemprop="price" content=(.+?)>'
    # pattern = re.compile(regex)
    # price5 = re.findall(pattern,htmltext)
    # print ("Sony 55inch",price5,str(datetime.now()))
    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)
    print ("sony",datetime.now())

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("19:47").do(job)
# schedule.every(6).seconds.do(job)


while 1:
    schedule.run_pending()
    time.sleep(1)


# To clear all functions
# schedule.clear()
