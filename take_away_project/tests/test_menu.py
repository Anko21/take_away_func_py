from lib.menu import *
from unittest.mock import Mock

'''
Initializing an instance  
returns an empty object
'''
def test_menu_check_initialization_returns_empty_object():
    menu = Menu()
    assert menu.all_dishes == {}

'''
Given a name and a price
adds a dish to all_dishes
'''
def test_add_dish_to_all_dishes():
    menu = Menu()
    menu.add_dish('Carbonara',10)
    assert menu.all_dishes == {'Carbonara': [10, False]}

'''
Given a name
marks a dish as selected
'''
def test_mark_selected_returns_true():
    menu = Menu()
    menu.add_dish('Carbonara',10)
    menu.mark_selected('Carbonara')
    assert menu.all_dishes == {'Carbonara': [10, True]}