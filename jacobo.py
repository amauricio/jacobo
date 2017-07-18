#!/usr/bin/env python
##
# jacobo 0.1.1-alpha
# release date:24/09/2016
# author: amauricio
## $> python jacobo.py -u http://misitioweb.com

##cat requeriments | sh
###################################################

import sys
import re
import urllib2
from optparse import OptionParser
import datetime
import random
from cookielib import CookieJar


## -- Options --##
parser = OptionParser()
parser.add_option("-u", dest="url",
                  help="URL to analize", metavar="[URL]")
parser.add_option("-A",
                  dest="agent",
                  metavar="[AGENT]",
                  help="User-Agent")

(options, args) = parser.parse_args()

## -- Define Host and normalize --##

try:
    host = options.url
    if host[len(host) - 1] == '/':
        host = host[:-1]
    base_host = host
    print base_host
    action_pattern = r"\/\/(.+)\/([a-zA-Z\.\-\/]+)?"
    action = re.findall(action_pattern, host)
    print action
    if (len(action) > 1):
        if (action[0][1] != ''):
            base_host = base_host.replace('/' + action[0][1], '')
except:
    ##End if not parameters
    print 'Failed load options'
    sys.exit(0)



# User agents
UA = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
    'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021029 Phoenix/0.4',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)'
]

# Storage links --##
STORAGE = {
    'LINKS': [],
    'CSS': [],
    'JS': [],
    'FORMS': [],
    'EXTERNAL': [],
    'IMAGES': [],
    'MAILS': []
}

## -- RegExpr -- ##
re_linkTag = r'((href|src)=(\'|\"))((http(s?):\/\/)?[a-zA-Z\:\/\.\?\=0-9\_\%\&\;\-]+\.\w{2,5})'
re_form = r'((action)=(\'|\"))((http(s?):\/\/)?[a-zA-Z\:\/\.\?\=0-9\_\%\&\;\-]+)'
re_mail = r'(([a-zA-Z0-9\_\.\-]+)@(.+\.\w{2,5}))'

##--Helpers--##

## -- Colors -- ##
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class Helper:
    @staticmethod
    def log(str_message):
        now = datetime.datetime.now()
        print '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + '][LOG] ' + str_message
        sys.stdout.flush()

    @staticmethod
    def log_info(str_message):
        now = datetime.datetime.now()
        print bcolors.OKBLUE + '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(
            now.second) + '][INF]\t' + str_message + bcolors.ENDC
        sys.stdout.flush()
    
    @staticmethod
    def log_error(str_message):
        now = datetime.datetime.now()
        print bcolors.FAIL + '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(
            now.second) + '][ERR]\t' + str_message + bcolors.ENDC
        sys.stdout.flush()

    @staticmethod
    def log_ok(str_message):
        now = datetime.datetime.now()
        print bcolors.OKGREEN + '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(
            now.second) + '][OK]\t' + str_message + bcolors.ENDC
        sys.stdout.flush()

    @staticmethod
    def end():
        print '\n'
        Helper.log('Exiting...')
        sys.exit(0)

    @staticmethod
    def request(url):
        Helper.log_info('GETTING: ' + url)
        try:
            cj = CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            req = urllib2.Request(url)
            req.add_header('User-Agent', random.choice(UA))
            response = opener.open(req)
            if (response.getcode() == 404):
                Helper.log_error('Status code : 404. Page not found')
                Helper.end()
            elif (response.getcode() == 200):
                Helper.log_ok('GET: ' + url)

            return response
        except Exception as e:
            Helper.log_error(str(e))
            Helper.end()


print '\n'
print '     8  8""""8 8""""8 8"""88 8""""8   8"""88'
print '     8  8    8 8    " 8    8 8    8   8    8'
print '     8e 8eeee8 8e     8    8 8eeee8ee 8    8'
print '     88 88   8 88     8    8 88     8 8    8'
print ' e   88 88   8 88   e 8    8 88     8 8    8'
print ' 8eee88 88   8 88eee8 8eeee8 88eeeee8 8eeee8'
print ' --'
print ' -- web crawler --'
print ' -- [GITHUB] https://github.com/amauricio/jacobo --'
print '\n'

