import re


def color(content, option="match"):
    """
    Change color content to color of option:
        + match pattern
        + line-number match pattern
        + path match pattern
    """
    if option == "match":
        # color same key
        return '\033[30;43m{}\033[0m'.format(content)
    if option == "line":
        # color line find key
        return '\033[1;33m{}\033[0m'.format(content)
    # color of this path file
    return '\033[1;32m{}\033[0m'.format(content)


def show_name_file(path):
    '''
    check is show path_file or not
    '''
    print("%s" % color(path, "path"))
    return False


def high_light(pattern, content, option):
    """
    Will find pattern every pattern in content ignore upper or lower
    and highlight that pattern in content
    """
    patterns = re.findall(pattern, content, re.IGNORECASE)
    for pattern in set(patterns):
        content = content.replace(pattern, color(pattern))
    return content if len(patterns) > 0 else None


