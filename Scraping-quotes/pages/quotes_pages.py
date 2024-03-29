from bs4 import BeautifulSoup
from locators.quotes_page_locators import QuotesPageLocators
from parsers.quotes import QuoteParser
class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tag = self.soup.select(locator)
        #print(quote_tag)
        return [QuoteParser(e) for e in quote_tag]
