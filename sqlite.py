from pathlib import Path
import sqlite3
from sqlite3 import Connection, Cursor

from classes.offer import Offer
from utils import Market
from datetime import datetime



class DBManager:
    def __init__(self, db_file_name: Path) -> None:
        self.db_file_name = db_file_name
        self.connection: Connection = sqlite3.connect(db_file_name)
        self.cursor: Cursor = self.connection.cursor()
        self.markets: Market = Market
    
        for market in self.markets:
            self.cursor.execute(
                f'''CREATE TABLE IF NOT EXISTS {market.name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product TEXT NOT NULL,
                    price TEXT NOT NULL,
                    validation TEXT NULL,
                    market TEXT NOT NULL
                )'''
            )
            self.connection.commit()

    def __del__(self) -> None:
        self.connection.close()


    def insert_offer(self, market: Market, offer: Offer):
        if market == Market.EDEKA:
            self.insert_edeka_offer(table_name=market.name, offer=offer)
        elif market == Market.REWE:
            self.insert_rewe_offer(table_name=market.name, offer=offer)
        else:
            raise NotImplementedError(f"Market '{market.name}' is not implemented.")
        self.connection.commit()

    def insert_edeka_offer(self, table_name: str, offer: Offer):
        self.cursor.execute(
            f"INSERT INTO {table_name} (product, price, validation, market) VALUES (?, ?, ?, ?)",
            (offer.product, offer.price, offer.validation, offer.market.name)
        )

    def insert_rewe_offer(self, table_name, offer: Offer):
        self.cursor.execute(
            f"INSERT INTO {table_name} (product, price, validation, market) VALUES (?, ?, ?, ?)",
            (offer.product, offer.price, offer.validation, offer.market.name)
        )