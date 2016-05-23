import requests
import urllib
import urllib2
import json


class IntraApi:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = ''
        self.cursus_id = ''

    def get_token(self):
        url = "https://api.intra.42.fr/oauth/token"
        data = {}
        data['grant_type'] = 'client_credentials'
        data['client_id'] = self.client_id
        data['client_secret'] = self.client_secret
        values = urllib.urlencode(data)
        # print values
        req = urllib2.Request(url, values)
        response = urllib2.urlopen(req)
        res = json.load(response)
        # print res
        self.token = res['access_token']

    def get_cursus(self):
        self.get_token()
        url = "https://api.intra.42.fr/v2/cursus?access_token=" + self.token + "&page=1"
        response = urllib2.urlopen(url)
        res = json.load(response)
        for elem in res:
            if elem['name'] == '42':
                self.cursus_id = str(elem['id'])

    def get_projects(self):
        self.get_cursus()
        projects = []
        for nb in range(4):
            url = "https://api.intra.42.fr/v2/cursus/" + self.cursus_id + \
                "/projects?access_token=" + self.token + "&page=" + str(nb)
            print url
            response = urllib2.urlopen(url)
            res = json.load(response)
            for elem in res:
                elem1 = [elem['id'], elem['name'], elem['description']]
                projects.append(elem1)
        return projects
