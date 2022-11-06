from item import Item


class Keyboard(Item):
    pay_rate = 0.4
    def __init__(self, name: str, price: float, quantity=0):
        # Call to super function to gain access to attributes & methods
        super().__init__(
            name, price, quantity
        )

        # Assign attributes to self instance
        self.name = name
        self.price = price
        self.quantity = quantity