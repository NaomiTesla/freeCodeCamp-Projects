# Naomi Tesla
# Python OOP Refresher from freeCodeCamp C:
# https://www.youtube.com/watch?v=Ej_02ICOIgs

from item import Item
from phone import Phone
from keyboard import Keyboard

Item.instantiate_from_csv()

phone1 = Phone("iPhone", 750, 1, 0)
phone1.name = "iPhone [SPACE GREY] [CLEAN IMEI]"

phone1.apply_increment(0.2)
phone1.apply_discount()
phone1.send_email('127.0.0.1:465')


item1 = Keyboard('Razer Black Widow Tournament Edition', 200, 1)
item1.apply_discount()