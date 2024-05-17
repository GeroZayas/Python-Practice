"""
Mount the Bowling Pins!
Task:
Did you ever play Bowling? Short: You have to throw a bowl into 10 Pins arranged like this:


I I I I  # each Pin has a Number:    7 8 9 10
 I I I                                4 5 6
  I I                                  2 3
   I                                    1

You will get an Array with Numbers, e.g.: [3,5,9] and remove them from the field like this:


I I   I
 I   I
  I
   I

Return a string with the current field.

Note that:
You begin a new line with \n
Each Line must be 7 chars long
Fill the missing pins with a whitespace
"""

print("-" * 20 + " GERO'S " + "-" * 20)
# ----------------------- MY SOLUTION (GERO ZAYAS MARCH 2022) -----------------------


def bowling_pins(arr):
    # create rows
    # substitute 10 by x, so it only takes one char
    row1 = "7 8 9 x"
    row2 = " 4 5 6 "
    row3 = "  2 3  "
    row4 = "   1   "

    # replace numbers in arr with ' ' space
    for i in range(len(arr)):
        if str(arr[i]) == "10":
            arr[i] = "x"
        row1 = row1.replace(str(arr[i]), " ")
        row2 = row2.replace(str(arr[i]), " ")
        row3 = row3.replace(str(arr[i]), " ")
        row4 = row4.replace(str(arr[i]), " ")

    def make_pins(a_string: str) -> str:
        final_string = ""
        for ele in a_string:
            if ele.isalnum():
                final_string += "I"

            else:
                final_string += ele
        return final_string

    row1 = make_pins(row1)
    row2 = make_pins(row2)
    row3 = make_pins(row3)
    row4 = make_pins(row4)

    # put them together with \n and .join()
    return "\n".join([row1, row2, row3, row4])


print(bowling_pins([1, 2, 10]))
print(bowling_pins([3, 5, 9]))

# ----------------------- BEST PRACTICES (SOLUTIONS ON CODEWARS) -----------------------
print("-" * 20 + " CODEWARS' " + "-" * 20)


pins = "{7} {8} {9} {10}\n" + " {4} {5} {6} \n" + "  {2} {3}  \n" + "   {1}   "


"""
Notice the * operator in the function call. It is used to unpack the list.
It has nothing to do with format. * unpacks the arguments so if there are, say 4 placeholders and 4 elements in your list, then format unpacks the args and fills the slots.
"""


def bowling_pins(arr):
    return pins.format(*(" " if i in arr else "I" for i in range(11)))


print(bowling_pins([1, 2, 10]))
print(bowling_pins([3, 5, 9]))
