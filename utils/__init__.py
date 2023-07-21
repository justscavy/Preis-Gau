from enum import Enum, auto


class Market(Enum):                             
    """Provide market names, which are already implemented."""
    EDEKA = auto()
    

HTML_CLASS_NAME: dict[str, str] = {                     #this is a map -> dict
   'offer_tile': 'css-1olgk07',
   'product_tile': 'css-6ha7pe',
   'price_tile': 'css-1tty58m'
}
