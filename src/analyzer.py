"""
analyzer.py

Coordinates the analysis of a parsed Python project.

Responsibilities:
- Build the symbol table
- Build the call graph
- Calculate project statistics
- Find the entry point
- Generate a beginner-friendly learning order

Author: Sourabh Kharche
Project: AI Code Tutor
"""

from symbol_table import SymbolTable
from call_graph import CallGraph

# ==========================================================
# Project Analyzer
# ==========================================================
class ProjectAnalyzer:
    """
    Performs high-level analysis on a parsed project.
    """
    def __init__(self):
        """
        Create the analyzer and its helper objects.
        """

        self.symbol_table = SymbolTable()
        self.call_graph = CallGraph()

    # ======================================================
    # Analyze Project
    # ======================================================
    def analyze(self, project):
        """
        Analyze the entire project.
        Parameters:
            project (Project)
        Returns:
            dict
        """
        # Build lookup tables.
        self.symbol_table.build(project)
        self.call_graph.build(project)

        # Collect all analysis results.
        results = {
            "statistics": self.calculate_statistics(project),
            "entry_point": self.find_entry_point(project),
            "learning_order": self.build_learning_order(project),
            "symbol_table": self.symbol_table,
            "call_graph": self.call_graph
        }

        return results

    # ======================================================
    # Project Statistics
    # ======================================================
    def calculate_statistics(self, project):
        """
        Count important project information.
        """
        statistics = {
            "python_files": 0,
            "imports": 0,
            "constants": 0,
            "classes": 0,
            "methods": 0,
            "functions": 0,
            "largest_file": None
        }

        largest_file = None
        largest_size = -1

        for python_file in project.files:
            statistics["python_files"] += 1
            statistics["imports"] += len(python_file.imports)
            statistics["constants"] += len(python_file.constants)
            statistics["classes"] += len(python_file.classes)
            statistics["functions"] += len(python_file.functions)

            method_count = 0

            for class_info in python_file.classes:
                method_count += len(class_info.methods)

            statistics["methods"] += method_count

            file_size = (
                len(python_file.classes)
                + len(python_file.functions)
                + method_count
            )

            if file_size > largest_size:
                largest_size = file_size
                largest_file = python_file.name

        statistics["largest_file"] = largest_file

        return statistics

    # ======================================================
    # Entry Point
    # ======================================================
    def find_entry_point(self, project):
        """
        Find the file containing:

            if __name__ == "__main__":
        """
        for python_file in project.files:
            if python_file.has_entry_point:
                return python_file.name

        return None

    # ======================================================
    # Learning Order
    # ======================================================
    def build_learning_order(self, project):
        """
        Suggest a simple order for reading the project.
        Files with fewer classes and functions appear first.
        """
        learning_order = []

        for python_file in project.files:
            complexity = (
                len(python_file.classes)
                + len(python_file.functions)
            )

            learning_order.append(
                (complexity, python_file.name)
            )

        learning_order.sort()
        ordered_files = []

        for _, file_name in learning_order:
            ordered_files.append(file_name)

        return ordered_files