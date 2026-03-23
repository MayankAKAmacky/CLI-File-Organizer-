# CLI File Organizer

A simple Python command-line tool that organizes files in a folder based on file type.

## What this project does
This script takes a folder path as a command-line argument and moves files into categorized folders.

Current categories:
- `Images` for `.jpg` and `.png`
- `Videos` for `.mp4` and `.mkv`
- `Documents` for `.pdf` and `.txt`
- `Others` for everything else

## Concepts used
This project practices:
- Python functions
- command-line arguments with `argparse`
- file and directory handling with `os`
- moving files with `shutil`
- basic automation scripting

## File
- `organizer.py` — main CLI file organizer script

## How to run
Open a terminal in this folder and run:

```bash
python organizer.py --path /path/to/your/folder
```

Example:

```bash
python organizer.py --path ~/Downloads
```

## How it works
The script:
1. checks whether the given path exists
2. lists the files in that folder
3. detects the file extension
4. creates category folders if needed
5. moves each file into the matching folder

## Example behavior
A folder containing:
- `photo.jpg`
- `movie.mkv`
- `notes.txt`
- `script.py`

would be reorganized into:
- `Images/photo.jpg`
- `Videos/movie.mkv`
- `Documents/notes.txt`
- `Others/script.py`

## Current limitations
- only a few extensions are categorized explicitly
- duplicate filenames are not handled yet
- nested folders are not processed
- hidden files are not treated differently
- the script moves files directly, so it should be used carefully on important folders

## Possible future improvements
- support more file types
- handle duplicate file names safely
- add a dry-run mode
- add recursive folder support
- show a summary of moved files
- skip already created category folders explicitly

## Why I built this
This project is part of my Python and automation learning journey. It helped me practice file handling, path logic, and writing a useful command-line script.
