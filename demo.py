
## $> python wcgs.py http://misitioweb.com
##
import sys
import re
import urllib
import getopt
import time

s = sys.argv[1:]
host = s[0]

isProcessing = True

admin_page = 'No se encuentra'
def load():
	print '/ \r'
	load()

def find_admin():
	f = open("admin")
	lines=f.read()
	explode=lines.split('\n');
	i=0
	for e in explode:
		print 'Calculando admin: ' + str(i) + ' de ' + str(len(explode)) +  " \r",
		is_admin = urllib.urlopen(host+e)
		if is_admin.getcode() == 200:
			print '\n'
			admin_page = host+e
			print admin_page
			break
		i+=1

coreExtendOld=[]
theFuckingURLs=[]
formsResources=[]
forms=[]
externalURLs=[]
styleResources=[]
scriptResources=[]
imageResources=[]
pushForNew={};

def complete_url(url):
	mn = url
	ifIsLocal = url.find('http')
	if ifIsLocal==-1:
		if host[len(host)-1] != '/' and url[0][0]!='/':
			url='/'+url
		if url[0][0]=='/':
			mn=host+url
	return mn

def getUrlFromScript(myUrlToScript):
	fs=[]
	response = urllib.urlopen(myUrlToScript)
	html = response.read()
	newrsx = re.findall(r'(url([\n\r\ \t])*?:)([\n\r\ \t])+?(\'|\")(([\/a-zA-Z0-9])+)(\'|\")',html);
	if len(newrsx)>0:
		for k in newrsx:
			if complete_url(k[4]) not in fs:
				fs.append(complete_url(k[4]))
	return fs

def re_analyzer(host):
	pushForNew['js'] = {}
	print 'Analizando sitio...\n'
	response = urllib.urlopen(host)
	html = response.read()
	new_html= html
	newrsx = re.findall(r'((href|src)=(\'|\"))((http(s?):\/\/)?[a-zA-Z\:\/\.\?\=0-9\_\%\&\;\-]+)',new_html);
	print str(len(newrsx)) + ' enlaces encontrados'
	forms = re.findall(r'((action)=(\'|\"))((http(s?):\/\/)?[a-zA-Z\:\/\.\?\=0-9\_\%\&\;\-]+)',new_html);
	print str(len(forms)) + ' form encontrados'
	#for init get url home
	for k in newrsx:
		theFuckingURLs.append(k[3])
	for f in forms:
		formsResources.append(complete_url(f[3]))
	urls = theFuckingURLs
	for u in urls:
		newhost = complete_url(u)
		u=newhost
		h=host.replace('http://www.', 'http://').replace('http://', '')
		ifIsLocal = u.find(h)
		if ifIsLocal==-1:
			if u not in  externalURLs:
				externalURLs.append(u)
		else:
			if re.search(r"(.)*\.(jpg|png|gif|JPG|PNG|GIF)", u):
				if u not in  imageResources:
					imageResources.append(u)
			elif re.search(r"(.)*\.(js|JS)", u):
				if u not in  styleResources:
					scriptResources.append(u)
					ins = getUrlFromScript(u)
					pushForNew['js'][u] = ins
			elif re.search(r"(.)*\.(css|CSS)", u):
				if u not in  styleResources:
					styleResources.append(u)
			else:
				if u not in  coreExtendOld:
					coreExtendOld.append(u)

	pushForNew['host']=coreExtendOld
	pushForNew['ex']=externalURLs
	pushForNew['css']=styleResources
	pushForNew['forms']=formsResources
	print str(len(styleResources)) + ' estilos encontrados'
	print str(len(scriptResources)) + ' scripts encontrados'
	print str(len(externalURLs)) + ' enlaces externos'
	isProcessing=False
	return pushForNew

find_admin()

gs=re_analyzer(host)


html = '<b>'+admin_page+'</b><br>'
html += "<h2>Enlaces--</h2>"
for h in gs['host']:
	html += '<a href="'+h+'">'+h +'</a><br>'

html += "<h2>Forms--</h2>"
for f in gs['forms']:
	html += '<a href="'+f+'">'+f +'</a><br>'

html += "<h2>Externos--</h2>"
for h in gs['ex']:
	html += '<a href="'+h+'">'+h +'</a><br>'

html += "<h2>Estilos-- </h2>"
for h in gs['css']:
	html += '<a href="'+h+'">'+h +'</a><br>'
html += "<h2>Scripts--</h2>"

for n in gs['js']:
	html += '<a href="'+n+'">'+n +'</a><br>'
	if len(gs['js'][n])>0:
		html += '<blockquote>'
		html += '<ul>'
		for g in gs['js'][n]:
			html += 'Enlaces dentro<br>'
			html += '<li>'
			html += '<a href="'+g+'">'+g +'</a><br>'
			html += '</li>'
		html += '</ul>'
open("cat.html","w");
with open("cat.html","a+") as f:
    f.write(html)





