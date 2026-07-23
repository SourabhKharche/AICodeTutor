"""
ui.py
Creates the Streamlit web interface for AI Code Tutor.

Responsibilities:
- Display project analysis
- Show files and code structure
- Provide a beginner-friendly interface

Author: Sourabh Kharche
Project: AI Code Tutor
"""

import streamlit as st
from pathlib import Path

from models import Project
from scanner import ProjectScanner
from parser import PythonParser
from analyzer import ProjectAnalyzer
from github_importer import GitHubImporter
from components.project_view import render_project_view
from components.code_explorer import render_code_explorer
from components.ai_panel import render_ai_panel
from components.learning_panel import render_learning_panel
from components.graph_panel import render_graph_panel

# ==========================================================
# Page Configuration
# ==========================================================
st.set_page_config(
    page_title="AI Code Tutor",
    page_icon="🤖",
    layout="wide"
)

# ==========================================================
# Helper Functions
# ==========================================================
def analyze_project(project_path):
    """
    Runs the complete analysis pipeline.

    Returns:
        Project and analysis results.
    """

    # ----------------------------------------------
    # Scan project files
    # ----------------------------------------------
    scanner = ProjectScanner()
    files = scanner.scan(project_path)

    # ----------------------------------------------
    # Parse files
    # ----------------------------------------------
    parser = PythonParser()
    project = Project()

    for file in files:
        python_file = parser.parse(file)
        project.files.append(
            python_file
        )

    # ----------------------------------------------
    # Analyze project
    # ----------------------------------------------
    analyzer = ProjectAnalyzer()
    results = analyzer.analyze(
        project
    )

    return project, results

# ==========================================================
# Application Interface
# ==========================================================
def main():
    """
    Runs the Streamlit application.
    """
    # ------------------------------------------------------
    # Title
    # ------------------------------------------------------
    st.title(
        "🤖 AI Code Tutor"
    )

    st.write(
        """
Upload a Python project and learn how the code works.
"""
    )

    # ------------------------------------------------------
    # Project Input
    # ------------------------------------------------------
    project_type = st.radio(
        "Choose project source:",
        [
            "Local Folder",
            "GitHub Repository"
        ]
    )

    project_path = None

    if project_type == "Local Folder":
        project_path = st.text_input(
            "Enter project folder path:"
        )
    else:
        github_url = st.text_input(
            "Enter GitHub URL:"
        )
        if github_url:
            importer = GitHubImporter()
            if st.button(
                "Import Repository"
            ):
                with st.spinner(
                    "Downloading repository..."
                ):
                    project_path = (
                        importer.clone_repository(
                            github_url
                        )
                    )

                    st.session_state.project_path = (
                        project_path
                    )

                    st.success(
                        "Repository imported!"
                    )

    analyze_button = st.button(
        "Analyze Project"
    )

    # ------------------------------------------------------
    # Run Analysis
    # ------------------------------------------------------
    if analyze_button:
        # ----------------------------------------------
        # Check project path
        # ----------------------------------------------
        if "project_path" in st.session_state:
            project_path = (
                st.session_state.project_path
            )
        elif project_path:
            project_path = Path(
                project_path
            )
        else:
            st.error(
                "Please provide a project source."
            )
            return

        # ----------------------------------------------
        # Run Analysis
        # ----------------------------------------------
        try:
            with st.spinner(
                "Analyzing project..."
            ):
                project, results = analyze_project(
                    project_path
                )
                st.session_state.project = project
                st.session_state.results = results

            st.success(
                "Project analyzed successfully!"
            )

        except Exception as error:
            st.error(
                f"Error: {error}"
            )

    # ------------------------------------------------------
    # Display Results
    # ------------------------------------------------------
    if "project" in st.session_state:
        project = st.session_state.project
        results = st.session_state.results

        # --------------------------------------------------
        # Project View
        # --------------------------------------------------
        render_project_view(
            project,
            results
        )

        # --------------------------------------------------
        # Code Explorer
        # --------------------------------------------------
        selected_symbol = render_code_explorer(
            project,
            results
        )
        
        # --------------------------------------------------
        # AI Panel
        # --------------------------------------------------
        render_ai_panel(
            project,
            results,
            selected_symbol
        )

        # --------------------------------------------------
        # Learning Panel
        # --------------------------------------------------
        render_learning_panel(
            project,
            results
        )

        # --------------------------------------------------
        # Graph Panel
        # --------------------------------------------------
        render_graph_panel(
            results
        )

# ==========================================================
# Program Start
# ==========================================================
if __name__ == "__main__":
    main()