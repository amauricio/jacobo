from libs.modules.log import Logging,Error, LogInit
from libs.parameters import Parameters
from libs.modules.helper import Url
from libs.request import Request
from pprint import pprint


class JacoboMain():
    def __init__(self):
        pass

    def run_app(self):
        ##start with presentation
        LogInit()
        ##set:) parameters
        args = Parameters()
        opts = args.options
        
        # URL sended by user
        url = Url(args.options.url)

        ##start with request
        req = Request()
        
        #assing url to project
        req.pull(url.link)
        
        ##start application
        req.request()


    def start(self):
        try:
            ##start application
            self.run_app()
        except Exception as e:
            pass
            Error('Failed: ' + str(e))

