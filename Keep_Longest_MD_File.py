import os
import hashlib


def get_file_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def hash_content(content):
    return hashlib.sha256(content.encode()).hexdigest()


def check_and_group_files(folder_path):
    file_paths = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if file.endswith(".md")
    ]
    content_hashes = {}

    for file_path in file_paths:
        content = get_file_content(file_path)
        content_hash = hash_content(content)

        if content_hash in content_hashes:
            content_hashes[content_hash].append(file_path)
        else:
            content_hashes[content_hash] = [file_path]

    for similar_files in content_hashes.values():
        if len(similar_files) > 1:
            longest_file = max(similar_files, key=lambda x: len(get_file_content(x)))
            new_folder = os.path.join(folder_path, os.path.basename(longest_file[:-3]))

            if not os.path.exists(new_folder):
                os.makedirs(new_folder)

            for similar_file in similar_files:
                if similar_file != longest_file:
                    destination = os.path.join(
                        new_folder, os.path.basename(similar_file)
                    )
                    os.rename(similar_file, destination)


if __name__ == "__main__":
    folder_path = input(r"insert folder path: ")
    check_and_group_files(folder_path)
