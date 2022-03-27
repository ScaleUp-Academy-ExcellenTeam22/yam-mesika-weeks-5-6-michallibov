"""
In this program I rewrote the known function 'join' for lists. This function gets
lists and joins them together to one list with a separator. The user can choose a
seperator between each joined list or no. If the user chooses not to add a separator-
the default separator is going to be '-'
"""


def join(*lists, sep='-'):
    """
    This function gets a certain amount of lists and joins them into one
    list where each list we got is separated by a character the user chose.
    if there's no separator- the default separator is going to be '-'.
    :param lists: the lists we got from the main to join
    :param sep: the char that will separate each list
    :return: the joined list of all lists the function received
    """

    # The list we got is empty (no list was sent)
    if not lists:
        raise Exception("No list was found to join")

    new_list = [item for sublist in zip(lists, sep * len(lists)) for item in sublist]
    new_list.pop()

    return new_list


if __name__ == '__main__':
    print(join([1], [1, 2], [4]))
