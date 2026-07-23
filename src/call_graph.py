"""
call_graph.py

Builds a function call graph for a parsed Python project.

The call graph shows which functions and methods call
other functions or methods.

Author: Sourabh Kharche
Project: AI Code Tutor
"""

import ast


# ==========================================================
# Call Graph Builder
# ==========================================================

class CallGraph:
    """
    Builds a call graph by walking the AST of every
    function and method in the project.
    """

    def __init__(self):
        """
        Create an empty call graph.
        """

        self.graph = {}

    # ======================================================
    # Build Call Graph
    # ======================================================

    def build(self, project):
        """
        Analyze every parsed file and build the call graph.

        Parameters:
            project (Project): Parsed project.
        """

        # Remove any previous results.
        self.graph.clear()

        # Visit every parsed Python file.
        for python_file in project.files:

            # Skip files that were not parsed correctly.
            if python_file.tree is None:
                continue

            # Walk through every node in the AST.
            for node in ast.walk(python_file.tree):

                # We only care about functions.
                if not isinstance(node, ast.FunctionDef):
                    continue

                # Find every function call inside this function.
                calls = self.find_function_calls(node)

                # Store the result.
                self.graph[node.name] = calls

    # ======================================================
    # Find Function Calls
    # ======================================================

    def find_function_calls(self, function_node):
        """
        Return every function called inside a function.

        Parameters:
            function_node (ast.FunctionDef)

        Returns:
            list[str]
        """

        calls = []

        # Search every node inside the function.
        for node in ast.walk(function_node):

            if not isinstance(node, ast.Call):
                continue

            # Example:
            # print()
            if isinstance(node.func, ast.Name):

                calls.append(node.func.id)

            # Example:
            # self.update_position()
            elif isinstance(node.func, ast.Attribute):

                calls.append(node.func.attr)

        # Remove duplicate calls while preserving order.
        unique_calls = []

        for call in calls:

            if call not in unique_calls:
                unique_calls.append(call)

        return unique_calls

    # ======================================================
    # Lookup
    # ======================================================

    def get_calls(self, function_name):
        """
        Return every function called by the given function.
        """

        return self.graph.get(function_name, [])

    # ======================================================
    # Display
    # ======================================================

    def display(self):
        """
        Print the call graph.
        """

        print("\n" + "=" * 60)
        print("CALL GRAPH")
        print("=" * 60)

        if not self.graph:

            print("\nNo function calls found.")
            return

        # Print functions alphabetically.
        function_names = list(self.graph.keys())
        function_names.sort()

        for function_name in function_names:

            print(f"\n{function_name}")

            calls = self.graph[function_name]

            if not calls:
                print("    └── No function calls")
                continue

            for call in calls:
                print(f"    └── {call}")