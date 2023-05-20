import requests
import cred.credentials as creds

url = "https://twelve-data1.p.rapidapi.com/stocks"

querystring = {"exchange":"NASDAQ","format":"json"}

headers = {
	"X-RapidAPI-Key": creds.creds['twelveData']['apiKey'],
	"X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
