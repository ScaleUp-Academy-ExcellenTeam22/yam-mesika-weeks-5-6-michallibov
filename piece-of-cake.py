"""
In this program I created a function that gets a dictionary of an ingredient and it's price,
an optional list of items that we can ignore and the amount of each ingredient we must buy.
The program will calculate the sum of all the prices of the needed ingredients based on their
amount and price and will return the price of everything.
"""


# This function gets ingredients, their prices, optional ingredients and how much of them
# we need, and calculates the total price of the ingredients we must buy.
def get_recipe_price(prices, optionals=[], **ingredients):
    """
    :param prices: a dictionary of the names and prices of an ingredient
    :param optionals: a list of optional ingredients we don't have to buy
    :param ingredients: the amount of each ingredient we need
    :return: the total price we will have to pay
    """
    total_price = 0
    for ingredient in ingredients:
        if ingredient not in optionals:     # if we must buy this ingredient (doesn't appear in optional)
            total_price += prices.get(ingredient) * ingredients.get(ingredient) // 100
    return total_price


print(get_recipe_price({'chocolate': 18, 'milk': 8}, milk=100, chocolate=200))