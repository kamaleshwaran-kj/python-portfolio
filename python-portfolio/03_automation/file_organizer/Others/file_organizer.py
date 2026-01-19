import os
import shutil

# Folder to organize (current directory)
TARGET_FOLDER = os.getcwd()

# File type mapping
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"]
}


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def organize_files():
    files = os.listdir(TARGET_FOLDER)

    for file in files:
        file_path = os.path.join(TARGET_FOLDER, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        moved = False
        file_ext = os.path.splitext(file)[1].lower()

        for folder, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                create_folder(folder)
                shutil.move(file_path, os.path.join(folder, file))
                moved = True
                break

        if not moved:
            create_folder("Others")
            shutil.move(file_path, os.path.join("Others", file))


def main():
    print(f"⚠️ This will organize files in:\n{TARGET_FOLDER}")
    confirm = input("Proceed? (yes/no): ").lower()

    if confirm == "yes":
        organize_files()
        print("✅ Files organized successfully!")
    else:
        print("❌ Operation cancelled.")


if __name__ == "__main__":
    main()
