import os
import shutil
import argparse

# парсинг аргументів командного рядка
parser = argparse.ArgumentParser(description='Копіює файли до нової директорії, сортує по розширенням')
parser.add_argument('src_dir', help='Шлях до вихідної директорії')
parser.add_argument('dst_dir', nargs='?', default='dist', help='Шлях до директорії призначення')
args = parser.parse_args()

def copy_files(src_dir, dst_dir):
    try:
        # перебираємо всі елементи у вихідній директорії
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            if os.path.isdir(src_path):
                # якщо елемент є директорією, викликаємо copy_files рекурсивно
                copy_files(src_path, dst_dir)
            else:
                # якщо елемент є файлом, копіюємо його до відповідної піддиректорії
                ext = os.path.splitext(item)[1][1:]  # отримуємо розширення файлу
                dst_path = os.path.join(dst_dir, ext, item)
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                shutil.copy2(src_path, dst_path)
    except Exception as e:
        print(f'Помилка при копіюванні файлів: {e}')

copy_files(args.src_dir, args.dst_dir)