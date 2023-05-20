import requests
import cred.credentials as creds


def get12Data(qString=dict, outputLoc=str):
    
	url = "https://twelve-data1.p.rapidapi.com/stocks"
	querystring = qString

	headers = {
		"X-RapidAPI-Key": creds.creds['twelveData']['apiKey'],
		"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	# response = {'test':1234}

	return response.text









