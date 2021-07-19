import requests

from pages.quotes_pages import QuotesPage

page_content = requests.get('https://quotes.toscrape.com').content
page = QuotesPage(page_content)


for quote in page.quotes:
    print(quote)

