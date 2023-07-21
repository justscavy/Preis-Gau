from bs4 import BeautifulSoup
import pytesseract
import cv2
import argparse

from classes.offer import Offer
from utils.functions import get_html, search_offers_by_name, search_offers_by_ocr, extract_offers, parse_arguments


def main():
    while True:
        found_offers = []  # Initialize an empty list for found offers in each iteration

        while True:
            mode_choice = input("Select search mode (1: By product name, 2: By OCR, q: Quit): ")
            
            if parse_arguments(argparse).mode == 1:
                search_term = parse_arguments(argparse).product_name
                edeka_url: str = 'https://www.edeka.de/eh/s%C3%BCdwest/edeka-barwig-z%C3%A4hringer-stra%C3%9Fe-344/angebote.jsp'   
                html_source: str = get_html(url=edeka_url)
                html: BeautifulSoup = BeautifulSoup(markup=html_source, features='html.parser')
                offers: list[Offer] = extract_offers(html=html)
                found_offers = search_offers_by_name(offers=offers, name=search_term)
                break
            elif parse_arguments(argparse).mode == 1:
                filename = input("Enter the image file name: ")
                edeka_url: str = 'https://www.edeka.de/eh/s%C3%BCdwest/edeka-barwig-z%C3%A4hringer-stra%C3%9Fe-344/angebote.jsp'
                html_source: str = get_html(url=edeka_url)
                html: BeautifulSoup = BeautifulSoup(markup=html_source, features='html.parser')
                offers: list[Offer] = extract_offers(html=html)
                image = cv2.imread(filename)
                search_words = pytesseract.image_to_string(image).split()
                found_offers = search_offers_by_ocr(offers=offers, ocr_detected_words=search_words)
                break
            elif mode_choice.lower() == "q":
                return
            else:
                print("Invalid option. Please try again.")

        if found_offers:
            for offer in found_offers:
                print(f"Price of {offer.product}: {offer.price}")
        else:
            print("No products found matching the search criteria.")

        choice = input("Do you want to continue searching? (y/n): ")
        print("")
        if choice.lower() != "y":
            return


if __name__ == "__main__":
    main()
