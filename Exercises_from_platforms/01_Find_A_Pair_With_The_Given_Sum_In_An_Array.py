# Find a pair with the given sum in an array
nums = [8, 7, 2, 5, 3, 1]
target = 10


def find_pair_for_sum(array, target):
    pair = []
    # For loop that takes first num in array and checks if
    # there is another number with which, if added together,
    # they yield target (example, if target = 10, and
    # first number = 8, the loop looks if there's a 2 in the array

    for n in array:
        second_num = target - n
        if second_num in array and second_num != n:
            # I also make sure that they don't repeat
            if n not in pair and second_num not in pair:
                # I add them to a list name pair[]
                pair.append(n)
                pair.append(second_num)

    # if there are no pairs:
    if len(pair) == 0:
        print("Pair  not found")

    # if there are pairs:
    elif len(pair) > 0:
        # I set this counter so I can use it as index points to print the
        # pairs that yield the target sum
        counter = 0
        for e in pair:
            # I set it counter < len(pair) so it does not yield a out of
            # index error
            while counter < len(pair):
                print("Pair found ", f"({pair[counter]}, {pair[counter+1]})")
                counter += 2  # to move two indexes and print the next pair
                if counter < len(
                    pair
                ):  # so at the end it doesn't print another "or" after the
                    # last pair
                    print("or")


find_pair_for_sum(nums, target)
