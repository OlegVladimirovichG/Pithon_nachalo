import os
import sys
import logging
from collections import namedtuple

# Определение namedtuple для хранения информации о файле/каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

# Настройка логирования
logging.basicConfig(filename='file_info.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_file_info(path):
    try:
        file_info_list = []

        for root, dirs, files in os.walk(path):
            parent_dir = os.path.basename(root)
            
            for name in dirs + files:
                is_directory = os.path.isdir(os.path.join(root, name))
                base_name, extension = os.path.splitext(name) if not is_directory else (name, None)
                file_info = FileInfo(base_name, extension, is_directory, parent_dir)
                file_info_list.append(file_info)

                logging.info(f"Name: {file_info.name}, Extension: {file_info.extension}, Is Directory: {file_info.is_directory}, Parent Directory: {file_info.parent_directory}")

        return file_info_list

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return []

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path>")
    else:
        path = sys.argv[1]
        if os.path.exists(path):
            file_info_list = get_file_info(path)
            print("File information collected and logged. Check file_info.log for details.")
        else:
            print("Path does not exist.")
