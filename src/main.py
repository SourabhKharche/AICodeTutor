"""
main.py

Entry point for the AI Code Tutor application.
This file connects all project components together.
Responsibilities:
- Get project path
- Scan Python files
- Parse source code
- Analyze project
- Generate AI context

Author: Sourabh Kharche
Project: AI Code Tutor
"""

from pathlib import Path
from models import Project
from scanner import ProjectScanner
from parser import PythonParser
from analyzer import ProjectAnalyzer
from context_builder import ContextBuilder

# ==========================================================
# Display Helpers
# ==========================================================
def display_header(title):
    """
    Prints a formatted section header.
    """
    print("\n")
    print("=" * 60)
    print(title)
    print("=" * 60)

def display_statistics(statistics):
    """
    Display project statistics.
    """
    display_header("PROJECT SUMMARY")
    print(
        f"Python Files : "
        f"{statistics['python_files']}"
    )
    print(
        f"Imports      : "
        f"{statistics['imports']}"
    )
    print(
        f"Classes      : "
        f"{statistics['classes']}"
    )
    print(
        f"Methods      : "
        f"{statistics['methods']}"
    )
    print(
        f"Functions    : "
        f"{statistics['functions']}"
    )
    print(
        f"Largest File : "
        f"{statistics['largest_file']}"
    )

def display_learning_order(order):
    """
    Display suggested learning order.
    """
    display_header("LEARNING ORDER")
    position = 1

    for file in order:
        print(
            f"{position}. {file}"
        )
        position += 1

def display_files(project):
    """
    Display parsed files.
    """
    display_header("FILES ANALYZED")

    for python_file in project.files:
        print(
            f"\n📄 {python_file.name}"
        )
        print(
            f"Classes: "
            f"{len(python_file.classes)}"
        )
        print(
            f"Functions: "
            f"{len(python_file.functions)}"
        )

# ==========================================================
# Main Application
# ==========================================================

def main():
    """
    Runs the AI Code Tutor pipeline.
    """
    # ------------------------------------------------------
    # Get project path
    # ------------------------------------------------------
    project_path = input(
        "Enter Python project path: "
    )
    project_path = Path(project_path)

    # ------------------------------------------------------
    # Scan files
    # ------------------------------------------------------
    scanner = ProjectScanner()
    files = scanner.scan(project_path)
    print(
        f"\nFound {len(files)} Python files."
    )

    # ------------------------------------------------------
    # Parse files
    # ------------------------------------------------------
    parser = PythonParser()
    project = Project()

    for file in files:
        print(
            f"Parsing: {file.name}"
        )
        python_file = parser.parse(file)
        project.files.append(
            python_file
        )

    # ------------------------------------------------------
    # Analyze project
    # ------------------------------------------------------
    analyzer = ProjectAnalyzer()
    results = analyzer.analyze(
        project
    )

    # ------------------------------------------------------
    # Display results
    # ------------------------------------------------------
    display_files(project)
    display_statistics(
        results["statistics"]
    )

    if results["entry_point"]:
        display_header(
            "ENTRY POINT"
        )

        print(
            results["entry_point"]
        )

    display_learning_order(
        results["learning_order"]
    )

    # ------------------------------------------------------
    # Build AI Context
    # ------------------------------------------------------
    builder = ContextBuilder()

    context = builder.build_project_context(
        project,
        results
    )

    display_header(
        "AI CONTEXT PREVIEW"
    )
    print(context[:2000])


if __name__ == "__main__":

    main()