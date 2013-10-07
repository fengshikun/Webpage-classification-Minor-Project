import re
import httplib
import urllib
from urlparse import urlparse
from BeautifulSoup import BeautifulSoup

regex = re.compile(
	r'(dir.yahoo.com/education/)'
        )


def isValidUrl(url):
    if regex.search(url) is not None:
        return True;
    return False

def crawler(SeedUrl,location):
    tocrawl=[SeedUrl]
  
    crawled=[]
   
    count = 0 
    var =0 
    while tocrawl:
        page=tocrawl.pop()
	links=[]
	#Fetch webpage
        response = urllib.urlopen(page)
	data=response.read()      # a `bytes` object
	s=data.decode('utf-8')
	s.encode('ascii','ignore')
        soup=BeautifulSoup(s)
        #print(s)
        title=soup.title.string
        print(title)
        #store file with title as file name
        f=open(location+"/"+title+".html","w+")
        f.write(s)
        f.close()
        print("Saved")
                
	'''find links in page'''
        links=soup.findAll('a',href=True)
        print(links)
	var=var+1
	    
        if page not in crawled:
            for l in links:
		#print l['href']
		
                if isValidUrl(l['href']):
                    tocrawl.append(l['href'])
       
            crawled.append(page)  
	#print var ,count 
   	if var > 40 : 
   		return crawled
    return 

url="http://dir.yahoo.com/education/"
dir="crawled/1"
crawler(url,dir)
