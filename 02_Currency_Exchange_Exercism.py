# https://exercism.org/tracks/python/exercises/currency-exchange

def exchange_money(budget, exchange_rate):
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    return round(denomination * number_of_bills)


def get_number_of_bills(budget, denomination):
    return round(budget // denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_rate = exchange_rate * spread / 100
    money = budget / (exchange_rate + spread_rate)
    # print(money)
    bills = get_number_of_bills(money, denomination)
    # print(bills)
    total_money = get_value_of_bills(denomination, bills)
    return total_money


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    spread_rate = exchange_rate * spread / 100
    print('spread rate: ', spread_rate)
    money = budget / (exchange_rate + spread_rate)
    print('money: ', money)
    bills = get_number_of_bills(money, denomination)
    print('bills: ', bills)
    total_money = get_value_of_bills(denomination, bills)
    print('total: ', total_money)
    money_lost_in_exchange = int(money - total_money)
    return money_lost_in_exchange


print(non_exchangeable_value(1500, 0.84, 25, 40))
