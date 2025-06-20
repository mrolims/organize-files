# organize_files

A simple Python package and CLI tool to organize files in a directory into categorized folders based on file extensions.

---

## Features

- Automatically sorts files into folders by file type  
- Supports a wide range of file categories (documents, images, code, music, videos, archives, and more)  
- CLI tool for quick organization from the terminal  
- Python API for integrating into your scripts or projects  

---

## Installation

You can install the package by cloning the repo and installing it locally:

```bash
git clone https://github.com/mrolims/organize_files.git
cd organize_files
pip install .
```

## Usage

After installing the package, you can organize files in a directory easily using the command line or Python API.

### Command-line interface (CLI)

Organize the current directory:

```bash
organize_files
```

Organize a specific directory:

```bash
organize_files /path/to/directory
```

To see the usage instruction, run:

```bash
organize_files --help
```

### Python API

Use the `DirectoryCleaner` class directly in your Python script:

```python
from organize_files import DirectoryCleaner

# Organize current directory
organizer = DirectoryCleaner()
organizer.create_folders()
organizer.move_files()

# Or organize a specific directory (relative to your home folder)
organizer = DirectoryCleaner("Documents/MyFolder")
organizer.create_folders()
organizer.move_files()
```

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0).

You can find a copy of the license in the [LICENSE](LICENSE) file or read it online at the [GNU website](https://www.gnu.org/licenses/gpl-3.0.en.html).
