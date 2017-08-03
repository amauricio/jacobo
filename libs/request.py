import urllib2


class Request():
    url = None
    def __init__(self):
        pass
    def pull(self, url):
        self.url = url

    def get_agent(self):
        with open(FILES['USER_AGENTS']) as f:
            content = f.readlines()