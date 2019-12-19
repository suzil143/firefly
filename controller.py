from connection import mongoconnection
from flask import jsonify

db = mongoconnection()

def gartnertype(typ):

	cursor = list(db.gartner.find({'conference-type':typ},{'fetch-date':0,'_id':0}))
	alldata = []
	for inp in cursor:
		alldata.append(inp)


	if alldata:	

		return jsonify(alldata)

	else:
		return "No Data Found"	



def gartnerall():

	cursor = list(db.gartner.find({},{'fetch-date':0,'_id':0}))
	alldata = []
	for inp in cursor:
		alldata.append(inp)


	if alldata:	

		return jsonify(alldata)

	else:
		return "No Data Found"


def techmemeall():

	cursor = list(db.techmeme.find({},{'fetch-date':0,'_id':0}))
	alldata = []
	for inp in cursor:
		alldata.append(inp)


	if alldata:	

		return jsonify(alldata)

	else:
		return "No Data Found"

