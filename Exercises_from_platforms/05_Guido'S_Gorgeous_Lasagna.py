EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_LAYERS = 2


def bake_time_remaining(minutes):
    """
    Returns remaining baking time
    :param minutes: 20
    :return: 20
    """
    return EXPECTED_BAKE_TIME - minutes


def preparation_time_in_minutes(amount_layers):
    """
    Takes numbers of the lasagna's layers to be
    """
    return amount_layers * PREPARATION_TIME_LAYERS


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    This function should return the total number of minutes you've been cooking, or the sum of your preparation time and the time the lasagna has already spent baking in the oven.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


print(elapsed_time_in_minutes(3, 20))
print(preparation_time_in_minutes(2))
print(bake_time_remaining(30))
