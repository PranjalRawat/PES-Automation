import shutil
import os
from visualize import style_message
import time

def delete_directory(relative_path, retries = 3):
    """
    Deletes the specified directory and all its contents.

    :param directory_path: Path to the directory to be deleted.
    """

    home_directory = os.path.expanduser("~")  # Get the current user's home directory
    directory_path = os.path.join(home_directory, relative_path)

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        try:
            shutil.rmtree(directory_path)
            style_message(f"Directory has been deleted successfully ===>> '{directory_path}'", 'green')
        except Exception as e:
            if retries > 0:
                time.sleep(2)
                delete_directory(relative_path, retries-1)
            else:
                style_message(f"Error: {e}", 'red')
    else:
        style_message(f"The directory does not exist ==>> '{directory_path}'", 'cyan')

def delete_file(relative_path, retries = 3):
    """
    Deletes the specified file.

    :param relative_path: Relative path from the user's home directory to the file to be deleted.
    """
    home_directory = os.path.expanduser("~")  # Get the current user's home directory
    file_path = os.path.join(home_directory, relative_path)

    if os.path.exists(file_path) and os.path.isfile(file_path):
        try:
            os.remove(file_path)
            style_message(f"File has been deleted successfully ===>> '{file_path}'", 'green')
        except Exception as e:
            if retries > 0:
                time.sleep(2)
                delete_file(relative_path, retries-1)
            else:
                style_message(f"Error: {e}", 'red')
    else:
        style_message(f"The file does not exist ==>> '{file_path}'", 'cyan')
