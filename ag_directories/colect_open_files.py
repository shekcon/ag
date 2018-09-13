from os.path import isfile
from os import walk
# import glob
from search_pattern import color, high_light, show_name_file

def open_file(file_search, pattern, option, flag=True):
    """
    Open file and search pattern
    Show line number with content in line match pattern
    """
    # open file
    try:
        if isfile(file_search):
            with open(file_search, "r", encoding="utf-8", errors="ignore") as file:
                # find key in each line
                for index, content in enumerate(file):
                    # check option find key
                    result = high_light(pattern, content, option)
                    if result is not None:
                        flag = show_name_file(file_search) if flag else False
                        print("%s:%s" % (
                            color(index+1, "line"),
                            high_light(pattern, content, option)),
                            end='')
        return flag               
    except BaseException:
        return flag


def colect_files_subdirectory(pwd, options):
    '''
    find all hidden files and non-hidden files in sub directory amd current dir
    '''
    option = '--hidden' if '--hidden' in options else None
    list_dir_files = []
    # find with nested tuple inside with index 0 is directory
    # index 2 is file in that directory
    for item in walk(pwd):
        list_dir_files.append(item)
    # get all file directory + "/" + filename
    list_files = []
    for item in list_dir_files:
        for file in item[2]:
            path_file = item[0] + "/" + file
            if option == '--hidden':
                list_files.append(path_file)
            elif '/.' not in path_file and '\\.' not in path_file:
                list_files.append(path_file)
    return list_files

# def find_files_subdirectory(pwd=os.getcwd()):
#     '''
#     find all file in sub directory and current directory
#     '''
#     list_files = []
#     for filename in glob.glob(pwd + "/**/*", recursive=True):
#         if os.path.isfile(filename):
#             list_files.append(filename)
#     return list_files
