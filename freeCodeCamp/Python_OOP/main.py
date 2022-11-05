# Naomi Tesla
# Python OOP Refresher from freeCodeCamp C:
# https://www.youtube.com/watch?v=Ej_02ICOIgs

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
    
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
