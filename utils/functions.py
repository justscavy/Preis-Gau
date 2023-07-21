from typing import Any
from bs4 import BeautifulSoup
from bs4.element import PageElement
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from utils import HTML_CLASS_NAME, Market
from classes.offer import Offer

VERSION = "1.0.0"

def get_html(url: str) -> str:                                                                     #
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
                                                                                           # HTML_CLASS_NAME = MAP to offers,product,price id from url
    offers: list[Offer] = []                                                               # creating a list to match price with product
    offer_tiles: list[PageElement] = html.find_all(class_=HTML_CLASS_NAME['offer_tile'])   # filling list with product+price offfers via PageElement(bs4 class)
    for offer_tile in offer_tiles:                                                         # starting loop                         
        product: str | None = offer_tile.find(class_=HTML_CLASS_NAME['product_tile'])      # find product name div and nav it to product var
        price: str | None = offer_tile.find(class_=HTML_CLASS_NAME['price_tile'])          # find price div and nav it to price var
        if product and price:
            # offers[product.text] = price.text
            offer: Offer = Offer(
                product=product.text,
                price=price.text,
                market=Market.EDEKA # "Hardcoded"
            )
            offers.append(offer)
    return offers


def search_offers_by_name(offers: list[Offer], name: str) -> list[Offer]:
    """Check if there are any offers containing a given string."""

    # results: list = []
    # for product in product.keys():
    #     if name.casefold() in product.casefold():
    #         results.append(product)
    # return results

    # "List Comprehension"
    return [offer for offer in offers if name.casefold() in offer.product.casefold()]


def search_offers_by_ocr(offers: list[Offer], ocr_detected_words: list[str]) -> list[Offer]:
    """Check offers containing any words of the einkaufslist!"""

    results: list[Offer] = []
    for offer in offers:
        for word in ocr_detected_words:
            if word.casefold() in offer.product.casefold():
                results.append(offer)
    return results




def parse_arguments(argparse):
    parser = argparse.ArgumentParser(description="Search for offers with a product name or an image. Example: python3 main.py --mode 1 --product-name 'name'")
    parser.add_argument("-v", "--version", action="version", version=f"Version {VERSION}")
    parser.add_argument("--mode", type=int, choices=[1, 2, 3], required=True, help="Choose to search by Product(1), OCR(2) or Exit(3)")
    parser.add_argument("--product-name", metavar="PRODUCT_NAME", type=str, help="Product name for search mode 1")
    parser.add_argument("--ocr-image", metavar="OCR_IMAGE", type=str, help=" Filepath to OCR image for search mode 2")

    return parser.parse_args()

#def parse_arguments(argparse):
#    parser = argparse.ArgumentParser(description="Search for offers with a product name or an image. Example: python3 main.py --mode 1 --product-name 'name'")
#    parser.add_argument("-v", "--version", action="version", version=f"Version {VERSION}")
#    parser.add_argument("--mode", type=int, choices=[1, 2, 3], required=True, help="Choose to search by Product(1), OCR(2) or Exit(3)")
#    parser.add_argument("--product-name", type=str, help="Product name for search mode 1")
#    parser.add_argument("--ocr-image", type=str, help=" Filepath to OCR image for search mode 2")
   # parser.add_argument("--exit", action="store_true", help=" Exit the programm mode 3")

    return parser.parse_args()


