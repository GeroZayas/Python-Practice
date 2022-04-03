def beeramid(bonus, price):
    levels = 0
    beers = int(bonus // price)
    print("beers", beers)
    if beers == 4:
        levels = 1
    elif beers > 4:
        while beers > 0:
            levels += 1
            beers -= levels**2
            # print("levels", levels)
    return levels


print(beeramid(9, 2))  # 1
print(beeramid(21, 1.5))  # 3
print(beeramid(-1, 4))  # 0
