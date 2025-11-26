stock = {
    "Laptop": 14,
    "Phone": 7,
    "Earbuds": 22,
    "Adapter": 6,
    "Keyboard": 11
}
print("Starting inventory:", stock)

stock["Monitor"] = 18
stock["Phone"] = 9
print("\nInventory after adjustments:", stock)

def get_low_stock(items):
    return {name: qty for name, qty in items.items() if qty < 10}

print("\nItems with low stock:", get_low_stock(stock))

del stock["Adapter"]
print("\nInventory after removing Adapter:", stock)

print("\nAvailable products:")
for item, quantity in stock.items():
    print(item, ":", quantity)
