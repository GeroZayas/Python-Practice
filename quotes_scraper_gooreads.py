import scrapy

# TODO: Get other pages too

class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    start_urls = ['https://www.goodreads.com/work/quotes/69320126-the-madness-of-crowds']
    # TODO: make the output file name dynamic
    output_file = 'quotes.txt'

    def parse(self, response):
        quotes = []

        # Extract quotes
        for quote in response.css('div.quoteText'):
            text = quote.css('::text').get().strip()
            quotes.append(text)

        # Save quotes to a text file
        with open(self.output_file, 'w') as file:
            file.write(f"Source: {response.url}\n\n")
            for quote in quotes:
                file.write(f"{quote}\n\n")

        self.log(f"Quotes saved in {self.output_file}")
