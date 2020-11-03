from typing import List, Tuple
price = float
rate = float

def discount(p: price, r: rate):
    return (1 - float(r/100)) * p

def modified_discount(p: price, *rates: List[rate]):
    reduced_price = p
    for rate in rates:
        reduced_price = discount(reduced_price, rate)
    return reduced_price

def discount_formula(p: price, *rates: Tuple[rate]):
    prod = 1
    for rate in rates:
        prod = prod * (100 - rate)
    return p / (100 ** len(rates)) * prod

price = 79.5

# print(discount_formula(price, 25, 10))
# print(discount(price, 35))
print(discount_formula(price, 25, 35))
print(modified_discount(price, 25, 35))