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
            if elem['slug'] == 'piscine-c-a-distance':
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

    def create_User(self, mail, fname, lname, campus_id='1', cursus_id='1'):
        self.get_cursus()
        url = "https://api.intra.42.fr/v2/users"
        data = {}
        data['access_token'] = self.token
        data['email'] = mail
        data['first_name'] = fname
        data['last_name'] = lname
        data['campus_id'] = campus_id
        data['cursus_id'] = cursus_id
        values = urllib.urlencode(data)
        req = urllib2.Request(url, values)
        response = urllib2.urlopen(req)
        return response

    def subscribe_User_To_Cursus(self, user_id, cursus_id='1'):
        self.get_cursus()
        url = "https://api.intra.42.fr/v2/cursus_users"
        data = {}
        data['access_token'] = self.token
        data['cursus_id'] = cursus_id
        data['user_id'] = user_id
        values = urllib.urlencode(data)
        req = urllib2.Request(url, values)
        response = urllib2.urlopen(req)
        return response

    def subscribe_User_To_Project(self, project_id, user_id):
        self.get_cursus()
        url = "https://api.intra.42.fr/v2/" + project_id + "/projects_users"
        data = {}
        data['access_token'] = self.token
        data['user_id'] = user_id
        values = urllib.urlencode(data)
        req = urllib2.Request(url, values)
        response = urllib2.urlopen(req)
        return response

