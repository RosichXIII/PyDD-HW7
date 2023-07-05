# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
# Например:
# для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def file_renamer(new_name: str, part_of_ordinal_number: int = '', chosen_expansion: str = '',
                result_expansion: str = '', part_of_original_name: list = []):
    files_in_directory = os.listdir()
    
    for file in files_in_directory:
        
        if file == "main.py":
            continue
        original_name, original_expansion = '', file.split('.')[1]
        
        if chosen_expansion != '' and original_expansion != chosen_expansion:
            continue
        
        if result_expansion == '':
            result_expansion = original_expansion
            
        if len(part_of_original_name) == 2:
            original_name = file[(part_of_original_name[0] - 1) - 1:(part_of_original_name[1] - 1):]
        
        if part_of_ordinal_number == '' or part_of_ordinal_number >= files_in_directory.index(file) + 1:
            part_of_ordinal_number = files_in_directory.index(file) + 1
        elif part_of_ordinal_number < files_in_directory.index(file) + 1:
            part_of_ordinal_number = int(str(files_in_directory.index(file) + 1)[:part_of_ordinal_number]) 
            
        os.rename(file, f'{original_name}{new_name}{str(part_of_ordinal_number)}.{result_expansion}')
        
file_renamer('TXT-', 2, 'txt', '', [3, 5])