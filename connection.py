from pymongo import MongoClient

def mongoconnection():

	client = MongoClient()
	db = client.firefly

	return db


