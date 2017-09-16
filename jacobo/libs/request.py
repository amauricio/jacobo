import urllib2
from libs.modules.helper import random_from_file
from libs.http.Fetcher import Fetcher
import app.settings as settings
class Request():
    
    url = None
    p_user_agent = 'jacobo/1.1'

    user_agent = None
    def __init__(self):
        pass

    def pull(self, url):
        self.url = url

    def set_user_agent(self, isa, irandom):
        if isa:
            self.p_user_agent = isa
        if irandom:
            self.p_user_agent = random_from_file(settings.USER_AGENTS)
                
    def request(self):
        fetcher = Fetcher(self.url)
        fetcher.get()
