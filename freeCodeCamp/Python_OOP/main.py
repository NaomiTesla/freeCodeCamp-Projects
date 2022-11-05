# Naomi Tesla
# Python OOP Refresher from freeCodeCamp C:
# https://www.youtube.com/watch?v=Ej_02ICOIgs

import csv

class Item:
    pay_rate = 0.8 # Pay rate after 20% discount :c
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Validates supplied arguments for instance
        assert price >= 0, f"Supplied price for {name}, {price}, is not >= zero! D:"
        assert quantity >= 0, f"Supplied quantity for {name}, {quantity}, is not >= zero! D:"
        
        # Assign attributes to self instance
        self.name = name
        self.price = price
        self.quantity = quantity

        # Default actions to run!! c:
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            csv_reader = csv.DictReader(f)
            items = list(csv_reader)
        for item in items:
            print(item)

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


Item.instantiate_from_csv()