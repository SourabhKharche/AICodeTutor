"""
scanner.py

Searches a project directory and finds Python files.

Responsibilities:
- Search folders recursively
- Collect Python files
- Apply project filtering rules
- Return a clean list of files

Author: Sourabh Kharche
Project: AI Code Tutor
"""


from pathlib import Path

from project_filter import ProjectFilter



# ==========================================================
# Project Scanner
# ==========================================================


class ProjectScanner:
    """
    Finds useful Python files inside a project directory.
    """



    def __init__(self):
        """
        Initialize scanner with a project filter.
        """

        self.filter = ProjectFilter()



    # ======================================================
    # Scan Project
    # ======================================================


    def scan(self, project_path):
        """
        Searches the given directory for Python files.

        Parameters:
            project_path (str | Path):
                Path to project folder.

        Returns:
            list[Path]:
                Filtered Python files.
        """



        # --------------------------------------------------
        # Convert input into Path object
        # --------------------------------------------------

        project_path = Path(
            project_path
        )



        # --------------------------------------------------
        # Validate directory
        # --------------------------------------------------

        if not project_path.exists():

            raise FileNotFoundError(
                f"Project folder not found: {project_path}"
            )



        if not project_path.is_dir():

            raise NotADirectoryError(
                f"{project_path} is not a directory."
            )



        # --------------------------------------------------
        # Find Python files
        # --------------------------------------------------

        python_files = list(
            project_path.rglob("*.py")
        )



        # --------------------------------------------------
        # Apply filtering rules
        # --------------------------------------------------

        python_files = (
            self.filter.filter_python_files(
                python_files
            )
        )



        # --------------------------------------------------
        # Sort for consistent output
        # --------------------------------------------------

        python_files.sort()



        return python_files