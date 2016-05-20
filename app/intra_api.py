import requests
import urllib, urllib2, json

class IntraApi:
	def __init__(self, client_id, client_secret):
		self.client_id = client_id
		self.client_secret = client_secret

	def get_token(self):
		url = "https://api.intra.42.fr/oauth/token"
		data = {}
		data['grant_type'] = 'client_credentials';
		data['client_id'] = self.client_id
		data['client_secret'] = self.client_secret
		values = urllib.urlencode(data)
		print values
		req = urllib2.Request(url, values)
		response = urllib2.urlopen(req)
		res = json.load(response)
		print res
		self.token = res['access_token']
