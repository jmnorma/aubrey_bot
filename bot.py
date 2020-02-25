import os
import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, json, request
import requests


kara_responses = ["Remember what room we're in?", 
"Remember food this time please", 
"Did you get taller?" ]

app = Flask(__name__)

@app.route('/', methods=['POST'])
def groupme_callback():
	json_body = request.get_json()
	if json_body['sender_type'] != 'bot':

		userName = json_body['name']
		### BOT CODE GOES HERE! ###
		if userName == os.environ['username']:
			message = "@Kara Cervetti "+random.choice(kara_responses)
			reply(message)
	
	return "ok", 200

def reply(message):
	payload = {
		'bot_id' : os.environ['BOT_ID'],
		'text'   : message,
	}
	request = Request('https://api.groupme.com/v3/bots/post', urlencode(payload).encode())
	json = urlopen(request).read().decode()



if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	# app.run(host='0.0.0.0', port=port, debug=True)
	app.run(host='0.0.0.0', port=port)