from libs.log import Logging,Error, LogInit
from libs.parameters import Parameters
from libs.helper import Url

G = {
    'UA' : 'USER_AGENTS'
}

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
        url = Url(args.options.url)
        print url.base
        
    def set_files(self ,paths):
        self.files = paths
    def set_settings(self, settings):
        self.settings = settings

    def start(self):
        try:
            ##start
            self.run_app()
            
        except Exception as e:
            Error('Failed: ' + str(e))

