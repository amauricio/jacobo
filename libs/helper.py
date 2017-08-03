import re 

class Url():
    base = ''
    ssl = False
    def __init__(self,host):
        host = str(host)
        if host[len(host) - 1] == '/':
            host = host[:-1]
        base_host = r"((http(s?):)?(\/\/)?([a-zA-Z\.\-0-9]+)\.([a-zA-Z]{2,3})(\/?))"
        get_host = re.findall(base_host, host)
        host_data =  get_host[0]

        '''
        if (len(get_host) > 1):
            if (action[0][1] != ''):
                base_host = base_host.replace('/' + action[0][1], '')
        '''
        if host_data[2] == 's':
            self.ssl = True
        self.base = base_host