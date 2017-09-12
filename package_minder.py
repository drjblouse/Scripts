! /usr/bin/python
""" This module compares package lists and find the differences. """
PACKAGE_FROM_SERVER_PATH = 'pr_packages.txt'
PACKAGE_TO_SERVER_PATH = 'build_packages.txt'
PACKAGE_NEW_FILE_PATH = 'package_install.txt'
GEM_FROM_SERVER_PATH = 'pr_gems.txt'
GEM_TO_SERVER_PATH = 'build_gems.txt'
GEM_NEW_FILE_PATH = 'gem_install.txt'
PIP_FROM_SERVER_PATH = 'pr_pip.txt'
PIP_TO_SERVER_PATH = 'build_pip.txt'
PIP_NEW_FILE_PATH = 'pip_install.txt'


def get_package_list():
    """ Get the list of all packages not on server2 or out of date. """
    from_list, to_list = get_lists_from_files(
        PACKAGE_FROM_SERVER_PATH, PACKAGE_TO_SERVER_PATH)
    to_dict = get_package_dictionary(to_list)
    from_dict = get_package_dictionary(from_list)
    updates = get_updates(from_dict, to_dict)
    write_package_list_to_file(updates)


def write_package_list_to_file(updates):
    """ Take the update dictionary and write it to the output file.
    :param updates: The update package list as a dictionary.
    """
    with open(PACKAGE_NEW_FILE_PATH, 'w') as new_file:
        for item, version in updates.iteritems():
            new_file.write(item + '=' + version + '\n')


def get_lists_from_files(from_path, to_path):
    """ Get the package lists for both servers.
    :param from_path: The path from the first server.
    :param to_path: The path from the second server.
    """
    to_file = open(to_path)
    from_file = open(from_path)
    to_list = to_file.readlines()
    from_list = from_file.readlines()
    to_file.close()
    from_file.close()
    return from_list, to_list


def get_updates(from_dict, to_dict):
    """ Get the dictionary of updates that are needed.
    :param to_dict: The to dictionary
    :param from_dict: The from dictionary
    """
    updates = dict()
    for name, version in to_dict.iteritems():
        if not from_dict.has_key(name):
            updates[name] = version
    return updates


def get_package_dictionary(pkg_list):
    """ Convert the package list to a dictionary.
    :param pkg_list: The list of packages.
    """
    packages = dict()
    for item in pkg_list:
        if len(item.split()) < 4:
            continue
        if item.split()[1].startswith('Name'):
            continue
        name, version = item.split()[1], item.split()[2]
        packages[name] = version
    return packages


def get_gem_dictionary(gem_list):
    """ Convert the gem list to a dictionary.
    :param gem_list: The list of gems.
    """
    gems = dict()
    for item in gem_list:
        if len(item.split()) < 2:
            continue
        name, version = item.split()[0], item.split()[1]
        gems[name] = version
    return gems


def get_pip_dictionary(pip_list):
    """ Convert the pip list to a dictionary.
    :param pip_list: The list of pip dependencies.
    """
    pips = dict()
    for item in pip_list:
        if len(item.split('==')) < 2:
            continue
        name, version = item.split('==')[0], item.split('==')[1]
        pips[name] = version
    return pips


def write_gem_updates_to_file(updates):
    """ Write the gem install file for updates.
    :param updates: Updates in a dictionary.
    """
    with open(GEM_NEW_FILE_PATH, 'w') as new_file:
        for item, version in updates.iteritems():
            new_file.write(
                'gem install ' + item +
                ' --version=' +
                version.lstrip('(').rstrip(')').rstrip(',') + '\n')


def generate_gem_update_script():
    """ Generate an update script based on gem list format. """
    from_list, to_list = get_lists_from_files(
        GEM_FROM_SERVER_PATH, GEM_TO_SERVER_PATH)
    to_dict = get_gem_dictionary(to_list)
    from_dict = get_gem_dictionary(from_list)
    updates = get_updates(from_dict, to_dict)
    write_gem_updates_to_file(updates)


def write_pip_updates_to_file(updates):
    """ Take the update dictionary and write it to the output file.
    :param updates: The update package list as a dictionary.
    """
    with open(PIP_NEW_FILE_PATH, 'w') as new_file:
        for item, version in updates.iteritems():
            new_file.write(item + '==' + version)


def generate_pip_update_script():
    """ Generate an update script based on pip list format. """
    from_list, to_list = get_lists_from_files(
        PIP_FROM_SERVER_PATH, PIP_TO_SERVER_PATH)
    to_dict = get_pip_dictionary(to_list)
    from_dict = get_pip_dictionary(from_list)
    updates = get_updates(from_dict, to_dict)
    write_pip_updates_to_file(updates)


if __name__ == "__main__":
    get_package_list()
    generate_gem_update_script()
    generate_pip_update_script()
