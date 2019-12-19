#!usr/bin/python
import sys
import os
sys.path.append(os.getcwd())
from flask import Flask,request
from controller import gartnertype,gartnerall,techmemeall

app = Flask(__name__)


@app.route('/gartner',methods = ['GET'])
def gartner():
	if 'type' in request.args:
		typ1 = request.args['type']

		output = gartnertype(typ1)

		return output

	else:
		output = gartnerall()

		return output	



@app.route('/techmeme',methods = ['GET'])
def techmeme():

	output = techmemeall()

	return output


if __name__ == "__main__":
	app.run(debug = True)


