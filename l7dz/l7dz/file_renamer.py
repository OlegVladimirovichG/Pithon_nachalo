import os

def rename_files(directory, new_name, source_extension, new_extension):
    file_list = os.listdir(directory)

    # Фильтруем файлы по расширению
    filtered_files = [file for file in file_list if file.endswith(source_extension)]

    # Переименовываем файлы
    for i, filename in enumerate(filtered_files):
        # Разбиваем имя файла на основную часть и расширение
        base_name, extension = os.path.splitext(filename)

        # Составляем новое имя файла с порядковым номером
        new_filename = f"{base_name}_{new_name}_{i + 1}.{new_extension}"

        # Полный путь к исходному файлу
        source_path = os.path.join(directory, filename)

        # Полный путь к новому файлу
        new_path = os.path.join(directory, new_filename)

        # Переименовываем файл
        os.rename(source_path, new_path)

        print(f"Переименован файл {filename} в {new_filename}")
