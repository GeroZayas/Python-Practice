# Set -> unordered, mutable, no duplicates
my_set = {1, 2, 3, 1, 2}
print(my_set)  # {1, 2, 3} -> because it doesn't allow duplicates

# ----- ANOTHER WAY TO CREATE A SET -----

my_set = set([4, 5, 6])
print(my_set)

# ----- ADD elements to a SET -----
my_set.add(7)
my_set.add(8)
my_set.add(9)

print(my_set)

# ----- REMOVE elements from a SET -----
my_set.remove(7)
print(my_set)

# another way -> discard
my_set.discard(8)
print(my_set)

# ----- EMPTY the SET -----
my_set.clear()
print(my_set)

# ----- ITERATE over the SET -----
my_set.add(7)
my_set.add(8)
my_set.add(9)


for i in my_set:
    print(i)

# ----- CHECK elements in SET -----
if 7 in my_set:
    print("YEAH BABY")

# ----- UNION -> COMBINE elements from two SETS without duplication -----

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

all = odds.union(evens)
print(all)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# INTERSECTION will only elements found in two SETS

intersection_set = odds.intersection(primes)
print(intersection_set)  # {3, 5, 7}

# Difference found in two SETS

diff = all.difference(odds)

print("This is the difference:", diff)

# symmetric difference, takes elements from both sets that are different

sym_diff = odds.symmetric_difference(primes)
print("This is the symmetric difference:", sym_diff)


# ----- UPDATE a SET -----
print("This is primes NOT updated:", primes)

primes.update(evens)

print("This is primes updated with 'evens': ", primes)


# ----- CREATE a FROZEN SET -----
"""Frozen set is just an immutable version of normal set. While elements of a set can be modified at any time, elements of frozen set remains the same after creation"""

a = frozenset([0, 1, 2, 3, 4])

# The following is not allowed:
# a.add(5)
# a.remove(1)
# a.discard(1)
# a.clear()

# Also no update methods are allowed:
# a.update([1,2,3])

print(a)
