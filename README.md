# Environmental Ipsum
The environmentally conscious way to make filler text!

## Files
- README.md
	- Self-explanatory.
- LICENSE
	- Self-explanatory.
- globe.gif
	- the spinning globe gif in the header.
	- Graciously borrowed from [here](http://bestanimations.com/Earth&Space/Earth/Earth4.html "globe.gif").
- index.html
	- Your standard index.
	- Styles are all inline (there weren't too many) .
- script.js
	- A small helper file which contains the (<10 lines) logic to communicate with the backend.
- usgs.py
	- Python scraper to grab the text content of USGS publication abstracts.
- nasa.py
	- Python scraper to grab the text content of NASA news articles.
- removeNames.cpp
	- Removes any line of text from markov_initial2.txt which contains more than two capital letters.
	- I wanted to avoid any potential proper nouns / names being generated, so this was my solution to this without spending time using R for named entity extraction :) .
	- No particular reason for this to be in c++, just wanted a change of pace.
- markov_initial2.txt
	- Output from the Markov library found [here](https://github.com/jsvine/markovify).
	- I didn't include the file itself, as my minor modifications didn't warrant a whole new file.
- clean_markov2.txt
	- Output from removeNames, used in the backend.
- usgs_pubs.txt
	- Scraped abstracts obtained from usgs.py.
- ipsum.php
	- Small PHP7 script to handle returning random ipsum sentences / paragraphs to the user.
- eipsum-cli.sh
	- Bash script so I can get environmentally conscious ipsum from my terminal :) .

## Running

If you wish to run everything as is, you'll need:
- g++ (or your preferred compiler)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- PHP7+ installed
	- If you remove type hinting, PHP5+ would work.
- Python 
	- v2 or v3 is fine.

## I just want my environmentally conscious ipsum!

[you're in luck](https://www.environmental-ipsum.com)

## I have an issue with a line of text generated!

Open up a pull request removing the line from the list of strings and I'll take a look.


 