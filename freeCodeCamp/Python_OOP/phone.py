from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to gain access to attributes & methods
        super().__init__(
            name, price, quantity
        )

        # Validates supplied argument for instance
        assert broken_phones >= 0, f"Supplied broken quantity for {name}, {broken_phones}, is not >= zero! D:"

        # Assign attributes to self instance
        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones
