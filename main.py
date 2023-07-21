from bs4 import BeautifulSoup
import pytesseract
import cv2
import argparse

from classes.offer import Offer
from utils.functions import get_html, search_offers_by_name, search_offers_by_ocr, extract_offers

VERSION="1.0.0"

parser = argparse.ArgumentParser(description="Search for offers with a product name or an image. Example: python3 main.py --mode 1 --product-name 'name'")
parser.add_argument("-v", "--version", action="version", version=f"Version {VERSION}")
parser.add_argument("--product", "-pn", metavar="PRODUCT_NAME", type=str, help="Product name for search mode 1")
parser.add_argument("--ocr", "-oi", metavar="OCR_IMAGE", type=str, help=" Filepath to OCR image for search mode 2")
args = parser.parse_args()



def get_offers(url):
    html_source: str = get_html(url=url)
    html: BeautifulSoup = BeautifulSoup(markup=html_source, features='html.parser')
    offers: list[Offer] = extract_offers(html=html)
    return offers

def main():
    edeka_url: str = 'https://www.edeka.de/eh/s%C3%BCdwest/edeka-barwig-z%C3%A4hringer-stra%C3%9Fe-344/angebote.jsp'
    if  args.product:
        search_term = args.product
        offers = get_offers(edeka_url)
        found_offers = search_offers_by_name(offers=offers, name=search_term)
    elif args.ocr:
        filename = args.ocr
        offers = get_offers(edeka_url)
        image = cv2.imread(filename)
        search_words = pytesseract.image_to_string(image).split()
        found_offers = search_offers_by_ocr(offers=offers, ocr_detected_words=search_words)
    if found_offers:
        for offer in found_offers:
            print(f"Price of {offer.product}: {offer.price}")

    #while True:
    #    
    #    edeka_url: str = 'https://www.edeka.de/eh/s%C3%BCdwest/edeka-barwig-z%C3%A4hringer-stra%C3%9Fe-344/angebote.jsp'  
    #    if parse_arguments(argparse).mode == 1:
    #        search_term = parse_arguments(argparse).product_name
    #        offers = get_offers(edeka_url)
    #        found_offers = search_offers_by_name(offers=offers, name=search_term)
    #    elif parse_arguments(argparse).mode == 2:
    #        filename = parse_arguments(argparse).ocr_image
    #        offers = get_offers(edeka_url)
    #        image = cv2.imread(filename)
    #        search_words = pytesseract.image_to_string(image).split()
    #        found_offers = search_offers_by_ocr(offers=offers, ocr_detected_words=search_words)
    #        #if parse_arguments(argparse).mode == 3:
    #        # break
    #    else:
    #        print("Invalid option. Please try again.")
    #        continue
#
    #    if found_offers:
    #        for offer in found_offers:
    #            print(f"Price of {offer.product}: {offer.price}")
    #    else:
    #        print("No products found matching the search criteria.")
#
    #    choice = input("Do you want to continue searching? (y/n): ")                #need to add loop recall to continue product stumble
    #    print("")
    #    if choice.lower() == "y":
    #        break                                         #andres nightmare
    #        #
    #        # search_term = input("Enter the product name: ")
    #        #
    #        # edeka_url: str = 'https://www.edeka.de/eh/s%C3%BCdwest/edeka-barwig-z%C3%A4hringer-stra%C3%9Fe-344/angebote.jsp'  
    #        #
    #        # html_source: str = get_html(url=edeka_url)
    #        #
    #        # html: BeautifulSoup = BeautifulSoup(markup=html_source, features='html.parser')
            #
            # offers: list[Offer] = extract_offers(html=html)
            #
            # found_offers = search_offers_by_name(offers=offers, name=search_term)


#        else:
#            exit
#            
#
if __name__ == "__main__":
    main()
 










