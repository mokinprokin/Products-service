import os
from django.core.files.storage import default_storage
from django.utils import timezone
from django.core.files.storage import FileSystemStorage


def rename_image(image, user_id):
    # Получаем имя и расширение файла
    base_filename, ext = os.path.splitext(image.name)

    # Формируем имя папки с ID пользователя
    user_directory = str(user_id)

    # Формируем новое имя файла и полный путь сохранения
    new_filename = f"{base_filename}{ext}"  # Оригинальное имя файла
    file_path = os.path.join(
        user_directory, new_filename
    )  # Путь: user_id/оригинальное_имя_файла

    # Проверяем существование директории
    user_dir_path = default_storage.path(user_directory)

    if not os.path.exists(user_dir_path):
        os.makedirs(user_dir_path)

    # Получаем список файлов в папке
    files = default_storage.listdir(user_directory)[1]  # [0] — это папки, [1] — файлы
    if len(files) >= 2:
        # Сортируем файлы по времени последнего изменения и удаляем самый старый
        files_with_times = [
            (f, default_storage.get_modified_time(os.path.join(user_directory, f)))
            for f in files
        ]
        oldest_file = min(files_with_times, key=lambda x: x[1])[
            0
        ]  # Получаем имя самого старого файла
        default_storage.delete(os.path.join(user_directory, oldest_file))

    # Проверяем, существует ли файл с таким именем
    if default_storage.exists(file_path):
        raise FileExistsError(
            f"Файл с именем '{new_filename}' уже существует в папке пользователя с ID {user_id}."
        )

    # Сохраняем изображение с новым именем
    file_path = default_storage.save(file_path, image)

    return file_path


def rename_image_host(image, user_id):
    # Получаем имя и расширение файла
    base_filename, ext = os.path.splitext(image.name)

    # Формируем имя папки с ID пользователя
    user_directory = str(user_id) + "/hosts/"

    # Формируем новое имя файла и полный путь сохранения
    new_filename = f"{base_filename}{ext}"  # Оригинальное имя файла
    file_path = os.path.join(
        user_directory, new_filename
    )  # Путь: user_id/оригинальное_имя_файла

    # Проверяем существование директории
    user_dir_path = default_storage.path(user_directory)

    if not os.path.exists(user_dir_path):
        os.makedirs(user_dir_path)

    # Получаем список файлов в папке
    files = default_storage.listdir(user_directory)[1]  # [0] — это папки, [1] — файлы
    # Проверяем, существует ли файл с таким именем
    # Сохраняем изображение с новым именем
    file_path = default_storage.save(file_path, image)

    return file_path


def rename_images_host(image, user_id):
    # Получаем имя и расширение файла
    base_filename, ext = os.path.splitext(image.name)

    # Формируем имя папки с ID пользователя
    user_directory = str(user_id) + "/hosts/images"

    # Формируем новое имя файла и полный путь сохранения
    new_filename = f"{base_filename}{ext}"  # Оригинальное имя файла
    file_path = os.path.join(
        user_directory, new_filename
    )  # Путь: user_id/оригинальное_имя_файла

    # Проверяем существование директории
    user_dir_path = default_storage.path(user_directory)

    if not os.path.exists(user_dir_path):
        os.makedirs(user_dir_path)

    # Получаем список файлов в папке
    files = default_storage.listdir(user_directory)[1]  # [0] — это папки, [1] — файлы


    # Сохраняем изображение с новым именем
    file_path = default_storage.save(file_path, image)

    return file_path
