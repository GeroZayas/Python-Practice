"""
5 kyu
Pete, the baker CODEWARS

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2

cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})

# must return 0

cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""


def cakes(recipe: dict, available: dict) -> int:
    # Declare var that we raturn -> int meaning amount
    # of cakes possible
    amount_of_cakes = 0
    # Declare var list result that will take on how
    # many times we can make a cake relative to a specific ingredient
    result = []
    # Declare var boolean have_all_ingredients and it starts being False
    have_all_ingredients = False

    # Declare var counter to count ingredients in recipe
    # then we check that we have all of those ingredients
    #  in the available dictionary
    counter = 0
    for ingredient in recipe.keys():
        if ingredient in available.keys():
            counter += 1
    # if the len of recipe is equal to number of ingredients
    # found in available, then it means we have all we need
    # So we turn have_all_ingredients to True
    if counter == len(recipe):
        have_all_ingredients = True

    # If we have all of the ingredients then we can proceed
    if have_all_ingredients == True:
        for ingredient in recipe.keys():
            # we do whole number division with //
            # for each ingredient we have available
            amount_of_cakes = available[ingredient] // recipe[ingredient]
            # We append it to our result list
            result.append(amount_of_cakes)
        # Logically, we select the min number of times
        # we can make a cake relative to one ingredient
        # That would our return
        amount_of_cakes = min(result)
    return amount_of_cakes


print(
    cakes(
        {"flour": 500, "sugar": 200, "eggs": 1},
        {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200},
    )
)  # must return 2

print("---------------------")

print(
    cakes(
        {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
        {"sugar": 500, "flour": 2000, "milk": 2000},
    )
)  # must return 0

print("---------------------")

print(
    cakes(
        {"crumbles": 18, "flour": 43, "cocoa": 23},
        {
            "crumbles": 7352,
            "apples": 9262,
            "butter": 3170,
            "cream": 2142,
            "cocoa": 8918,
            "nuts": 5152,
            "eggs": 3801,
            "oil": 2215,
            "sugar": 9682,
            "pears": 5201,
        },
    )
)  # must return 0
