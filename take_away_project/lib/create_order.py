class Create_Order:

    def __init__(self):
        self.order_list = []
    
    def see_menu(self, menu_list):
        return menu_list

    def is_selected(self, menu_list):
        for key,value in menu_list.items():
            if value[1] == True:
                self.order_list.append([key,value[0]])

    def total_price(self):
        all_prices = [price[1] for price in self.order_list] 
        return sum(all_prices)

    def order_receipt(self):
        if not self.order_list:
            raise Exception("You have not selected any dishes yet. Your basket is empty")
        itemized_receipt = "\n".join(list(map(lambda dish : f'{dish[0]} : {dish[1]}£' , self.order_list)))
        total = self.total_price()
        return f'{itemized_receipt}\nTotal price: {total}£'
    
# dish = Dish()
# dish.add_dish("carb", 10)
# dish.add_dish("bolo", 10)
# dish.mark_selected("carb")
# dish.mark_selected("bolo")
# # print(dish.dish_details)
# # print(menu.menu_list)
# create = Creating_Order()
# # print(create.see_menu(dish.dish_details))
# create.is_selected(dish.dish_details)
# # print(create.order_list)
# # print(create.total_price())
# print(create.order_receipt())