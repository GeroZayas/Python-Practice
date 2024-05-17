"""
A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.

He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

His mother looks out of a window 1.5 meters from the ground.

How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

Note:
The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

Examples:
- h = 3, bounce = 0.66, window = 1.5, result is 3

- h = 3, bounce = 1, window = 1.5, result is -1

(Condition 2) not fulfilled).
"""


def bouncing_ball(h, bounce, window):
    # We declare a var bouncing_times and set it to 0
    # We will add to it how many times the ball passes in front of the
    # mother's window, which is what we want to determine here
    bouncing_times = 0
    # Now we determine how high will the ball bounce the first time
    height_bounce = h * bounce
    # With the IF we check that all conditions are met
    # before moving forward with the calculation
    if h > 0 and 0 < bounce < 1 and window < h:
        # With the WHILE LOOP we make sure that the other condition is met:
        # The ball can only be seen if the height of the rebounding ball is
        # strictly greater than the window parameter.
        while height_bounce > window:
            # we add 1 time for every time is bounces in front of Mom's
            # window
            bouncing_times += 1
            # And we reduce the height of the bouncing every time
            # making sure the while loops becomes false at one point
            height_bounce *= bounce
        # we return bouncing times * 2, as we count every time it's
        # falling (passes in front of mom's window)
        # and we add one more time (+1) accounting for the first time it
        # falls
        return bouncing_times * 2 + 1
    return -1


print(bouncing_ball(2, 0.5, 1))  # 1
print(bouncing_ball(3, 0.66, 1.5))  # 3
print(bouncing_ball(30, 0.66, 1.5))  # 15
print(bouncing_ball(30, 0.75, 1.5))  # 21
