import requests

class IntraApi:
	def __init__(self, client_id, client_secret):
		self.client_id = client_id
		self.client_secret = client_secret

	def get_token(self):
		url = "https://api.intra.42.fr/oauth/token?grant_type=client_credentials&client_id=%s&client_secret=%s" % (self.client_id, self.client_secret)
		print url