print '[*] TARGET : ' + host
print ''
real_host = Helper.request(host)
print ''
print '#### HEADERS --------------------------------------------------------------------'
print ''
headers = real_host.info()
for k in headers:
    print bcolors.OKGREEN + '[*]' + '[' + k + '] ' + bcolors.ENDC + headers[k]
print '---------------------------------------------------------------------------------'
print ''


# Detect if link is incomplete - add host base --##
def complete_url(url):
    first_char = url[0][0]
    if (url[:4] == 'http'):
        # has host
        mn = url
    elif first_char == '/':
        mn = base_host + url
    elif first_char == '.':
        mn = base_host + url[1:]
    else:
        mn = base_host + '/' + url
    Helper.log_info('TO: '+mn)
    return mn


def getUrlFromScript(myUrlToScript):
    fs = []
    response = urllib2.urlopen(myUrlToScript)
    html = response.read()
    newrsx = re.findall(r'(url([\n\r\ \t])*?:)([\n\r\ \t])+?(\'|\")(([\/a-zA-Z0-9])+)(\'|\")', html);
    if len(newrsx) > 0:
        for k in newrsx:
            if complete_url(k[4]) not in fs:
                fs.append(complete_url(k[4]))
    return fs


def re_analyzer(host):
    Helper.log_ok('Starting...')
    new_html = real_host.read()

    # Declare variables

    push_js = []
    push_css = []
    push_images = []
    push_external = []
    push_general = []
    push_forms = []
    push_mails = []

    theFuckingURLs = []

    # Get link based SRC|HREF attribute
    Helper.log_info('Obteniendo enlaces...')
    newrsx = re.findall(re_linkTag, new_html)

    for k in newrsx:
        theFuckingURLs.append(k[3])

    # Get link based ACTION attribute
    Helper.log_info('Obteniendo formularios...')
    forms = re.findall(re_form, new_html)

    for k in forms:
        push_forms.append(k[3])

    # Get link based ACTION attribute
    Helper.log_info('Obteniendo mails...')
    mails = re.findall(re_mail, new_html)

    for k in mails:
        push_mails.append(k[0])

    # for init get url home
    for u in theFuckingURLs:
        newhost = complete_url(u)
        u = newhost
        h = host.replace('http://www.', 'http://').replace('http://', '')
        ifIsLocal = u.find(h)
        if ifIsLocal == -1:
            if u not in push_external:
                push_external.append(u)
        else:
            if re.search(r"(.)*\.(jpg|png|gif|JPG|PNG|GIF)", u):
                if u not in push_images:
                    push_images.append(u)
            elif re.search(r"(.)*\.(js|JS)", u):
                if u not in push_js:
                    push_js.append(u)
                    #ins = getUrlFromScript(u)
            elif re.search(r"(.)*\.(css|CSS)", u):
                if u not in push_css:
                    push_css.append(u)
            else:
                if u not in push_css:
                    push_general.append(u)

    STORAGE['LINKS'] = push_general
    STORAGE['EXTERNAL'] = push_external
    STORAGE['CSS'] = push_css
    STORAGE['JS'] = push_js
    STORAGE['FORMS'] = push_forms
    STORAGE['IMAGES'] = push_images
    STORAGE['MAILS'] = push_mails

    return STORAGE

gs = re_analyzer(host)

html = '<h1>' + host + '</h1><br>\n'
html += "<h2>Enlaces--</h2>"
for h in STORAGE['LINKS']:
    html += '<a href="' + h + '">' + h + '</a><br>\n'

html += "<h2>Forms--</h2>\n"
for f in STORAGE['FORMS']:
    html += '<a href="' + f + '">' + f + '</a><br>\n'

html += "<h2>Externos--</h2>\n"
for h in STORAGE['EXTERNAL']:
    html += '<a href="' + h + '">' + h + '</a><br>\n'

html += "<h2>Estilos-- </h2>\n"
for h in STORAGE['CSS']:
    html += '<a href="' + h + '">' + h + '</a><br>\n'

html += "<h2>Scripts-- </h2>\n"
for h in STORAGE['JS']:
    html += '<a href="' + h + '">' + h + '</a><br>\n'

html += "<h2>Mails-- </h2>\n"
for h in STORAGE['MAILS']:
    html += '<a href="' + h + '">' + h + '</a><br>\n'

open("cat.html", "w");
with open("cat.html", "a+") as f:
    f.write(html)
