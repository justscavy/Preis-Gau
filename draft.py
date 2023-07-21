# Base functions

# search_offers_by_name(offers: list[Offer], name: str) -> list[Offer]:
# ...

# search_offers_by_ocr(offers: list[Offer], file: Path) -> list[Offer]:
# ...

# Interactive console app:
# 
# print("Choose search option:")
# print("1. Search product by name")
# print("2. Search product using OCR")
# option = input("Enter your choice 1 or 2: ")
# if option == 1:
#   search_offers_by_name(...)
# elif option == 2:
#   search_offers_by_ocr(...)


# CLI:
#
# scrape.py --search-offers-by-name "Kaffee"
# oder
# scrape.py --search-offers-by-ocr --image-file $(pwd)/bs/testone.png

# ==> Argparse

# if args.search... == 'name':
#   search_offers_by_name(...)


# Optimierung des Todes!

# if option == 1:
#   search_offers_by_name(...)
# elif option == 2:
#   search_offers_by_ocr(...)

# =>
def search_offers_by_name():
    ...
def search_offers_by_ocr():
    ...

x = input('name or ocr')

search_by: dict = {
    'name': search_offers_by_name,                                #<---mapping example
    'ocr': search_offers_by_ocr
}

search_by[x](...)