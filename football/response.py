class Response():
    '''
    This is the base class for anything that holds restful response data
    '''

    def __init__(self, response):
        self._response = {}
        for response_attr in response:
            utf8_attr = response_attr.encode('ascii','ignore')
            if (type(response[response_attr]) == type(u'unicode')):
                self._response[utf8_attr] = response[response_attr].encode('ascii','ignore')
            else:
                if response_attr=='_links':
                    self._response[utf8_attr] = self.parse_links(response[response_attr])
                else:
                    self._response[utf8_attr] = response[response_attr]

    def parse_links(self, links):
        links_obj = {}
        for link in links:
            linkutf8 = link.encode('ascii','ignore')
            links_obj[linkutf8] = links[link][u'href'].encode('ascii','ignore')
        return links_obj