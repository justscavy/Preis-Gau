from dataclasses import dataclass

from utils import Market


@dataclass
class Offer:
    product: str
    price: str
    market: Market


# @dataclass
# class OfferContainer:
#     url: str
#     offers: list[Offer]

#     def __post_init__(self):
#         html_source = get_html(url=self.url)
    
#     def search_offers_by_name(self, name: str) -> list[Offer]:
#         return [offer for offer in self.offers if name in offer.product]

# offer_container = OfferContainer(url=MARKET_URL['EDEKA'])