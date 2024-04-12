from classes.offer import Offer
from sqlite import DBManager
from main import get_offers, get_offers_2
from utils import Market



edeka_url: str = 'https://www.edeka.de/eh/s%C3%BCdwest/edeka-barwig-z%C3%A4hringer-stra%C3%9Fe-344/angebote.jsp'
rewe_url: str = "https://www.rewe.de/angebote/gundelfingen/831300/rewe-markt-alte-bundesstr-68-70/"

edeka_offers: list[Offer] = get_offers(edeka_url)
rewe_offers: list[Offer] = get_offers_2(rewe_url)


db: DBManager = DBManager(db_file_name='offers.db')

for offer in edeka_offers:
    db.insert_offer(market=Market.EDEKA, offer=offer)

for offer in rewe_offers:
    db.insert_offer(market=Market.REWE, offer=offer)



