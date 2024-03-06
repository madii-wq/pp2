import os

def delete_file(path):
    if not os.path.exists(path):
        print("File does not exist.")
        return

    if not os.access(path, os.R_OK | os.W_OK):
        print("Permission denied to access the file.")
        return

    try:
        os.remove(path)
        print("File deleted successfully.")
    except OSError as e:
        print(f"Error: {e.strerror}")

file_path = input()
delete_file(file_path)
