"""
graph_panel.py

Displays dependency graph visualization.

Responsibilities:
- Generate graph
- Render interactive graph

Author:
Sourabh Kharche

Project:
AI Code Tutor
"""


import streamlit as st

import streamlit.components.v1 as components


from graph_visualizer import GraphVisualizer



# ==========================================================
# Graph Panel
# ==========================================================


def render_graph_panel(results):
    """
    Displays dependency graph.

    Parameters:

        results:
            Analyzer output dictionary

    """



    st.header(
        "🕸️ Dependency Graph"
    )



    # ======================================================
    # Check Graph Availability
    # ======================================================


    if "call_graph" not in results:


        st.warning(
            "No call graph available."
        )


        return



    # ======================================================
    # Generate Graph
    # ======================================================


    if st.button(
        "Generate Dependency Graph"
    ):



        with st.spinner(
            "Creating graph..."
        ):



            visualizer = (
                GraphVisualizer()
            )


            graph = (
                visualizer.create_graph(
                    results["call_graph"]
                )
            )


            filename = (
                "call_graph.html"
            )


            visualizer.save_graph(
                graph,
                filename
            )



        st.success(
            "Graph created!"
        )



        # ----------------------------------------------
        # Display HTML
        # ----------------------------------------------


        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:


            html = file.read()



        components.html(
            html,
            height=650
        )