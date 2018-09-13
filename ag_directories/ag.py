from os import getcwd
from os.path import isfile
from get_input import find_pattern_path, check_option
from colect_open_files import open_file, colect_files_subdirectory



if __name__ == "__main__":
    list_option = check_option()
    pattern, path = find_pattern_path()
    '''
    what options is use
    '''
    option = '--case-sensitive' if '--case-sensitive' in list_option else None
    if path != getcwd and isfile(path):
        ''' path is file '''
        open_file(path, pattern, option)
    else:
        files = colect_files_subdirectory(path, list_option)
        for file in files:
            if open_file(file, pattern, option) == False:
                print("")
