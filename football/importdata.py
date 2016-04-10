#!/usr/bin/python

import requests
import json

'''
This is some documentation
http://api.football-data.org/documentation
curl -H 'X-Response-Control: minified' -X GET http://api.football-data.org/v1/soccerseasons/?season=2015
'''

class Import:
    def __init__(self, token):
        self.response = []

    def importurlfromrest(self, url):
        '''
        Wrapper around restful call to footbal-data.org
        :return: JSON response object
        '''
        headers = {
            'X-Auth-Token': token
           }
        response = requests.get(url,headers=headers)
        self.response = json.loads(response.content)
        return self.response
