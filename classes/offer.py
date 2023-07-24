from dataclasses import dataclass

from utils import Market


@dataclass
class Offer:
    product: str
    price: str
    market: Market
    validation: str




# @dataclass
# class OfferContainer:
#     url: str
#     market: Market
#     valid_from: datetime
#     valid_to: datetime
#     offers: list[Offer]

#     def __post_init__(self):
#         html_source = get_html(url=self.url)
    
#     def search_offers_by_name(self, name: str) -> list[Offer]:
#         return [offer for offer in self.offers if name in offer.product]

#     def get_offers(self)
#     ... self.market.name

# offer_container = OfferContainer(url=MARKET_URL['EDEKA'])





# Protocol

# class OfferContainer(Protocol):
# # folgendermaßen musst du mindestens aussehen, wenn du ein offercontainer sein möchtest 
#     self.market
#     self.offers
#     self.valid_from
#     self.valid_to

# # und folgendes musst du mindestens können
#     def get_offers(product, price) -> list[Offers]:
#         ...
    
#     def search_offers(name: str):
#         ...


# @dataclass
# class EDEKAContainer:
#     market: str
#     offers: list[Offer]
#     valid_from: datetime
#     valid_to: datetime

#     def get_offers(product, price) -> list[Offers]:
#         offers: list[Offer] = []                                                               
#         offer_tiles: list[PageElement] = html.find_all(class_=HTML_CLASS_NAMES['EDEKA']['offer_tile'])   
#         for offer_tile in offer_tiles:                                                                                 
#             product: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['EDEKA']['product_tile'])      
#             price: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['EDEKA']['price_tile'])       
#             validation: str | None = offer_tile.find(class_=HTML_CLASS_NAMES['EDEKA']['validation_tile'])
#             if product and price:
#                 offer: Offer = Offer(
#                     product=product.text.strip(),
#                     price=price.text.strip(),
#                     validation=validation,
#                     market=Market.EDEKA # "Hardcoded"
                    
#                 )
#                 offers.append(offer)
#         return offers
