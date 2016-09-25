#!/usr/bin/env python
##
# wcgs 0.1.1-alpha
# release date:24/09/2016
# author: amaurcio
## $> python wcgs.py -u http://misitioweb.com

##pip install requests
###################################################

import sys
import re
import urllib
import getopt
import time
from optparse import OptionParser
import urllib2
import datetime

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
    action_pattern = r"\/\/(.+)\/([a-zA-Z\.\-\/]+)?"
    action = re.findall(action_pattern, host)
    if (action[0][1] != ''):
        base_host = base_host.replace('/' + action[0][1], '')
except:
    ##End if not parameters
    print 'Failed load options'
    sys.exit(0)


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


## -- Storage links --##
STORAGE = {
    'LINKS': [],
    'CSS': [],
    'JS': [],
    'FORMS': [],
    'EXTERN': []
}

## -- RegExpr -- ##
re_linkTag = r'((href|src)=(\'|\"))((http(s?):\/\/)?[a-zA-Z\:\/\.\?\=0-9\_\%\&\;\-]+\.\w{2,5})'
re_form = r'((action)=(\'|\"))((http(s?):\/\/)?[a-zA-Z\:\/\.\?\=0-9\_\%\&\;\-]+)'

coreExtendOld = []
theFuckingURLs = []
formsResources = []
forms = []
externalURLs = []
styleResources = []
scriptResources = []
imageResources = []
pushForNew = {}


##--Helpers--##
def log(str_message):
    now = datetime.datetime.now()
    print '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + '][LOG] ' + str_message
    sys.stdout.flush()


def log_info(str_message):
    now = datetime.datetime.now()
    print bcolors.OKBLUE + '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(
        now.second) + '][INF]\t' + str_message + bcolors.ENDC
    sys.stdout.flush()


def log_error(str_message):
    now = datetime.datetime.now()
    print bcolors.FAIL + '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(
        now.second) + '][ERR]\t' + str_message + bcolors.ENDC
    sys.stdout.flush()


def log_ok(str_message):
    now = datetime.datetime.now()
    print bcolors.OKGREEN + '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(
        now.second) + '][OK]\t' + str_message + bcolors.ENDC
    sys.stdout.flush()


def end():
    print '\n'
    log('Exiting...')
    sys.exit(0)


def request(url):
    log_info('GETTING: ' + url)
    try:
        response = urllib.urlopen(url)
        if (response.getcode() == 404):
            log_error('Status code : 404. Page not found')
            end()
        elif (response.getcode() == 200):
            log_ok('GET: ' + url)

        return response
    except Exception as e:
        log_error(str(e))
        end()


print '\n'
print '     8  8""""8 8""""8 8"""88 8""""8   8"""88'
print '     8  8    8 8    " 8    8 8    8   8    8'
print '     8e 8eeee8 8e     8    8 8eeee8ee 8    8'
print '     88 88   8 88     8    8 88     8 8    8'
print ' e   88 88   8 88   e 8    8 88     8 8    8'
print ' 8eee88 88   8 88eee8 8eeee8 88eeeee8 8eeee8'
print ' --'
print ' -- web crawler --'
print ' -- [GITHUB] https://github.com/amauricio/wcgs --'
print '\n'

print '[*] TARGET : ' + host
print ''
real_host = request(host)
print ''
print '#### HEADERS --------------------------------------------------------------------'
print ''
headers = real_host.info()
for k in headers:
    print bcolors.OKGREEN + '[*]' + '[' + k + '] ' + bcolors.ENDC + headers[k]
print '---------------------------------------------------------------------------------'
print ''


## -- Detect if link is incomplete - add host base --##
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
    # log_info('TO: '+mn)
    return mn


def getUrlFromScript(myUrlToScript):
    fs = []
    response = urllib.urlopen(myUrlToScript)
    html = response.read()
    newrsx = re.findall(r'(url([\n\r\ \t])*?:)([\n\r\ \t])+?(\'|\")(([\/a-zA-Z0-9])+)(\'|\")', html);
    if len(newrsx) > 0:
        for k in newrsx:
            if complete_url(k[4]) not in fs:
                fs.append(complete_url(k[4]))
    return fs


def re_analyzer(host):
    log_ok('Starting...')
    new_html = real_host.read()
    pushForNew['js'] = {}
    ##--Get link based SRC|HREF -- ##
    newrsx = re.findall(re_linkTag, new_html)
    print str(len(newrsx)) + ' enlaces encontrados'

    ##--Get link based ACTION -- ##
    forms = re.findall(re_form, new_html)
    print str(len(forms)) + ' form encontrados'

    # for init get url home
    for k in newrsx:
        theFuckingURLs.append(k[3])

    for f in forms:
        formsResources.append(complete_url(f[3]))

    urls = theFuckingURLs
    for u in urls:
        newhost = complete_url(u)
        u = newhost
    h = host.replace('http://www.', 'http://').replace('http://', '')
    ifIsLocal = u.find(h)
    if ifIsLocal == -1:
        if u not in externalURLs:
            externalURLs.append(u)
    else:
        if re.search(r"(.)*\.(jpg|png|gif|JPG|PNG|GIF)", u):
            if u not in imageResources:
                imageResources.append(u)
        elif re.search(r"(.)*\.(js|JS)", u):
            if u not in scriptResources:
                scriptResources.append(u)
                ins = getUrlFromScript(u)
        elif re.search(r"(.)*\.(css|CSS)", u):
            if u not in styleResources:
                styleResources.append(u)
        else:
            if u not in coreExtendOld:
                coreExtendOld.append(u)

    STORAGE['LINKS'] = coreExtendOld
    STORAGE['EXTERNAL'] = externalURLs
    STORAGE['CSS'] = styleResources
    STORAGE['FORMS'] = formsResources
    print str(len(styleResources)) + ' estilos encontrados'
    print str(len(scriptResources)) + ' scripts encontrados'
    print str(len(externalURLs)) + ' enlaces externos'
    return pushForNew


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
html += "<h2>Scripts--</h2>\n"

open("cat.html", "w");
with open("cat.html", "a+") as f:
    f.write(html)
