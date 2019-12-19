#!usr/bin/python
import sys
import os
sys.path.append(os.getcwd())
import requests
from bs4 import BeautifulSoup as bs
import urllib
from pymongo import MongoClient
from dateutil import parser
from datetime import datetime

now = datetime.today().strftime('%Y-%m-%d')

client = MongoClient()
db = client.firefly

baseurl = 'https://www.techmeme.com'
url = "https://www.techmeme.com/events"

def techevent(url):

	data = requests.get(url).content
	info = beautiyfycontent(data)

	insertdb = db.techmeme.insert_many(info)


def beautiyfycontent(data):
	pretty = bs(data,'html.parser')
	allrows = pretty.find('div',{'id':'events'}).find_all('div',{'class':'rhov'})
	allextrcteddata = []

	for inp in allrows:
		indirow = getrowdata(inp)

		allextrcteddata.append(indirow)

	return allextrcteddata	


def getrowdata(singlerows):

	link = singlerows.find('a')['href']
	href_link = baseurl+link
	eventinfo = singlerows.find_all('div')

	fieldname = ['event-date','event-title','event-location']
	alldata = {}
	for event,num in zip(eventinfo,range(len(eventinfo))):
		article = event.text.strip().encode('ascii','ignore')

		alldata[fieldname[num]] = article

	alldata['fetch-date'] = now
	alldata['event-description-link'] = href_link

	return alldata	

techevent(url)	
