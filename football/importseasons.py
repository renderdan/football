#!/usr/bin/python

import requests
import json
import ast

'''
This is some documentation
http://api.football-data.org/documentation
curl -H 'X-Response-Control: minified' -X GET http://api.football-data.org/v1/soccerseasons/?season=2015
'''

class ImportSeasons:
    def __init__(self):
        self.seasons_list = []

    def importurlfromrest(self, url):
        '''
        Wrapper around restful call to footbal-data.org
        :return: JSON response object
        '''
        headers = {
            'X-Auth-Token': '38762f684dfb41f99dbb0fc3b9f7e70b'
           }
        response = requests.get(url,headers=headers)
        self.response = json.loads(response.content)
        return self.response
