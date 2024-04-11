class Menu:
    
    def __init__(self):
        self.all_dishes={}

    def add_dish(self, name, price):
        self.all_dishes[name] = [ price , False ]

    
    def mark_selected(self,name):
        self.all_dishes[name][1] = True

menu = Menu()
menu.add_dish("carb", 10)
menu.add_dish("bolo", 10)
menu.add_dish("bdolo", 10)
menu.add_dish("bodlo", 10)
menu.add_dish("bodlo", 10)
menu.mark_selected("carb")
print(menu.all_dishes)