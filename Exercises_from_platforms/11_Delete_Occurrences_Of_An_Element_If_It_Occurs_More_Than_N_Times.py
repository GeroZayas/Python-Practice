"""Enough is enough! Alice and Bob were on a holiday. Both of them took many pictures of the places they've been,
and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions,
since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. He tells them that he will only
sit during the session if they show the same motive at most N times. Luckily, Alice and Bob are able to encode the
motive as a number. Can you help them to remove numbers such that their list contains each number only up to N times,
without changing the order?

Task Given a list lst and a number N, create a new list that contains each number of lst at most N times without
reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,
2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

Example
  delete_nth ([1,1,1,1],2) # return [1,1]

  delete_nth ([20,37,20,21],1) # return [20,37,21]
"""


def delete_nth(order: list, max_e: int) -> list:
    # We create the list which will be returned
    new_list = []
    # For loop to go element by element in order list
    for num in order:
        # We count how many times the element is in our new list
        # With the limit of max_e, taken as argument
        # While the amount of times the elements appears in our new list
        # is less or equal than our limit, we keep appending it to our new list
        # The KEY here is using the COUNT method from lists
        if new_list.count(num) < max_e:
            new_list.append(num)
    return new_list


print(delete_nth([1, 1, 1, 1], 2))  # return [1,1]
print(delete_nth([20, 37, 20, 21], 1))  # return [20,37,21]
