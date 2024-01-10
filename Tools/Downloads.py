import os
import shutil

def organize_downloads_folder():
    # Get the path to the Downloads folder
    downloads_folder = os.path.expanduser("~/Downloads")

    # Create a dictionary to store file extensions and their corresponding subdirectories
    extensions = {}

    # Iterate through files in the Downloads folder
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)

        # Check if the path is a file (not a directory)
        if os.path.isfile(file_path):
            # Get the file extension
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension[1:].lower()  # Remove the dot and convert to lowercase

            # Check if the subdirectory already exists
            if file_extension not in extensions:
                extensions[file_extension] = os.path.join(downloads_folder, file_extension)
                os.makedirs(extensions[file_extension], exist_ok=True)

            # Move the file to the corresponding subdirectory
            destination = os.path.join(extensions[file_extension], filename)

            # Check if the file is not already in the destination
            if not os.path.exists(destination):
                shutil.move(file_path, destination)
                print(f"Moved {filename} to {file_extension} folder.")
            else:
                print(f"{filename} already exists in {file_extension} folder.")

    print("Organizing completed.")

if __name__ == "__main__":
    organize_downloads_folder()
