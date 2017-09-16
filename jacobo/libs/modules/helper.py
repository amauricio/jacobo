import re 
from libs.modules.log import Logging,Error, LogInit
import random

class Url():
    base = ()
    link = None
    ssl = False
    def __init__(self,host):
        host = str(host)
        if host[len(host) - 1] == '/':
            host = host[:-1]
        base_host = RegEx.host
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

def random_from_file(name_file ):
    with open(name_file) as file_content:
        content = file_content.readlines()
    return str.replace(random.choice(content), '\n', '')
    
class RegEx():
    normal_url = r"([a-z-A-Z0-9\-\.\_]+)"
    numbers = r"([0-9]+)"
    letters = r"([a-zA-Z]+)"

    host = r"((http(s?):)?(\/\/)?([a-zA-Z\.\-0-9\:]+)(\.[a-zA-Z]{2,3})?)(\/?)"