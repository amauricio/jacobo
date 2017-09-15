from libs.log import Logging,Error, LogInit
from libs.parameters import Parameters
from libs.helper import Url
from libs.request import Request
from pprint import pprint


class JacoboMain():
    files = {}
    settings = {}
    def __init__(self):
        pass

    def run_app(self):
        ##start with presentation
        LogInit()
        ##set:) parameters
        args = Parameters()
        # URL sended by user
        url_from_cli = args.options.url
        url = Url(url_from_cli)

        ##start with request
        req = Request(self.files, self.settings)
        #assing url to project
        req.pull(url.link)
        ##set parameters
        opts = args.options
        req.set_user_agent(opts.user_agent, opts.random_agent)
        
        ##start application
        req.request()

    def set_files(self ,paths):
        self.files = paths
    def set_settings(self, settings):
        self.settings = settings

    def start(self):
        try:
            ##start application
            self.run_app()
        except Exception as e:
            pass
            Error('Failed: ' + str(e))

