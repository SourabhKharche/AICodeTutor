"""
graph_visualizer.py

Creates interactive visualizations from
the project's call graph.

Author: Sourabh Kharche
Project: AI Code Tutor
"""

from pyvis.network import Network

# ==========================================================
# Graph Visualizer
# ==========================================================
class GraphVisualizer:
    """
    Converts call graph data into a visual graph.
    """
    def create_graph(self, call_graph):
        """
        Creates a PyVis network.
        Parameters:
            call_graph:
                CallGraph object
        Returns:
            Network object
        """
        # Create graph
        network = Network(
            height="600px",
            width="100%",
            directed=True
        )

        # --------------------------------------------------
        # Add nodes and edges
        # --------------------------------------------------
        for function, calls in call_graph.graph.items():
            # Add current function
            network.add_node(
                function,
                label=function
            )

            for called_function in calls:
                # Add called function
                network.add_node(
                    called_function,
                    label=called_function
                )

                # Connect them
                network.add_edge(
                    function,
                    called_function
                )

        return network

    # ======================================================
    # Save Graph
    # ======================================================
    def save_graph(
        self,
        network,
        filename="call_graph.html"
    ):
        """
        Saves graph as HTML.
        """
        network.save_graph(
            filename
        )

        return filename