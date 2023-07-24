from typing import Any
from bs4 import BeautifulSoup
from bs4.element import PageElement
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')
 


VERSION = "1.0.0"
from utils import HTML_CLASS_NAMES, Market
from classes.offer import Offer



def get_html(url: str) -> str:                                                                     
    """Retrieve the HTML content of a given URL and include JS changes."""
    options: Options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    html_source = driver.page_source
    driver.quit()
    return html_source


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


def extract_offers2(html: BeautifulSoup) -> list[Offer]:
    """Extract REWE offers from its offer tiles."""                                                                                      
    offers2: list[Offer] = []                                                               
    offer_tiles2: list[PageElement] = html.find_all(class_=HTML_CLASS_NAMES['REWE']['offer_tile'])   
    for offer_tile in offer_tiles2:                                                                                 
        product: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['REWE']['product_tile'])      
        price: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['REWE']['price_tile'])  
        validation: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['REWE']['validation_tile'])
        if product and price:
            offer2: Offer = Offer(
                product=product.text.strip(),
                price=price.text.strip(),  #LEARN HOWTO REGEX
                validation=validation,
                market=Market.REWE # "Hardcoded"
            )
            offers2.append(offer2)
    return offers2




def search_offers_by_name(offers: list[Offer], name: str) -> list[Offer]:
    return [offer for offer in offers if name.casefold() in offer.product.casefold()]


def search_offers_by_ocr(offers: list[Offer], ocr_detected_words: list[str]) -> list[Offer]:
    """Check offers containing any words of the einkaufslist!"""

    results: list[Offer] = []
    for offer in offers:
        for word in ocr_detected_words:
            if word.casefold() in offer.product.casefold():
                results.append(offer)
    return results



