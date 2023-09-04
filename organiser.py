import os
import shutil

source_directory = f'C:/Users/megha/Downloads'
file_extensions = {
    "txt": "TextFiles",
    "jpg": "Images",
    "png": "Images",
    "pdf": "PDFs",
    "docx": "Documents",
    "xlsx": "Documents",
    "pptx": "Documents",
    "mp3": "Music",
    "mp4": "Videos",
}

# Create subdirectories if they don't exist
for folder in file_extensions.values():
    directory = os.path.join(source_directory, folder)
    if not os.path.exists(directory):
        os.makedirs(directory)

for files in os.listdir(source_directory):
    file_extension = files.split(".")[-1].lower()
    if file_extension in file_extensions:
        source_path = os.path.join(source_directory, files)
        target_directory = os.path.join(source_directory,file_extensions[file_extension])
        target_path = os.path.join(target_directory, target_directory)

        shutil.move(source_path, target_path)
