import re 
from libs.log import Logging,Error, LogInit

class Url():
    base = ()
    link = None
    ssl = False
    def __init__(self,host):
        host = str(host)
        if host[len(host) - 1] == '/':
            host = host[:-1]
        base_host = r"((http(s?):)?(\/\/)?([a-zA-Z\.\-0-9]+)\.[a-zA-Z]{2,3})(\/?)"
        get_host = re.findall(base_host, host)
        if len(get_host)>0:
            host_data =  get_host[0]
            # clean regx
            if host_data[2] == 's':
                self.ssl = True
            self.link = host
            self.base = host_data
        else:
            Error('URL not valid')
        