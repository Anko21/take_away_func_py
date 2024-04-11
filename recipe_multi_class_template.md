# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

Use the twilio-python package to implement this next one. You will need to use mocks too.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ Creating_Order(dish):      │
│                            │
│ - menu(list of dishes)     │
│ - select a dish            │
│ - sum price                |
| - itemized_receipt, with   |
|   grand total              │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Menu(dish, price,       |
| selected)               │
│ - list of dishes        │
│ - add dish(name,price)  │
│ - mark dish selected()=>│
│   => selected = true    │
└─────────────────────────┘

```

```python

class Creating_Order:

    def __init__(self):
        # side effect : sets an order_list , with dishes that has been marked as selected
        pass
    
    def see_menu(self, menu_list):
        #Parameters: 
        #   menu_list: a list of dishes
        #returns : a list of dishes

    def is_selected(self, menu_list):
        # Parameters:
        #   menu_list: list of dishes
        #side effects: adds the dishes that has been marked as selected to the order_list
        pass # No code here yet

    def total_price(self):
        # Parameters:
        #   none
        # Returns:
        #   price: number representing a sum of prices inside the order_list
        pass # No code here yet

    def order_receipt(self):
        # Parameters:
        #   none
        # Returns:
        #   A string that lists all selected dishes with their prices and at the end the total price
        pass # No code here yet

class Menu():
    def __init__(self, name, price):
        #side effects: sets a list, for dishes
        pass
    def add_dish(self,name):
        #side effects: adds an dish, to the dishes
    def mark_selected(self):
        #side-effects: sets a dish as selected
        pass

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a menu_list
returns the menu_list
"""
menu = Menu()
menu.add_dish('Carbonara',10)
create_order= Create_Order()
create_order.see_menu(menu) #=> {'Carbonara': [10, False])}

"""
Given a menu_list
adds all the dishes that are marked as selected to the order_list
"""
menu = Menu()
menu.add_dish('Carbonara',10)
menu.mark_selected('Carbonara')
menu.add_dish('Bolognese',12)
create_order= Create_Order()
create_order.is_selected(menu.all_dishes) 
create_order.order_list#=> {'Carbonara': [10, True])}

"""
Returns a sum of all prices of the dishes inside order_list
"""
menu = Menu()
menu.add_dish('Carbonara',10)
menu.mark_selected('Carbonara')
menu.add_dish('Bolognese',12)
menu.mark_selected('Bolognese')
create_order= Create_Order()
create_order.is_selected(menu.all_dishes) 
create_order.total_prices#=> 22

'''
returns a lists of all selected dishes with their prices 
and at the end the total price 
'''
menu = Menu()
menu.add_dish('Carbonara',10)
menu.mark_selected('Carbonara')
menu.add_dish('Bolognese',12)
menu.mark_selected('Bolognese')
create_order= Create_Order()
create_order.is_selected(menu.all_dishes) 
create_order.order_receipt#=> "carb : 10£ bolo : 10£ Total preice: 20£"
"""
Given an empty order_list
We return an error
"""
menu = Menu()
create_order= Create_Order()
create_order.order_receipt# => "You have not selected any dishes yet. Your basket is empty"


## 4. Create Examples as Unit Tests
# lib/menu

'''
Initializing an instance  
returns an empty object
'''
menu = Menu()
menu.all_dishes #=> {}

'''
Given a name and a price
adds a dish to all_dishes
'''
menu = Menu()
menu.add_dish('Carbonara',10)
menu.all_dishes #=> {'Carbonara': [10, False])}

'''
Given a name
marks a dish as selected
'''
menu = Menu()
menu.add_dish('Carbonara',10)
menu.mark_selected('Carbonara')
menu.all_dishes #=> {'Carbonara': [10, True])}

# lib/create_order

'''
Initializing an instance
return an empty list'''
create_order = Create_order()
create_order.order_list #=> []

# MOCK

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
