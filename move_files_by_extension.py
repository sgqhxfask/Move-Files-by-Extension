import os
import shutil

def move_files_by_extension(source_dir, target_dir, extension):
    """
    Moves all files with a specific extension from source_dir (recursively) to target_dir.

    Args:
        source_dir (str): Source directory path.
        target_dir (str): Destination directory path.
        extension (str): Extension to filter by (e.g., '.txt').
    """
    if not os.path.isdir(source_dir):
        print(f"Source directory does not exist: {source_dir}")
        return

    os.makedirs(target_dir, exist_ok=True)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(extension):
                src_path = os.path.join(root, file)
                dest_path = os.path.join(target_dir, file)
                # Handle filename collision
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(file)
                    i = 1
                    while True:
                        new_name = f"{base}_{i}{ext}"
                        new_dest_path = os.path.join(target_dir, new_name)
                        if not os.path.exists(new_dest_path):
                            dest_path = new_dest_path
                            break
                        i += 1
                shutil.move(src_path, dest_path)
                print(f"Moved: {src_path} -> {dest_path}")

if __name__ == "__main__":
    source = input("Source directory: ").strip()
    target = input("Target directory: ").strip()
    ext = input("File extension (e.g., .txt): ").strip()
    move_files_by_extension(source, target, ext)
