from bs4 import BeautifulSoup
import pytesseract
import cv2
import argparse
from argparse import RawTextHelpFormatter
from classes.offer import Offer
from utils.functions import get_html, search_offers_by_name, search_offers_by_ocr, extract_offers, extract_offers2
import sys
sys.stdout.reconfigure(encoding='utf-8')



VERSION="1.0.0"

parser = argparse.ArgumentParser(description="Search for offers with a product name or image.\nExample: python3 main.py -pn 'name'",
                                formatter_class=argparse.RawTextHelpFormatter)                         
parser.add_argument("-v", "--version", action="version", version=f"Version {VERSION}")
parser.add_argument("-pn", "--product", metavar="PRODUCT_NAME", type=str, help="search with a productname")
parser.add_argument("-oi", "--ocr", metavar="OCR_IMAGE", type=str, help="search with an image")
args = parser.parse_args()





def get_offers(url):   #edeka
    html_source: str = get_html(url=url)
    html: BeautifulSoup = BeautifulSoup(markup=html_source, features='html.parser')
    offers: list[Offer] = extract_offers(html=html)
    return offers



def get_offers_2(url):   #rewe
    html_source: str = get_html(url=url)
    html: BeautifulSoup = BeautifulSoup(markup=html_source, features='html.parser')
    offers: list[Offer] = extract_offers2(html=html)
    return offers

def main():
    edeka_url: str = 'https://www.edeka.de/eh/s%C3%BCdwest/edeka-barwig-z%C3%A4hringer-stra%C3%9Fe-344/angebote.jsp'
    rewe_url: str = "https://www.rewe.de/angebote/gundelfingen/831300/rewe-markt-alte-bundesstr-68-70/"
    if  args.product:
        search_term = args.product
        offers = get_offers(edeka_url)
        offers2 = get_offers_2(rewe_url)
        found_offers = search_offers_by_name(offers=offers, name=search_term)
        found_offers2 = search_offers_by_name(offers=offers2, name=search_term)
    elif args.ocr:
        filename = args.ocr
        offers = get_offers(edeka_url)
        offers2 = get_offers_2(rewe_url)
        image = cv2.imread(filename)
        search_words = pytesseract.image_to_string(image).split()
        found_offers = search_offers_by_ocr(offers=offers, ocr_detected_words=search_words)
        found_offers2 = search_offers_by_ocr(offers=offers2, ocr_detected_words=search_words)
   
   
   
    total_price_REWE = 0
    total_price = 0

    if found_offers:
        print("EDEKA\n")        
        for offer in found_offers:
            product = offer.product = offer.product.strip()
            price_str = offer.price.strip().replace("€", "").replace(",",".")   
            price = float(price_str)
            total_price += price           
            print(f"{offer.product.strip()}: {offer.price.strip()}")       # adding euro symbol?
    print("\nTotal price: {:.2f}\n\n\n".format(total_price))

    
    if found_offers2:
        print("REWE\n")
        for offer in found_offers2:
            product = offer.product = offer.product.strip()
            price_str_REWE = offer.price.strip().replace("€", "").replace(",",".")
            price_REWE = float(price_str_REWE)
            total_price_REWE += price_REWE  
            print(f"{offer.product.strip()}: {offer.price.strip()}")
    else:
        print("REWE")
        print("no offers found")
        sys.exit()
    print("\nTotal price: {:.2f}\n".format(total_price_REWE))
    


   

    
            


if __name__ == "__main__":
    main()
 










