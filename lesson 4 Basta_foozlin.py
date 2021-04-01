
early_items  = {
    'salumeria plate': 8.00,
    'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00,
    'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 1.50,
    'espresso': 3.00
}
brunch_items = {
    'pancakes': 7.50,
    'waffles': 9.00,
    'burger': 11.00,
    'home fries': 4.50,
    'coffee': 1.50,
    'espresso': 3.00,
    'tea': 1.00,
    'mimosa': 10.50,
    'orange juice': 3.50
}
dinner_items = {
    'crostini with eggplant caponata': 13.00,
    'ceaser salad': 16.00,
    'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50,
    'coffee': 2.00,
    'espresso': 3.00
}
kids_items   = {
    'chicken nuggets': 6.50,
    'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}
arepas_items ={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

class Business:
    def __init__(self, name, franchises):
        self.franchises = franchises
        self.name = name
    

class Franchise:
    def __init__(self, address, menus, name):
        self.address = address
        self.menus = menus
        self.name = name
    def __repr__(self):
        return ("{} is in {}".format(a=self.address))

    def available_menus(self, time):
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)
        return available_menu


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return (''' \n\n{name} menu serving from {start_time} to {end_time}:

             {items}'''.format(name=self.name, items=self.items, start_time=self.start_time, end_time=self.end_time))
    
    def calculate_bill(self, purchased_items):
        self.total = 0
        for item in purchased_items:
            self.total += self.items.get(item, 0)
        return self.total

#menu creation, menus items at top:
brunch_menu = Menu('Brunch',       brunch_items,     1100, 1600)
earlyb_menu = Menu('Early Bird',   early_items,      1500, 1800)
dinner_menu = Menu('Dinnah',       dinner_items,     1700, 2300)
childr_menu = Menu('kids',         kids_items,       1100, 2100)
arepas_menu = Menu('Arepa',        arepas_items,     1000, 2000 )
#compiled list:
menus       = [brunch_menu, earlyb_menu, dinner_menu, childr_menu, arepas_menu]

#franchise creation and store indexing:
flagship_store  = Franchise("1232 West End Road",       menus,   'og'      )
new_installment = Franchise("12 East Mulberry Street",  menus,   'newmoney')
arepas_franchise= Franchise("189 Fitzgerald Avenue",    menus,   'arepas'  )
#compiled list:
franchises      = [flagship_store, new_installment, arepas_franchise]

#business creation and indexing:
basta_fazoolin = Business("Take a'Arepa", franchises)


#testing 1-2-3
brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee'           ])
earlyb_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
# print(flagship_store.available_menus(1700))
# print(flagship_store.available_menus(1200))
# print(flagship_store.menus)






