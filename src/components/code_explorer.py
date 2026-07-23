"""
code_explorer.py

Provides a code browsing interface.

Responsibilities:
- Display classes
- Display methods
- Display functions
- Show source code
- Show documentation

Author:
Sourabh Kharche

Project:
AI Code Tutor
"""


import streamlit as st



# ==========================================================
# Build Symbol List
# ==========================================================


def build_symbol_list(project):
    """
    Creates a list of selectable code symbols.

    Example:

    PhysicsEngine
    PhysicsEngine.simulate
    distance

    """


    symbols = []


    for python_file in project.files:


        # ----------------------------------------------
        # Classes and methods
        # ----------------------------------------------

        for class_info in python_file.classes:


            symbols.append(
                class_info.name
            )


            for method in class_info.methods:


                symbols.append(
                    f"{class_info.name}.{method.name}"
                )



        # ----------------------------------------------
        # Functions
        # ----------------------------------------------

        for function in python_file.functions:


            symbols.append(
                function.name
            )


    return symbols



# ==========================================================
# Code Explorer Component
# ==========================================================


def render_code_explorer(project, results):
    """
    Displays code explorer.

    Returns:
        Selected symbol
    """



    st.header(
        "🔎 Code Explorer"
    )



    symbols = build_symbol_list(
        project
    )



    if not symbols:


        st.warning(
            "No code elements found."
        )

        return None



    selected_symbol = st.selectbox(
        "Select code element:",
        symbols
    )



    # --------------------------------------------------
    # Find symbol information
    # --------------------------------------------------

    symbol_table = (
        results["symbol_table"]
    )


    symbol = symbol_table.lookup(
        selected_symbol
    )



    if symbol:



        st.subheader(
            selected_symbol
        )



        # ----------------------------------------------
        # Documentation
        # ----------------------------------------------

        st.write(
            "### Description"
        )


        if symbol.docstring:


            st.info(
                symbol.docstring
            )


        else:


            st.info(
                "No documentation available."
            )



        # ----------------------------------------------
        # Source code
        # ----------------------------------------------

        st.write(
            "### Source Code"
        )


        if symbol.source_code:


            st.code(
                symbol.source_code,
                language="python"
            )


        else:


            st.warning(
                "Source code unavailable."
            )



    return selected_symbol