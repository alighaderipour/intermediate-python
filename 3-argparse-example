import argparse
import os
import shutil

# File categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".tar", ".rar", ".gz"],
    "Scripts": [".py", ".sh", ".bat"],
}

def organize_files(directory, dry_run=False):
    """Organizes files in a directory into categorized folders."""
    if not os.path.exists(directory):
        print(f"❌ Error: Directory '{directory}' does not exist.")
        return

    # Create category folders if they don't exist
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            if not dry_run:
                os.makedirs(category_path)

    # Scan and move files
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        file_ext = os.path.splitext(file)[1].lower()

        # Find the right category
        for category, extensions in FILE_CATEGORIES.items():
            if file_ext in extensions:
                destination = os.path.join(directory, category, file)
                if dry_run:
                    print(f"🔍 [Dry Run] Would move: {file} → {category}/")
                else:
                    shutil.move(file_path, destination)
                    print(f"✅ Moved: {file} → {category}/")
                break
        else:
            # If no category found, put it in 'Others'
            other_path = os.path.join(directory, "Others")
            if not os.path.exists(other_path) and not dry_run:
                os.makedirs(other_path)

            destination = os.path.join(other_path, file)
            if dry_run:
                print(f"🔍 [Dry Run] Would move: {file} → Others/")
            else:
                shutil.move(file_path, destination)
                print(f"✅ Moved: {file} → Others/")

def main():
    parser = argparse.ArgumentParser(description="📂 File Organizer - Automatically sort files into folders.")
    
    parser.add_argument("directory", help="Directory to organize")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be moved without actually moving files")

    args = parser.parse_args()
    organize_files(args.directory, args.dry_run)

if __name__ == "__main__":
    main()


    
#python organizer.py /path/to/directory

#dry-run
#python organizer.py /path/to/directory --dry-run
