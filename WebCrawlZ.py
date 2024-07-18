import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from art import *

tprint("WebCrawlZ")
print("Web Crawling Tool by Toughrebel4041")
print("To use the Crawler:")
print("Enter website URL: https://yourUrl.com/")
print("\n")

#generate user_agent
user_agent = UserAgent()
headers = {'User-Agent': str(user_agent.chrome)}

#crawler func
def web_crawler(website_url):
    try:
        response = requests.get(website_url, headers=headers)
        response.raise_for_status()  #raise HTTPError for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')
	
	#extract and print all links on the webpage
        for hyperlink in soup.find_all('a'):
            print(hyperlink.get('href'))
	
        print(f"Scan Complete for: {website_url}")
    except requests.exceptions.RequestException as error:
        print(f"Error on scanning: {website_url}\nException: {error}")

#user input for the url
website_url = input('Enter website URL: ')
web_crawler(website_url)
