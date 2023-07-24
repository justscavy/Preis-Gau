from enum import Enum, auto


class Market(Enum):                             
    """Provide market names, which are already implemented."""
    EDEKA = 1
    REWE = 2
    
    






HTML_CLASS_NAME_EDEKA: dict[str, str] = {                     #this is a map -> dict
   'offer_tile': 'css-1olgk07',
   'product_tile': 'css-6ha7pe',
   'price_tile': 'css-1tty58m',
   'validation_tile': 'css-1skty0g'
}

HTML_CLASS_NAME_REWE: dict[str, str] = {                     #this is a map -> dict
   'offer_tile': 'cor-offer-renderer-tile cor-link',
   'product_tile': 'cor-offer-information__title-link',
   'price_tile': 'cor-offer-price__tag-price',
   'validation_tile': 'sos-headings__duration'
} 
