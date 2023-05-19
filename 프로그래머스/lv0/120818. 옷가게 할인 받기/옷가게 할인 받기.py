import math
def solution(price):
    if price >= 500000:
        price = price*(80/100)
    elif price >= 300000:
        price = price*(90/100)
    elif price >= 100000:
        price = price*(95/100)
    return math.trunc(price)