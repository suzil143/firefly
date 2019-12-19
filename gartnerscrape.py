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

baseurl = "https://www.gartner.com"
url = "https://www.gartner.com/en/conferences/calendar"


def beautifycontent(data):
	pretty = bs(data,'html.parser')

	gettabledata = pretty.find('div',{'class':'row calendar-tiles'}).find_all('a')
	allextrcteddata = []
	for indi in gettabledata:
		href_link = baseurl+indi['href']
		startdate = indi['data-gtm-start-date']
		conferencetype = indi['data-type']
		getallrowdata = getrowdata(indi,href_link,startdate)
		getallrowdata['fetch-date'] = now
		getallrowdata['conference-type'] = conferencetype
		getallrowdata['event-description-link'] = href_link
		getallrowdata['start-date'] = startdate
		allextrcteddata.append(getallrowdata)

	return allextrcteddata	


def getrowdata(singlerow):
		individualdata = singlerow.find('div',{'class':'conference-data-content'})
		my_json = {}
		for indi in individualdata.find_all('p'):
			field = indi['class'][0]
			my_json[field] = indi.text.strip().encode('ascii','ignore')

		return my_json



class gartnerscrape():
	"""docstring for gartnerscrape"""

	def webscrape(self,url):


		data = requests.get(url).content
		info = beautifycontent(data)

		insetdb = db.gartner.insert_many(info)

		self.url = "successfully scraped data from this url %s" % url
		print self.url

if __name__ == "__main__":

	obj = gartnerscrape()
	obj.webscrape(url)







