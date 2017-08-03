from time import gmtime, strftime

class Logging():
    def __init__(self, message, show_help=False):
        print '[-] '+message
        if show_help:
            print '\n'
            print 'For help : --help | -h'
            print '\n'

class Error():
    def __init__(self, message):
        p_print.fail(message)

class p_print:
    end = '\033[0m'
    @staticmethod
    def ok(message, bold=False):
        print ('\033[1m' if bold else '') + '\033[92m' + p_print.get_format_time() +' [INFO] ' + message + p_print.end
    @staticmethod
    def warn(message, bold=False):
        print ('\033[1m' if bold else '') +'\033[93m' + p_print.get_format_time() +' [INFO] ' + message + p_print.end
    @staticmethod
    def fail(message, bold=True):
        print ('\033[1m' if bold else '') +'\033[91m' + p_print.get_format_time() +' [ERROR] ' + message + p_print.end
    @staticmethod
    def log(message, bold=False):
        print ('\033[1m' if bold else '') + p_print.get_format_time() +' [LOG] ' + message + p_print.end
    @staticmethod
    def verbose(message, bold=False):
        print ('\033[1m' if bold else '') +  '\033[94m' + p_print.get_format_time() +' [LOG] ' + message + p_print.end

    @staticmethod
    def get_format_time():
        return strftime("[%H:%M:%S]", gmtime())

class LogInit():
    def __init__(self):
        init = '''
  _                 _           
 (_)               | |          
  _  __ _  ___ ___ | |__   ___  
 | |/ _` |/ __/ _ \| '_ \ / _ \ 
 | | (_| | (_| (_) | |_) | (_) |
 | |\__,_|\___\___/|_.__/ \___/ 
_/ |                            
|__/       

@version : 1.1
----- author : xorderexo 
----- twitter: @xorderexo 
----- github: http://github.com/amauricio
----- web : mauricio.pe
--------------------------------------------
'''
        print init