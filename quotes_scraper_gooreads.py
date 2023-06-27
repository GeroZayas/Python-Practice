import scrapy
from urllib.parse import urljoin
import os
from scrapy.selector import Selector


class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    start_url = input("Enter the URL of the book you want to scrape: ") 
    start_urls = [start_url]
    output_file = 'quotes_{}.txt'
    current_page = 1
    max_retries = 4
    counter = 0

    def parse(self, response):
        quotes = []

        # Extract quotes
        for quote in response.css('div.quoteText'):
            text = quote.css('::text').get().strip()
            quotes.append(text)

        # Get folder name from XPath
        folder_name = Selector(response).xpath('/html/body/div[2]/div[3]/div[1]/div[2]/h1/text()').get()
        folder_name = folder_name.strip().replace(' ', '-')

        # Create folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Save quotes to a text file
        if quotes:
            with open(f"{folder_name}/{self.output_file.format(self.current_page)}", 'w') as file:
                file.write(f"Source: {response.url}\n\n")
                for quote in quotes:
                    file.write(f"{quote}\n\n")

            self.log(f"Quotes saved in {folder_name}/{self.output_file.format(self.current_page)}")
        elif self.max_retries > 0:
            self.max_retries -= 1
            yield scrapy.Request(url=response.url, callback=self.parse)
        else:
            self.log(f"No quotes found on {response.url}. Max retries reached.")

        # Check if there is a next page
        next_page_disabled = response.css('span.next_page.disabled').get()
        if not next_page_disabled:
            self.current_page += 1
            next_url = urljoin(response.url, f'?page={self.current_page}')
            yield scrapy.Request(url=next_url, callback=self.parse)
        else:
            self.counter += 1

        # Check if counter reaches 3, stop running
        if self.counter >= 3:
            self.log("Reached maximum iterations. Stopping the spider.")
            return
