import os
import shutil
from datetime import datetime

def organize_pictures():
    pictures_path = os.path.join(os.path.expanduser("~"), "Pictures")
    destination_path = os.path.join(pictures_path, "organized")

    if not os.path.exists(pictures_path):
        print("Default Pictures directory not found.")
        return

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    screenshots_path = os.path.join(destination_path, "Screenshots")
    if not os.path.exists(screenshots_path):
        os.makedirs(screenshots_path)

    for root, dirs, files in os.walk(pictures_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            if os.path.isfile(file_path) and is_picture_file(filename):
                if "screenshot" in filename.lower():
                    organize_screenshot(file_path, screenshots_path)
                else:
                    organize_picture(file_path, destination_path)

def organize_picture(file_path, destination_path):
    try:
        file_date = get_file_date(file_path)
        if file_date:
            year, month = file_date.year, file_date.month
            year_month_folder = os.path.join(destination_path, f"{year}-{month:02d}")

            if not os.path.exists(year_month_folder):
                os.makedirs(year_month_folder)

            move_file(file_path, year_month_folder)
        else:
            print(f"Could not determine date for file: {file_path}")

    except Exception as e:
        print(f"Error organizing file: {e}")

def organize_screenshot(file_path, screenshots_path):
    try:
        file_date = get_file_date(file_path)
        if file_date:
            year, month = file_date.year, file_date.month
            year_month_folder = os.path.join(screenshots_path, f"{year}-{month:02d}")

            if not os.path.exists(year_month_folder):
                os.makedirs(year_month_folder)

            move_file(file_path, year_month_folder)
        else:
            print(f"Could not determine date for screenshot: {file_path}")

    except Exception as e:
        print(f"Error organizing screenshot: {e}")

def is_picture_file(filename):
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}
    _, extension = os.path.splitext(filename)
    return extension.lower() in image_extensions

def get_file_date(file_path):
    try:
        # Get the modification date of the file
        file_stat = os.stat(file_path)
        file_timestamp = file_stat.st_mtime

        # Convert the timestamp to a datetime object
        file_date = datetime.fromtimestamp(file_timestamp)

        return file_date
    except Exception as e:
        print(f"Error getting file date: {e}")
        return None

def move_file(source, destination):
    try:
        shutil.move(source, destination)
    except shutil.Error as e:
        print(f"Error moving file: {e}")

if __name__ == "__main__":
    organize_pictures()
