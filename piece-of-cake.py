import functools


def get_recipe_price(prices, optionals=[], **ingredients):
    """
    This function gets ingredients, their prices, optional ingredients and how much of them
    we need, and calculates the total price of the ingredients we must buy.
    :param prices: a dictionary of the names and prices of an ingredient
    :param optionals: a list of optional ingredients we don't have to buy
    :param ingredients: the amount of each ingredient we need
    :return: the total price we will have to pay
    """

    # Sums up the total price of all ingredients we must buy using a lambda function.
    total_price = functools.reduce(lambda price, ingredient: price + ingredients.get(ingredient) *
                                    prices.get(ingredient)//100 if ingredient not in optionals else price, prices, 0)

    return total_price


if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, milk=100, chocolate=200))
