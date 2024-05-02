# This program is written to calculate the total stock value of a cafe

# This program use the items in menu as keys to get the item's number and price
# from the stock and price dictionaries

# The results are printed out in the end


menu = ["coffee", "tea", "snack", "mug"]

stock = {
    "coffee": 30000,
    "tea": 15000,
    "snack": 5000,
    "mug": 1000,
    # units
}

price = {
    "coffee": 3,
    "tea": 2,
    "snack": 4,
    "mug": 15,
    # pound per unit
}

total_stock = 0
for item in menu:
    item_value = stock[item] * price[item]
    print("The value of {} is {} pounds.".format(item, item_value))
    total_stock += item_value
print("\nThe total stock of the cafe is {} pounds.".format(total_stock))
