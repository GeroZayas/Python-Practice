def eat_ghost(power_pellet_active, touching_ghoust):
    return power_pellet_active and touching_ghoust


def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    return power_pellet_active == False and touching_ghost


def win(all_dots_eaten, power_pellet_active, touching_ghost):
    if all_dots_eaten and power_pellet_active and not touching_ghost:
        return True
    elif all_dots_eaten and not touching_ghost:
        return True
    elif all_dots_eaten and power_pellet_active and touching_ghost:
        return True
    else:
        return False


# print(eat_ghost(True, True))
# print(score(False, True))
# print(lose(False, True))
print(win(True, False, True))
