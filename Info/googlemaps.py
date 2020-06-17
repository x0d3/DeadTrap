import urllib
import requests
from bs4 import BeautifulSoup

def trace(location):
    URL = f"https://www.google.com/maps?q={location}"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent" : USER_AGENT}
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
	    soup = BeautifulSoup(resp.content, "html.parser")
	    results = []
	    for g in soup.find_all('div', class_='r'):
		    anchors = g.find_all('a')
		    if anchors:
			    link = anchors[0]['href']
			    title = g.find('h3').text
			    item = title , link
			
			    results.append(item)
	    
	    return f"Location on google maps : {'\n'.join(map(str, results))}"