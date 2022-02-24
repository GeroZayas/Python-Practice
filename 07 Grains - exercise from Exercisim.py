def square(number):
    """
    Returns an integer representing the amount of grains in the particular square we received as input
    """
    # We make sure the argument is between 1 and 64 -> Else we raise an error
    if 1 <= number <= 64:
        result = 1
        # In case we are in the first square, we just return 1 grain
        if number == 1:
            return result
        else:
            # while we go up in squares, the amount doubles each time
            for sq in range(1, number):
                result = result * 2
            return result
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    total_amount = 0
    for sq  in range(1, (64+1)):
        total_amount += square(sq)
    return total_amount


# we do this format here to be able to read the number better
print("{:,}".format(square(2)))
print("\nThe total amount of grains would be: ")
print("{:,}".format(total()))
#print("{:,}".format(18446744073709551615))
