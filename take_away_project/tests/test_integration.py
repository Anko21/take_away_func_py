import pytest
from lib.create_order import *
from lib.menu import *

"""
Given a menu_list
returns the menu_list
"""
def test_see_menu_returns_menu_list():
    menu = Menu()
    menu.add_dish('Carbonara',10)
    create_order= Create_Order()
    assert create_order.see_menu(menu.all_dishes) == {'Carbonara': [10, False]}

"""
Given a menu_list
adds only the dishes that are marked as selected to the order_list,
"""
def test_is_selected_adds_selected_in_order_list():
    menu = Menu()
    menu.add_dish('Carbonara',10)
    menu.mark_selected('Carbonara')
    menu.add_dish('Bolognese',12)
    create_order= Create_Order()
    create_order.is_selected(menu.all_dishes) 
    assert create_order.order_list == [['Carbonara', 10]]

"""
Returns a sum of all prices of the dishes inside order_list
"""
def test_total_price_returns_sum_of_prices():
    menu = Menu()
    menu.add_dish('Carbonara',10)
    menu.mark_selected('Carbonara')
    menu.add_dish('Bolognese',12)
    menu.mark_selected('Bolognese')
    create_order= Create_Order()
    create_order.is_selected(menu.all_dishes) 
    assert create_order.total_price() == 22

'''
returns a lists of all selected dishes with their prices 
and at the end the total price 
'''
def test_order_receipt_returns_itemized_receipts_and_total():
    menu = Menu()
    menu.add_dish('Carbonara',10)
    menu.mark_selected('Carbonara')
    menu.add_dish('Bolognese',12)
    menu.mark_selected('Bolognese')
    create_order= Create_Order()
    create_order.is_selected(menu.all_dishes) 
    assert create_order.order_receipt() ==  'Carbonara : 10£\nBolognese : 12£\nTotal price: 22£'

"""
Given an empty order_list
We return an error
"""
def test_order_receipt_returns_error_with_empty_order_list():
    create_order= Create_Order()
    with pytest.raises(Exception) as e:
        create_order.order_receipt()
    assert  str(e.value) == "You have not selected any dishes yet. Your basket is empty"