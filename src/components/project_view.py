"""
project_view.py

Displays project information.
Responsibilities:
- Show project statistics
- Show project structure
- Display files, classes, and functions

Author: Sourabh Kharche
Project: AI Code Tutor
"""

import streamlit as st

# ==========================================================
# Project View Component
# ==========================================================
def render_project_view(project, results):
    """
    Displays project overview.
    Parameters:
        project:
            Parsed Project object
        results:
            Analyzer output dictionary
    """

    # ======================================================
    # Project Summary
    # ======================================================
    st.header(
        "Project Summary"
    )

    statistics = (
        results["statistics"]
    )

    # Create metric columns
    col1, col2, col3, col4 = (
        st.columns(4)
    )
    col1.metric(
        "Python Files",
        statistics["python_files"]
    )
    col2.metric(
        "Classes",
        statistics["classes"]
    )
    col3.metric(
        "Functions",
        statistics["functions"]
    )
    col4.metric(
        "Methods",
        statistics["methods"]
    )

    # ======================================================
    # Project Structure
    # ======================================================
    st.header(
        "📁 Project Structure"
    )

    for python_file in project.files:
        with st.expander(
            python_file.name
        ):
            # ----------------------------------------------
            # Imports
            # ----------------------------------------------
            st.write(
                "### Imports"
            )

            if python_file.imports:
                for item in python_file.imports:
                    st.write(
                        f"- {item}"
                    )
            else:
                st.write(
                    "No imports"
                )

            # ----------------------------------------------
            # Classes
            # ----------------------------------------------
            st.write(
                "### Classes"
            )

            if python_file.classes:
                for class_info in python_file.classes:
                    st.write(
                        f"#### {class_info.name}"
                    )

                    if class_info.docstring:
                        st.caption(
                            class_info.docstring
                        )

                    st.write(
                        "Methods:"
                    )

                    for method in class_info.methods:
                        st.write(
                            f"- {method.name}()"
                        )
            else:
                st.write(
                    "No classes"
                )

            # ----------------------------------------------
            # Functions
            # ----------------------------------------------
            st.write(
                "### Functions"
            )

            if python_file.functions:
                for function in python_file.functions:
                    st.write(
                        f"- {function.name}()"
                    )
            else:
                st.write(
                    "No functions"
                )