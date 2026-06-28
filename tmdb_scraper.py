import scrapy

class TmdbSpider(scrapy.Spider):
    name = "tmdb"
    
    # All settings are self-contained here. No external files needed.
    custom_settings = {
        "ROBOTSTXT_OBEY": False,
        "USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 1.0,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
    }

    # Hardcoded URLs to completely avoid start_requests() indentation issues
    start_urls = [
        'https://www.themoviedb.org/movie?page=1',
        'https://www.themoviedb.org/movie?page=2',
        'https://www.themoviedb.org/movie?page=3',
        'https://www.themoviedb.org/movie?page=4',
        'https://www.themoviedb.org/movie?page=5'
    ]

    def parse(self, response):
        movie_cards = response.xpath('//div[contains(@class, "comp:poster-card")]')
        
        for card in movie_cards:
            relative_url = card.css('a::attr(href)').get()
            full_url = f"https://www.themoviedb.org{relative_url}" if relative_url else None
            title = card.css('h2.font-semibold span::text').get()

            # Prints to your terminal so you can watch it work
            self.logger.info(f"SUCCESS - SCRAPED: {title}")

            yield {
                'title': title,
                'release_date': card.css('span.subheader::text').get(),
                'movie_url': full_url
            }