import urllib2
from libs.http.Headers import Headers
from libs.http.Cookies import Cookies
import app.settings as settings 
class Fetcher():
    
    robots = 'robots.txt'

    my_url = None
    my_request = None
    my_response = None

    my_headers = Headers.lst
    my_cookies = Cookies.lst

    def __init__(self, url):
        self.my_url = url
    
    def get(self):
        self.my_request = urllib2.Request(self.my_url, None)
        self.my_request.get_method = lambda : 'GET'

        self.my_response = urllib2.urlopen(self.my_request, timeout= settings.CONNECTION_TIME )
        print self.my_response.headers
    
    def handler_response(self):
        self.response_info = self.my_response.headers
        Headers.push_from_response(self.response_info)
    
