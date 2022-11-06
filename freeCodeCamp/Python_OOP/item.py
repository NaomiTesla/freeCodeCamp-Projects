import os
import csv


class Item:
    pay_rate = 0.8  # Pay rate after 20% discount :c
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Validates supplied arguments for instance
        assert price >= 0, f"Supplied price for {name}, {price}, is not >= zero! D:"
        assert quantity >= 0, f"Supplied quantity for {name}, {quantity}, is not >= zero! D:"

        # Assign attributes to self instance
        self.__name = name  # Double underscore prefix makes attribute inaccessible
        self.__price = price
        self.quantity = quantity

        # Default actions to run!! c:
        Item.all.append(self)

    # Property decorator makes attribute read only! c:
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    # Setter that allows users to change name value
    @name.setter
    def name(self, value):
        if len(value) > 50:
            raise Exception("Name cannot be greater than 50!")
        else:
            self.__name = value

    @price.setter
    def price(self, value):
        if value > 1000000:
            raise Exception("Price cannot be greater than $1,000,000!")
        else:
            self.__price = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @classmethod
    def instantiate_from_csv(cls):
        # Current file directory, useful when running in vscode c:
        cfd = os.path.join(os.path.dirname(__file__)) + '\\'
        with open(cfd + 'items.csv', 'r') as f:
            csv_reader = csv.DictReader(f)
            items = list(csv_reader)

        for item in items:
            Item(
                name=str(item.get('name')),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # This basically just checks for floats ending in only '.0'
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, float):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}', '{self.quantity}')"

    def __connect(self, smtp_server):
        print(f"""
        <==================================================>
                    Connecting to {smtp_server}...
                    Connected to  {smtp_server}!
        <==================================================>
        """)

    def __prepare_body(self):
        print(f"""
        <==================================================>
        <sender: naomiselectronics@email.com>,
        <recipient: customer@email.com>,
        <Coordinated Universal Time (UTC), UTC +0>

        Dear Customer,

        Your purchase of {self.quantity} * {self.name}(s) is complete!
        Be sure to leave good feedback if you're satisfied!
        
        Thanks,
        Naomi's Electronics
        <==================================================>

        """)

    def __send(self):
        pass

    def send_email(self, smtp_server):
        self.__connect(smtp_server)
        self.__prepare_body()
        self.__send()
