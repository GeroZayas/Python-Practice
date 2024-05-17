# 100 doors
# from https://rosettacode.org/wiki/100_doors

for i in range(1, 101):
    if i**0.5 % 1:
        door_state = "closed"
    else:
        door_state = "open"
    print("Door {}:{}".format(i, door_state))
