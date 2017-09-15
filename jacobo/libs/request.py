import urllib2
from libs.helper import random_from_file

class Request():
    url = None
    files = None
    settings = None
    p_user_agent = 'jacobo/1.1'

    user_agent = None
    def __init__(self, files, settings):
        self.files = files
        self.settings = settings

    def pull(self, url):
        self.url = url

    def set_user_agent(self, isa, irandom):
        if isa:
            self.p_user_agent = isa
        if irandom:
            self.p_user_agent = random_from_file(self.files['USER_AGENTS'])
                
    def request(self):
        request = urllib2.Request(self.url, None)
        request.get_method = lambda : 'GET'
        request.add_header('User-Agent', self.p_user_agent )

        response = urllib2.urlopen(request)
        print response.info()
