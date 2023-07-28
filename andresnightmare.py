from utils import Market
from bs4 import BeautifulSoup
import pytesseract
import cv2
import argparse
from argparse import RawTextHelpFormatter
from classes.offer import Offer
import sys
from enum import Enum, auto
from dataclasses import dataclass
sys.stdout.reconfigure(encoding='utf-8')




@dataclass
class Offer:
    product: str
    price: str
    market: Market
    validation: str


@dataclass
class Container_offers                     #what do i need to get offers:
    Market_url: str                            #Url
    Market_name: Market                        #Offers tile
    offers:list[Offer]                                     #Price,
    Category: str                              #Category?,
    Validation_from: float                     #ValidationDate
    Validation_to: float
    ZIPCODE: int
    Address: str


class Market(Enum):                             
   """Provide market names, which are already implemented."""
   EDEKA = auto()
   REWE = auto()


MARKET_URLS: dict[str, str] = {
   'EDEKA': 'https://...'
}

HTML_CLASS_NAMES: dict[str, dict[str, str]] = {
   'EDEKA': {
      'offer_tile': 'css-1olgk07',
      'product_tile': 'css-6ha7pe',
      'price_tile': 'css-1tty58m',
      'validation_tile': 'css-1skty0g'
   },} 


parser = argparse.ArgumentParser(description="Search for offers with a product name or image.\nExample: python3 main.py -pn 'name'",
                                formatter_class=argparse.RawTextHelpFormatter)                         
parser.add_argument("-v", "--version", action="version", version=f"Version {VERSION}")
parser.add_argument("-pn", "--product", metavar="PRODUCT_NAME", type=str, help="search with a productname")
parser.add_argument("-oi", "--ocr", metavar="OCR_IMAGE", type=str, help="search with an image")
args = parser.parse_args()




def get_html(url: str) -> str:                                                                     
    """Retrieve the HTML content of a given URL and include JS changes."""
    options: Options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    html_source = driver.page_source
    driver.quit()
    return html_source                                       
                                           
                                          
def main():
    edeka_url: str = 'https://www.edeka.de/eh/s%C3%BCdwest/edeka-barwig-z%C3%A4hringer-stra%C3%9Fe-344/angebote.jsp'

    args.product:
    search_term = args.product
    offers = get_offers(edeka_url)
    found_offers = search_offers_by_name(offers=offers, name=search_term)                       
                                        



def get_offers(url):   #edeka
    html_source: str = get_html(url=url)
    html: BeautifulSoup = BeautifulSoup(markup=html_source, features='html.parser')
    offers: list[Offer] = extract_offers(html=html)
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
                                        
                                        

                                        

