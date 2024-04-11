from lib.create_order import *
from unittest.mock import Mock

'''
Initializing an instance
return an empty list'''

def test_create_order_initialization_returns_empty_list():
    create_order = Create_Order()
    assert create_order.order_list == []

"""
Given a menu_list
returns the menu_list
"""
def test_see_menu_returns_menu_list_mock():
    menu = Mock()
    menu.all_dishes = {'Carbonara': [10, False]}
    create_order= Create_Order()
    assert create_order.see_menu(menu.all_dishes) == {'Carbonara': [10, False]}


"""
Given a menu_list
adds only the dishes that are marked as selected to the order_list,
"""
def test_is_selected_adds_selected_in_order_list_mock():
    menu = Mock()
    menu.all_dishes = {'Carbonara': [10, True], 'Bolognese': [12, False]}
    create_order= Create_Order()
    create_order.is_selected(menu.all_dishes) 
    assert create_order.order_list == [['Carbonara', 10]]

"""
Returns a sum of all prices of the dishes inside order_list
"""
def test_total_price_returns_sum_of_prices_mock():
    menu = Mock()
    menu.all_dishes = {'Carbonara': [10, True], 'Bolognese': [12, True]}
    create_order= Create_Order()
    create_order.is_selected(menu.all_dishes) 
    assert create_order.total_price() == 22

'''
returns a lists of all selected dishes with their prices 
and at the end the total price 
'''
def test_order_receipt_returns_itemized_receipts_and_total_mock():
    menu = Mock()
    menu.all_dishes = {'Carbonara': [10, True], 'Bolognese': [12, True]}
    create_order= Create_Order()
    create_order.is_selected(menu.all_dishes) 
    assert create_order.order_receipt() ==  'Carbonara : 10£\nBolognese : 12£\nTotal price: 22£'