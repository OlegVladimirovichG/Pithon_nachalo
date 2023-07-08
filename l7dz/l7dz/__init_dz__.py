from file_renamer import rename_files
import os

# Получаем путь к текущей папке
current_directory = os.path.dirname(os.path.abspath(__file__))

# Путь к целевому каталогу (находится в текущей папке)
target_directory = os.path.join(current_directory, "test")

new_name = "new_name"
source_extension = ".txt"
new_extension = "docx"

rename_files(target_directory, new_name, source_extension, new_extension)
