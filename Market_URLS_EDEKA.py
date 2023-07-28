from enum import Enum
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from dataclasses import dataclass
from bs4.element import PageElement

class Market(Enum):
    MARKET1 = "https://www.edeka.de/eh"
    MARKET2 = "https://www.rewe.de/angebote"

market1_urls = [
    Market.MARKET1.value + "/nord/schlemmermarkt-struve-poststr.-36/index.jsp",
    Market.MARKET1.value + "/südwest/e-center-gundelfingen-gewerbestraße-23/index.jsp",
    Market.MARKET1.value + "/südwest/scheck-in-center-hainer-weg-56-80/angebote.jsp",
]

market2_urls = [
    Market.MARKET2.value + "/gundelfingen/831300/rewe-markt-alte-bundesstr-68-70/",
    Market.MARKET2.value + "/berlin-alt-treptow/4040712/rewe-markt-kiefholzstr-50/",
    Market.MARKET2.value + "/angebote/frankfurt-am-main/320168/rewe-markt-thudichumstrasse-18-22/",
]

HTML_CLASS_NAMES: dict[str, dict[str, str]] = {
   'EDEKA': {
      'offer_tile': 'css-1olgk07',
      'product_tile': 'css-6ha7pe',
      'price_tile': 'css-1tty58m',
      'validation_tile': 'css-1skty0g'}} 

@dataclass
class Container_offers:
    Market_url: str
    Market_name: str
    offers: list
    Category: str
    Validation_from: float
    Validation_to: float
    ZIPCODE: int
    Address: str


def get_html(urls: list) -> list:
    options: Options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    html_sources = []
    for url in urls:
        driver.get(url)
        html_sources.append(driver.page_source)
    driver.quit()
    return html_sources

def extract_offers(html: BeautifulSoup) -> list[Container_offers]:
    """Extract EDEKA offers from its offer tiles."""                                                                                      
    offers: list[Container_offers] = []                                                               
    offer_tiles: list[PageElement] = html.find_all(class_=HTML_CLASS_NAMES['EDEKA']['offer_tile'])   
    for offer_tile in offer_tiles:                                                                                 
        product: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['EDEKA']['product_tile'])      
        price: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['EDEKA']['price_tile'])       
        validation: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['EDEKA']['validation_tile'])
        if product and price:
            offer: Container_offers = Container_offers(
                product=product.text.strip(),
                price=price.text.strip(),
                validation=validation,
                market=Market.EDEKA # "Hardcoded"
                
            )
            offers.append(offer)
    return offers

    



def get_offers(urls: list):
    html_sources = get_html(urls)
    offers = extract_offers(html_sources)
    return offers



#def extract_offers(html: BeautifulSoup) -> list[Container_offers]:
#    """Extract EDEKA offers from its offer tiles."""                                                                                      
#    offers: list[Container_offers] = []                                                               
#    offer_tiles: list[PageElement] = html.find_all(class_=HTML_CLASS_NAMES['EDEKA']['offer_tile'])   
#    for offer_tile in offer_tiles:                                                                                 
#        product: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['EDEKA']['product_tile'])      
#        price: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['EDEKA']['price_tile'])       
#        validation: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['EDEKA']['validation_tile'])
#        if product and price:
#            offer: Container_offers = Container_offers(
#                product=product.text.strip(),
#                price=price.text.strip(),
#                validation=validation,
#                market=Market #                    
#            )
#            offers.append(offer)
#    return offers
'''
def get_offers(url):   #edeka
    html_source: str = get_html(url=url)
    html: BeautifulSoup = BeautifulSoup(markup=html_source, features='html.parser')
    offers: list[Container_offers] = extract_offers(html=html)
    return offers

def extract_offers(html: BeautifulSoup) -> list[Offer]:
    """Extract EDEKA offers from its offer tiles."""                                                                                      
    offers: list[Offer] = []                                                               
    offer_tiles: list[PageElement] = html.find_all(class_=HTML_CLASS_NAMES['EDEKA']['offer_tile'])   
    for offer_tile in offer_tiles:                                                                                 
        product: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['EDEKA']['product_tile'])      
        price: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['EDEKA']['price_tile'])       
        validation: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['EDEKA']['validation_tile'])
        if product and price:
            offer: Offer = Offer(
                product=product.text.strip(),
                price=price.text.strip(),
                validation=validation,
                market=Market.EDEKA # "Hardcoded"
                
            )
            offers.append(offer)
    return offers

def get_html_for_multiple_urls(url_list: list) -> dict:
    """Retrieve the HTML content for multiple URLs and store them in a dictionary."""
    result_dict = {}
    for url in url_list:
        html_content = get_html(url)
        result_dict[url] = html_content
    return result_dict





# Get HTML content for Market1 URLs
market1_html_dict = get_html_for_multiple_urls[market1_urls]

# Get HTML content for Market2 URLs
market2_html_dict = get_html_for_multiple_urls[market2_urls] 

HTML_CLASS_NAMES: dict[str, dict[str, str]] = {
   'EDEKA': {
      'offer_tile': 'css-1olgk07',
      'product_tile': 'css-6ha7pe',
      'price_tile': 'css-1tty58m',
      'validation_tile': 'css-1skty0g'
'''


