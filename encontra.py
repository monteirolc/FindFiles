import os


def formated_size(size):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5
    if size < kilo:
        size = base
        text = 'B'
    elif size < mega:
        size /= kilo
        text = 'KB'
    elif size < giga:
        size /= mega
        text = 'MB'
    elif size < tera:
        size /= giga
        text = 'GB'
    elif size < peta:
        size /= tera
        text = 'TB'
    else:
        size /= peta
        text = 'PB'
    size = round(size, 2)
    return f'{size} {text}'.replace('.', ',')


def find_files(find_path='', find_expression='', count=0):
    for root, directory, files in os.walk(find_path):
        for file in files:
            if find_expression in file:
                try:
                    count += 1
                    full_path = os.path.join(root, file)
                    file_name, ext_file = os.path.splitext(file)
                    size = os.path.getsize(full_path)
                    size_correted = formated_size(size)
                    print()
                    print("I find your file: ", file)
                    print("Name: ", file_name)
                    print("Path: ", full_path)
                    print("Extension: ", ext_file)
                    print(f"Size: {size_correted} ({size} B)")
                except PermissionError as e:
                    print('No permission')
                except FileNotFoundError as e:
                    print('File not found')
                except Exception as e:
                    print('Unknown error')
    print()
    print(f'Finded results {count}')
