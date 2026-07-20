from pathlib import Path


class FileScanner:
    def __init__(self, root_directory: str):
        self.root_directory = Path(root_directory)

    def scan(self):
        python_files = []

        for file in self.root_directory.rglob("*.py"):
            python_files.append(file)

        return python_files