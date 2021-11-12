prices = {
    "Banana" : 4,
    "Apple" : 0,
    "Orange" : 1.5,
    "Pear" : 3,
}

stocks = {
    "Banana" : 6,
    "Apple" : 0,
    "Orange" : 1.5,
    "Pear" : 15,
}

groceries = ["Banana","Pear","Orange"]

def compute_bill(food) : 
    total = 0
    for i in food :
        total = total + prices[i]
    return total

a11 = compute_bill(groceries)


def compute_bill(food) :
    total = 0
    for i in food :
        if stocks[i] > 0 :
            total = total + prices[i]
            stocks[i] = stocks[i] - 1
        else :
            pass
    return total

a = compute_bill(groceries)

print(a)
print(stocks)