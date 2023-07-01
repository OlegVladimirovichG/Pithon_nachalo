import os

def split_filepath(filepath):
    path, filename = os.path.split(filepath)
    filename, extension = os.path.splitext(filename)
    return path, filename, extension


filepath = '/home/user/documents/example.txt'
result = split_filepath(filepath)
print(result)