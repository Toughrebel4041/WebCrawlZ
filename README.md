# WebCrawlZ
#### Written by: Toughrebel4041
__        __       _       ____                         _  _____
\ \      / /  ___ | |__   / ___| _ __   __ _ __      __| ||__  /
 \ \ /\ / /  / _ \| '_ \ | |    | '__| / _` |\ \ /\ / /| |  / /
  \ V  V /  |  __/| |_) || |___ | |   | (_| | \ V  V / | | / /_
   \_/\_/    \___||_.__/  \____||_|    \__,_|  \_/\_/  |_|/____|
   
WebCrawlZ is a simple and fundamental web crawler tool that scans a website for all anchor (`&lt;a>`) tags and prints their `href` attributes. It is built using Python and utilizes the `requests`, `BeautifulSoup`, and `fake-useragent` libraries for web scraping and user agent spoofing. Additionally, it uses the `art` library for ASCII art.

## Features

- Fetches and prints all links from a given URL.
- Spoofs user agent to avoid blocking by websites.
- Provides error handling for various request exceptions.
- Displays an ASCII art title "WebCrawlZ" at the start.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/WebCrawlZ.git
cd WebCrawlZ
```

2. Install the Dependencies:
```bash
pip install -r requirements.txt
```

## Requirements
The tool requires the following Python libraries:
- requests
- beautifulsoup4
- fake-useragent
- art
These dependencies are listed in the requirements.txt file.

## Usage
To use the WebCrawlZ tool, run the following command and provide the URL when prompted:
```bash
python WebCrawlZ.py

Enter the URL: https://YourURL.com/
```

## Disclaimer
Please use this tool responsibly. Web scraping may be against the terms of service of some websites. Always ensure you have permission to scrape a website before doing so.

## This project is for educational purposes only.