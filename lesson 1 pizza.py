#most basic of doodles, was assignment, didn't even know classes exist. seemed good for the time. Now is ew.


toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
print(""" 
base toppings:""")
print(toppings)

prices = [2, 6, 1, 3, 2, 7, 2]
print("""
base prices:""")
print(prices)
print("""
""")
num_pizzas = len(toppings)
print("We sell " +str(num_pizzas)+ " different kinds of pizza!")
print("""
menu style list of pizza:""")
menu_pizza = zip(toppings, prices)
print(list(menu_pizza))

print("""
zipped data, price first, unsorted:""")
pizzas = list(zip(prices, toppings))
print(pizzas)
pizzay = sorted(pizzas)
print("""
sorted by price""")
print(pizzay)
print("""
cheapest recommended pizza topping:""")
cheapest_pizza = pizzay[0]
print("" +str(cheapest_pizza)[1:-1] +"")
print("""
pizza for the man of the discerning taste:""")
priciest_pizza = pizzay[-1]
print("" +str(priciest_pizza)[1:-1] +"")
three_cheapest= pizzay[0:3]
print("""
pizza 4 da miceskies:""")
print("" +str(three_cheapest)+"")

print("""

""")
num_two_dollar_slices = prices.count(2)
print("number of two dollar slices: "+str(num_two_dollar_slices)+ " ")
