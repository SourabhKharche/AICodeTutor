"""
sidebar.py

Handles project input controls.
Responsibilities:
- Local folder selection
- GitHub repository import

Author: Sourabh Kharche
Project: AI Code Tutor
"""

import streamlit as st
from pathlib import Path
from github_importer import GitHubImporter

# ==========================================================
# Sidebar Component
# ==========================================================
def render_sidebar():
    """
    Displays sidebar controls.
    Returns:
        project path
    """
    st.sidebar.title(
        "Project Source"
    )

    source = st.sidebar.radio(
        "Choose source:",
        [
            "Local Folder",
            "GitHub Repository"
        ]
    )

    project_path = None

    # --------------------------------------------------
    # Local Folder
    # --------------------------------------------------
    if source == "Local Folder":
        path = st.sidebar.text_input(
            "Project folder path:"
        )

        if path:
            project_path = Path(path)

    # --------------------------------------------------
    # GitHub
    # --------------------------------------------------
    else:
        url = st.sidebar.text_input(
            "GitHub URL:"
        )

        if st.sidebar.button(
            "Import Repository"
        ):
            importer = GitHubImporter()

            with st.spinner(
                "Downloading repository..."
            ):
                project_path = (
                    importer.clone_repository(
                        url
                    )
                )
                st.session_state.project_path = (
                    project_path
                )
                st.sidebar.success(
                    "Repository imported!"
                )

    return project_path