import os

"""
In this program I created a function that gets a path to a directory and returns a 
list of all files in the given directory which start with the word 'deep'
"""


# This function gets a path to a directory and returns a list of the files that start
# with the word 'deep' in the given directory
def get_deep_files(path):
    my_list = list()
    for x in os.listdir(path):
        if x.startswith("deep"):
            my_list.append(x)

    return my_list


print('\n'.join(get_deep_files("C:\\Users\\Michal\\Downloads\\Notebooks-master\\week05\\images")))