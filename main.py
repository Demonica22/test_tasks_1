def find_all_paths(x: dict, paths, path="/"):
    if not x:  # empty dirs
        paths.append(path)
    else:
        for key, value in x.items():
            if validate_name(key):  # checking only valid dirs
                if isinstance(value, dict):  # checking nested dirs in current dir
                    if value:
                        find_all_paths(value, paths=paths, path=path + key + "/")
                    else:
                        paths.append(path + key)
                else:  # if only files left in dir, looking for first valid filename
                    values = validate_unique_files(value)
                    if values:
                        paths.append(path + key + "/" + values[0])


def biggestPath(x: dict) -> str:
    paths = ['/']
    find_all_paths(x, paths=paths)
    valid_paths = list(filter(lambda path: len(path) <= 255, paths))  # validating paths with length <= 255
    return max(valid_paths,
               key=lambda elem: len(elem.split("/")))  # looking for longest path by number of dirs included


def validate_unique_files(x: list) -> list:
    if len(x) == len(set(x)):  # only unique names in list
        return list(filter(lambda elem: validate_name(elem), x))
    for elem in set(x.copy()):
        if x.count(elem) > 1:  # deleting all repeating elems
            while elem in x:
                x.remove(elem)
        elif not validate_name(elem):  # validating names of elems
            x.remove(elem)
    return x


def validate_name(name):
    for elem in name:
        # looking for english letters (only lowercase a-z) or nums
        if (elem.isalpha() and not 97 <= ord(elem.lower()) <= 122) or not elem.isalnum():
            return False
    return True


d1 = {'dir1': {}, 'dir2': ['file1'], 'dir3': {'dir4': ['file2'], 'dir5': {'dir6': {'dir7': {}}}}}
d2 = {'dir1': ['file1', 'file1']}
d3 = {'dir1': ['file1', 'file2', 'file2']}
d4 = {'dir1': {}, 'dir2': ['файл2']}
d5 = {'dir1': {'dir2': {'dir3': {'dir4': {'dir5': {'dir6': {'dir7': {'dir8': {'dir9': {'dir10': {'dir11': {'dir12': {
    'dir13': {'dir14': {'dir15': {'dir16': {'dir17': {'dir18': {'dir19': {'dir20': {'dir21': {'dir22': {'dir23': {
        'dir24': {'dir25': {'dir26': {'dir27': {'dir28': {'dir29': {'dir30': {'dir31': {'dir32': {'dir33': {'dir34': {
            'dir35': {'dir36': {'dir37': {'dir38': {'dir39': {'dir40': {'dir41': {
                'dir42': {'dir43': {'dir44': {'dir45': {'dir46': {'dir47': {'dir48': {'dir49': {'dir50': {'dir51': {
                    'dir52': {'dir53': {'dir54': {'dir55': {'dir56': {'dir57': {'dir58': {'dir59': {'dir60': {'dir61': {
                        'dir62': {'dir63': {'dir64': {'dir65': {'dir66': {'dir67': {'dir68': {'dir69': {'dir70': {
                            'dir71': {'dir72': {'dir73': {'dir74': {'dir75': {'dir76': {'dir77': {'dir78': {'dir79': {
                                'dir80': {'dir81': {'dir82': {'dir83': {'dir84': {'dir85': {'dir86': {'dir87': {
                                    'dir88': {'dir89': {'dir90': {'dir91': {'dir92': {'dir93': {'dir94': {'dir95': {
                                        'dir96': {'dir97': {'dir98': {'dir99': {
                                            'dir100': [
                                                "file1"]}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
assert biggestPath(d1) == '/dir3/dir5/dir6/dir7'
assert biggestPath(d2) == '/'
assert biggestPath(d3) == '/dir1/file1'
# invalid filename
assert biggestPath(d4) == '/'
# too long path
assert biggestPath(d5) == '/'
