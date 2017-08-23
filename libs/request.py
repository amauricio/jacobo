import urllib2
import random

class Request():
    url = None
    files = None
    settings = None

    user_agent = None
    def __init__(self, files, settings):
        self.files = files
        self.settings = settings

    def pull(self, url):
        self.url = url

    def set_user_agent(self, isa):
        if isa:
            self.p_user_agent = isa

    def set_random_agent(self, isa):
        if isa:
            self.p_user_agent = self.get_agent()

    def get_agent(self):
        with open(self.files['USER_AGENTS']) as file_content:
            content = file_content.readlines()
        return random.choice(content)