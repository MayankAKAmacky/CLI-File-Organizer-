import os
import shutil
import argparse

def organize_files(path):
    if not os.path.exists(path):
        print("Invalid path")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = file.split(".")[-1].lower()

            if ext in ["jpg", "png"]:
                folder = "Images"
            elif ext in ["mp4", "mkv"]:
                folder = "Videos"
            elif ext in ["pdf", "txt"]:
                folder = "Documents"
            else:
                folder = "Others"

            target_folder = os.path.join(path, folder)
            os.makedirs(target_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(target_folder, file))


parser = argparse.ArgumentParser()
parser.add_argument("--path", required=True, help="Path to organize")

args = parser.parse_args()

organize_files(args.path)