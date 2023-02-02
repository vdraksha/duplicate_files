from pathlib import Path
from hashlib import md5


def list_files(path: str, filetype: str):
    return list(Path(path).rglob(filetype))


def checksum(path: str, filetype: str):
    lt = list_files(path, filetype)
    dt = dict()
    for file in lt:
        md5hash = md5(open(file, 'rb').read()).hexdigest()
        if md5hash not in dt:
            dt[md5hash] = [file]
        else:
            dt[md5hash].append(file)
    return dt


def print_duplicates(dt: dict()):
    for key in dt:
        if len(dt[key]) > 1:
            print(dt[key])
    return 0


def remove_duplicate(dt):
    for key in dt:
        if len(dt[key]) > 1:
            for i in range(1, len(dt[key])):
                f = Path(dt[key][i])
                f.unlink()
    return 0


if __name__ == '__main__':
    d = checksum('path', '*.(filetype or *)')
    print_duplicates(d)
    #remove_duplicate(d)
