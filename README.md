# Move Files by Extension

This Python script moves all files with a specific extension from a source directory (recursively) to a target directory.

## Usage

1. Place `move_files_by_extension.py` in your project folder.
2. Run the script:
    ```sh
    python move_files_by_extension.py
    ```
3. Enter:
    - Source directory (where files are searched)
    - Target directory (where files are moved)
    - File extension (e.g., `.txt`)

## Features

- Recursively finds files with the specified extension.
- Handles filename collisions by renaming moved files.
- Creates the target directory if it does not exist.

## Example

If you want to move all `.txt` files from `./documents` to `./text_files`, run:

```sh
python move_files_by_extension.py
```
Then enter:
```
Source directory: ./documents
Target directory: ./text_files
File extension (e.g., .txt): .txt
```

## Requirements

- Python 3.x

No external dependencies.

## License

MIT License.
