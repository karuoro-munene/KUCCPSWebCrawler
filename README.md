<p align="center>### Crawling KUCCPS Placement Data</p>

<p align="center">
    <a href="https://scrapy.org">
      <img alt="Scrapy src="https://scrapy.org/img/scrapylogo.png" />
    </a>    
  </p>

#### About:
* The scraper is built on [Scrapy](https://docs.scrapy.org/en/latest/index.html), an open source crawling framework built on python.
* The data crawled is on placement of Kenyan undergraduate students into local universities by [KUCCPS](https://kuccps.net/).
* The comprehensive JSON file of placement details is [here](https://github.com/MercurialMune/KUCCPSWebCrawler/blob/main/kuccps/programme_details.json).
* The placement details crawling script is [here](https://github.com/MercurialMune/KUCCPSWebCrawler/blob/main/kuccps/kuccps/spiders/programme_details.py)


#### Recreating the project
- clone this repo ``` ~/: git clone https://github.com/MercurialMune/KUCCPSWebCrawler.git```
- change directory to project ``` ~/: cd KUCCPSWebCrawler ```
- create a virtualenv; if on debian linux distros its ``` ~/: virtualenv -p /usr/bin/python3 virtual``` 
- activate the virtual environment ``` ~/:  source virtual/bin/activate```
- install the requirements ``` ~/: pip install -r requirements.txt```
- run any spider, for example, the [institution list](https://github.com/MercurialMune/KUCCPSWebCrawler/blob/main/kuccps/kuccps/spiders/institutions.py) spider ``` ~/: scrapy crawl institutions-table --output new-institutions.json --nolog```
- a new file named ```new institutions.json``` will appear in root directory of your project


#### Hire Me: 
Through this [email](mailto:munenecyp@gmail.com) or call on +254 769 703150 for scripts or projects


#### Licence:
Free
