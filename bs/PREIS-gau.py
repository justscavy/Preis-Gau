from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time
import pytesseract
import cv2

def search_product_by_name(prices, search_term):
    found_products = []
    for product in prices.keys():
        if search_term.lower() in product.lower():
            found_products.append(product)
    return found_products

def search_product_by_ocr(prices, search_words):
    found_products = []
    for product in prices.keys():
        for word in search_words:
            if word.lower() in product.lower():
                found_products.append(product)
                break
    return found_products

def main():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 1280, "height": 1080})
        page.goto("https://edeka.de/eh/angebote.jsp")
        page.get_by_role("button", name="AKTIVIEREN").click()  # cookie akzeptieren (nicht notwendig)
        html = page.inner_html("#__next")  # body id =__next
        soup = BeautifulSoup(html, "html.parser")

        prices = {}                                             # creating a dict to match price with product
        items = soup.find_all(class_="has-size-s css-1olgk07")  # frames with product + price
        for item in items:                                      # for loop                             
            price = item.find(class_="css-1tty58m")             # find price div and nav it to price var
            product = item.find(class_="css-6ha7pe")            # find product name div and nav it to product var
            if product and price:
                prices[product.text] = price.text

        while True:
            valid = soup.find(class_="css-1skty0g")             #valid from till
            
            print(valid.text)
            print("Choose search option:")                      #choose method of search
            print("1. Search product by name")
            print("2. Search product using OCR")

            option = input("Enter your choice 1 or 2: ")

            if option == "1":
                search_term = input("Enter the product name: ")
                found_products = search_product_by_name(prices, search_term)
            elif option == "2":
                filename = input("Enter the filepath: ")
                image = cv2.imread(filename)
                search_words = pytesseract.image_to_string(image).split()
                found_products = search_product_by_ocr(prices, search_words)
            else:
                print("Invalid option. Please try again.")
                continue

            if found_products:
                for found_product in found_products:
                    print(f"Price of {found_product}: {prices[found_product]}")
            else:
                print("No products found matching the search criteria.")

            choice = input("Do you want to continue searching? (y/n): ")
            print("")
            if choice.lower() != "y":
                break

main()