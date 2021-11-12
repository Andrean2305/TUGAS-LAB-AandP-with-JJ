prices = {
    "Banana" : 4,
    "Apple" : 0,
    "Orange" : 1.5,
    "Pear" : 3,
}

stocks = {
    "Banana" : 6,
    "Apple" : 0,
    "Orange" : 32,
    "Pear" : 15,
}

for a,b in prices.items() :
    print(a)
    print(f"Price: {b}") 
    print(f"Stocks: {stocks[a]}\n")

total = 0
for a,b in prices.items() : 
    print(f"{a}: {(b * stocks[a])}")
    total = total + (b * stocks[a])

print(f"\nTotal: {total}") #to make it int just do int(total)
