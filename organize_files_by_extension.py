import os
import shutil
import sys
from pathlib import Path


def organize_files(target_dir):
    """
    Organizes files in the specified directory into subdirectories based on their file extensions.
    """
    path = Path(target_dir).resolve()

    if not path.exists():
        print(f"Error: The directory '{target_dir}' does not exist.")
        return
    if not path.is_dir():
        print(f"Error: '{target_dir}' is not a directory.")
        return

    print(f"Organizing files in: {path}")

    # Avoid moving the script itself if it's inside the target dir
    script_path = Path(__file__).resolve()

    files_moved = 0

    for item in path.iterdir():
        # We only want to move files, not directories
        if item.is_dir():
            continue

        # Don't move the script itself
        if item.resolve() == script_path:
            continue

        # Skip hidden files (files starting with .)
        if item.name.startswith("."):
            continue

        # Get file extension
        # suffix includes the dot, e.g., '.txt'
        file_ext = item.suffix.lower()

        if not file_ext:
            folder_name = "no_extension"
        else:
            folder_name = file_ext[1:]  # remove the dot

        # Create destination folder path
        destination_folder = path / folder_name

        try:
            destination_folder.mkdir(exist_ok=True)
        except OSError as e:
            print(f"Error creating folder '{folder_name}': {e}")
            continue

        destination_file = destination_folder / item.name

        # Move the file
        try:
            # Avoid overwriting
            if destination_file.exists():
                print(f"Skipped: '{item.name}' already exists in '{folder_name}'")
            else:
                shutil.move(str(item), str(destination_file))
                print(f"Moved: '{item.name}' -> '{folder_name}/'")
                files_moved += 1
        except Exception as e:
            print(f"Error moving '{item.name}': {e}")

    print(f"Done. Moved {files_moved} files.")


if __name__ == "__main__":
    # If a directory argument is provided, use it. Otherwise, use the current working directory.
    if len(sys.argv) > 1:
        target_directory = sys.argv[1]
    else:
        target_directory = os.getcwd()
        print("No directory provided. Using current working directory.")

    organize_files(target_directory)
