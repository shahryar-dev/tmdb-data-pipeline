# TMDB Data Pipeline: High-Performance Scraper

A lightweight, optimized data extraction pipeline built in Python to index movie metadata from The Movie Database (TMDB). 

##  Technical Highlights
- **Performance Optimized:** Bypassed heavy browser automation (like Playwright/Selenium) by engineering a pure-Scrapy HTTP request architecture, resulting in sub-5-second extraction times for 100+ records.
- **Data Normalization:** Extracted dynamic DOM elements using robust XPath and CSS selectors, cleaning and compiling the raw data into structured CSV formats suitable for Pandas analysis.
- **Ethical Crawling:** Implemented `AutoThrottle` and concurrent request limits to ensure compliance with server resources and API rate limits.

##  Tech Stack
- **Language:** Python 3.x
- **Framework:** Scrapy
- **Data Formats:** CSV, JSON

##  How to Run
1. Clone the repository.
2. Install dependencies: `pip install scrapy`
3. Execute the crawler: `scrapy runspider tmdb_scraper.py -o dataset.csv`