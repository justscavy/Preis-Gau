from datetime import datetime

import sqlite3
from main import get_offers, get_offers_2


current_date = datetime.now()

edeka_url: str = 'https://www.edeka.de/eh/s%C3%BCdwest/edeka-barwig-z%C3%A4hringer-stra%C3%9Fe-344/angebote.jsp'
rewe_url: str = "https://www.rewe.de/angebote/gundelfingen/831300/rewe-markt-alte-bundesstr-68-70/"

edeka_offers_list = get_offers(edeka_url)
rewe_offers_list = get_offers_2(rewe_url)




all_offers_edeka = []
for offer_edeka in edeka_offers_list:
    all_offers_edeka.append({
        "product": offer_edeka.product,
        "price": offer_edeka.price,
        "validation": offer_edeka.validation,
        "market": offer_edeka.market.name
    })

all_offers_rewe = []                            
for offer_rewe in rewe_offers_list:
    all_offers_rewe.append({
        "product": offer_rewe.product,
        "price": offer_rewe.price,
        "validation": offer_rewe.validation,
        "market": offer_rewe.market.name
    })


# Set the database file name to "ABC"
db_file_name = "offers.db"
connection = sqlite3.connect(db_file_name)
cursor = connection.cursor()

# create table and set name EDEKA
edeka_table_name = "EDEKA"

cursor.execute(f'''CREATE TABLE IF NOT EXISTS {edeka_table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product TEXT NOT NULL,
                    price TEXT NOT NULL,
                    validation TEXT NOT NULL,
                    market TEXT NOT NULL
                )''')

def insert_offer_into_db(cursor, edeka_table_name, offer_edeka):
    cursor.execute(f"INSERT INTO {edeka_table_name} (product, price, validation, market) VALUES (?, ?, ?, ?)",
                   (offer_edeka["product"], offer_edeka["price"], offer_edeka["validation"], offer_edeka["market"]))

# create table and set name REWE
rewe_table_name = "REWE"

cursor.execute(f'''CREATE TABLE IF NOT EXISTS {rewe_table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product TEXT NOT NULL,
                    price TEXT NOT NULL,
                    validation TEXT NOT NULL,
                    market TEXT NOT NULL
                )''')

def insert_offer_into_db(cursor, rewe_table_name, offer_rewe):
    cursor.execute(f"INSERT INTO {rewe_table_name} (product, price, validation, market) VALUES (?, ?, ?, ?)",
                   (offer_rewe["product"], offer_rewe["price"], offer_rewe["validation"], offer_rewe["market"]))

for offer_edeka in all_offers_edeka:
    if offer_edeka["market"] == "EDEKA":
        insert_offer_into_db(cursor, edeka_table_name, offer_edeka)

for offer_rewe in all_offers_rewe:
    if offer_rewe["market"] == "REWE":
        insert_offer_into_db(cursor, rewe_table_name, offer_rewe)

connection.commit()
connection.close()
