from sys import argv
from os import getcwd

def check_option(options=argv[1:]):
    """
    Find option input find pattern
        + find only pattern : --case-sensitive
        + find all files include hidden files: --hidden
    Return list option and positon of option in sys.argv
    """
    list_option = []
    for option in options:
        if option == "--case-sensitive":
            list_option.append(option)
        if option == "--hidden":
            list_option.append(option)
    return list_option


def find_pattern_path(path=getcwd()):
    """
    return pattern, path if path is None return os.getcwd()
    """
    index_pattern, pattern = find_pattern()
    for index, item in enumerate(argv[1:]):
        if (item != "--case-sensitive"
           and item != "--hidden" and
           index != index_pattern):
            path = item  
    return [pattern, path]

def find_pattern():
    '''
    This return 2 thing:
        + Index of pattern find
        + Pattern input
    '''
    for index, item in enumerate(argv[1:]):
        if item != "--case-sensitive" and item != "--hidden":
            return index, item
    