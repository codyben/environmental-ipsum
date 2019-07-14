import requests
from bs4 import BeautifulSoup
import time

i=0;

baseBlogUrl = "https://www.usgs.gov"

individualSoup = None;
individualData= None;

allTextString = "";

href = "";

f = open("usgs_pubs.txt","w+");
for i in range(1,120):
	BaseURL = "https://www.usgs.gov/products/publications/type/report?page="+str(i);
	data = requests.get(BaseURL);
	data.connection.close();
	time.sleep(0.5); #USGS doesn't like being constantly bombarded, so slowing down the scraping helps
	#print(data.content);
	soup = BeautifulSoup(data.content,'lxml');
	for title in soup.findAll("div",attrs = {'class':"col-sm-10"}) :
		href = title.find("a")['href'];
		if href == "/":
			continue;
		else:
			if(href[0:3] == "http"):
				break;
			print(href);
			individualData = requests.get(href);
			individualSoup = BeautifulSoup(individualData.content, 'lxml');
			for ipsumBuilder in individualSoup.findAll("div", attrs = {'class':'abstract-contents'}):
				for gc in ipsumBuilder.findAll("p"):
					#gc.find("img").decompose();
					f.write(gc.get_text()+"\n"); #write as we go, as the connection sometimes closes unexpectedly
f.close();
#print(allTextString);