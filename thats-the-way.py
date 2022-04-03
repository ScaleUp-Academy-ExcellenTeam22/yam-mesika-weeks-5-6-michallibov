import os

"""
In this program I created a function that gets a path to a directory and returns a 
list of all files in the given directory which start with the word 'deep'
"""


def get_deep_files(path):
    """
    This function gets a path to a directory and returns a list of the files that start
    with the word 'deep' in the given directory.
    :param path: a path to the directory we would like to check
    :return: a list of names of the files that start with the word 'deep'
    """
    files_start_with_deep_list = [file_name for file_name in os.listdir(path) if file_name.startswith("deep")]

    return files_start_with_deep_list


if __name__ == '__main__':
    print('\n'.join(get_deep_files("C:\\Users\\Michal\\Downloads\\Notebooks-master\\week05\\images")))
