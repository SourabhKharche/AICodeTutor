"""
github_importer.py

Downloads GitHub repositories for analysis.
Responsibilities:
- Clone repositories
- Manage local repository copies

Author: Sourabh Kharche
Project: AI Code Tutor
"""

from pathlib import Path
import git

# ==========================================================
# GitHub Importer
# ==========================================================
class GitHubImporter:
    """
    Handles importing GitHub repositories.
    """
    def __init__(self):
        """
        Create importer.
        """
        self.download_folder = Path(
            "downloaded_projects"
        )
        self.download_folder.mkdir(
            exist_ok=True
        )

    # ======================================================
    # Clone Repository
    # ======================================================
    def clone_repository(self, url):
        """
        Clone a GitHub repository.
        Parameters:
            url:
                GitHub repository URL
        Returns:
            Path to downloaded project
        """
        # Extract repository name
        repo_name = (
            url
            .split("/")
            [-1]
            .replace(
                ".git",
                ""
            )
        )

        destination = (
            self.download_folder
            /
            repo_name
        )

        # Avoid cloning twice
        if destination.exists():
            return destination

        # Clone repository
        git.Repo.clone_from(
            url,
            destination
        )

        return destination