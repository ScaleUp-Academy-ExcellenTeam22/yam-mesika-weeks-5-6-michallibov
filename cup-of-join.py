"""
In this program I rewrote the known function 'join' for lists. This function gets
lists and joins them together to one list with a separator. The user can choose a
seperator between each joined list or no. If the user chooses not to add a separator-
the default separator is going to be '-'
"""


# This function gets a certain amount of lists and joins them into one
# list where each list we got is separated by a character the user chose.
# if there's no separator- the default separator is going to be '-'.
def join(*lists, sep='-'):
    if not lists:   # the list we got is empty (no list was sent)
        return None

    new_list = list()
    for x in lists:
        new_list.extend(x)      # adds the given list to the output list without []
        new_list.append(sep)

    new_list.pop()  # remove the last separator
    return new_list


print(join([1]))