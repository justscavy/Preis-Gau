from enum import Enum, auto


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
   },
   'REWE': {
      'offer_tile': 'cor-offer-renderer-tile cor-link',
      'product_tile': 'cor-offer-information__title-link',
      'price_tile': 'cor-offer-price__tag-price',
      'validation_tile': 'sos-headings__duration'
   }
}
