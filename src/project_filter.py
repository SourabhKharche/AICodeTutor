"""
project_filter.py

Filters unnecessary files and folders
before code analysis.

Author: Sourabh Kharche
Project: AI Code Tutor
"""

from pathlib import Path

class ProjectFilter:
    """
    Removes files that should not be analyzed.
    """
    def __init__(self):
        self.ignored_directories = [
            ".git",
            "venv",
            ".venv",
            "__pycache__",
            "node_modules",
            "build",
            "dist"
        ]
        self.ignored_files = [
            "__init__.py"
        ]

    # ======================================================
    # Check Directory
    # ======================================================
    def should_ignore_directory(self, directory):
        return directory.name in (
            self.ignored_directories
        )

    # ======================================================
    # Check File
    # ======================================================
    def should_ignore_file(self, file):
        return file.name in (
            self.ignored_files
        )

    # ======================================================
    # Filter Files
    # ======================================================
    def filter_python_files(self, files):
        """
        Returns only useful Python files.
        """
        filtered = []

        for file in files:
            ignore = False

            for parent in file.parents:
                if self.should_ignore_directory(
                    parent
                ):
                    ignore = True

            if self.should_ignore_file(file):
                ignore = True

            if not ignore:
                filtered.append(file)

        return filtered