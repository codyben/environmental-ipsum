import requests
from bs4 import BeautifulSoup
i=0;
#BaseURL = "https://climate.nasa.gov/blog/?page="+i;
baseBlogUrl = "https://climate.nasa.gov"

individualSoup = None;
individualData= None;

allTextString = "";

href = "";

f = open("ipsum.txt","w+");
for i in range(1,23):
	BaseURL = "https://climate.nasa.gov/blog/?page="+str(i);
	data = requests.get(BaseURL);
	soup = BeautifulSoup(data.content,'lxml');
	for title in soup.findAll("h1",attrs = {'class':"article_title"}) :
		href = title.find("a")['href'];
		if href == "/": #handle an edge case where some links are incorrect on the site.
			continue;
		else:
			href = baseBlogUrl+href;
			print(href);
			individualData = requests.get(href);
			individualSoup = BeautifulSoup(individualData.content, 'lxml');
			for ipsumBuilder in individualSoup.findAll("div", attrs = {'class':'wysiwyg_content'}):
				for gc in ipsumBuilder.findAll("p"):
					allTextString += gc.get_text()+"\n";

f.write(allTextString+"\n");
f.close();
#print(allTextString);