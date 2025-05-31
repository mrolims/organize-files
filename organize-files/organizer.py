import os
from typing import Optional


class DirectoryCleaner:
    def __init__(self,
                 directory: Optional[str] = None) -> None:
        if directory is None:
            self.directory = os.getcwd()
        else:
            home = os.path.expanduser("~")
            self.directory = os.path.join(home, directory)
        if not os.path.exists(self.directory):
            raise FileNotFoundError(
                f"The directory {self.directory} does not exist.")

    folders_extensions = {
        "TextFiles": ["txt", "md", "log", "csv"],
        "Images": ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp", "heic", "svg"],
        "Documents": ["pdf", "doc", "docx", "odt", "rtf", "djvu", "epub", "tex", "xps"],
        "Spreadsheets": ["xls", "xlsx", "ods", "csv"],
        "Presentations": ["ppt", "pptx", "odp", "key"],
        "Music": ["mp3", "wav", "aac", "ogg", "flac", "m4a"],
        "Videos": ["mp4", "mkv", "avi", "mov", "wmv", "flv", "webm"],
        "Bibtex": ["bib", "bibtex", "ris", "bbl"],
        "Archives": ["zip", "rar", "tar", "gz", "7z", "bz2", "xz", "iso"],
        "Code": ["py", "ipynb", "js", "ts", "java", "cpp", "c", "h", "html", "css", "json", "xml", "sh", "bat", "rb", "php", "pl", "r", "go", "swift", "kt", "scala"],
        "Applications": ["exe", "msi", "app", "dmg", "apk", "deb", "rpm"],
        "Fonts": ["ttf", "otf", "woff", "woff2"],
        "3DModels": ["obj", "stl", "fbx", "gltf", "glb", "3ds"],
        "CAD": ["dwg", "dxf"],
        "Design": ["psd", "ai", "sketch", "xd", "fig", "svg"],
        "Database": ["db", "sqlite", "sql", "mdb", "accdb"],
        "Config": ["ini", "cfg", "conf", "yaml", "yml", "toml", "env"],
        "Executables": ["bin", "out", "run"],
        "Logs": ["log"],
        "Backups": ["bak", "old", "tmp"],
        "PythonPackages": ["whl", "egg", "tar.gz"],
        "Latex": ["tex", "cls", "sty"],
    }

    def create_folders(self) -> None:
        for folder, extensions in self.folders_extensions.items():
            folder_path = os.path.join(self.directory, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

    def move_files(self) -> None:
        for file in os.listdir(self.directory):
            # Check if the file is a regular file
            if os.path.isfile(file):
                # Get the file extension
                file_extension = file.split(
                    '.')[-1].lower() if '.' in file else None

                # Move the file to the appropriate folder based on its extension
                moved = False
                for folder, extensions in self.folders_extensions.items():
                    if file_extension in extensions:
                        os.rename(file, os.path.join(folder, file))
                        moved = True
                        break

                # If no matching folder was found, move it to "Others"
                if not moved:
                    if not os.path.exists("Others"):
                        os.makedirs("Others")
                    os.rename(file, os.path.join("Others", file))
