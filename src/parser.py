"""
parser.py

Parses Python source code using Python's built-in AST module.
Responsibilities:
- Parse imports
- Parse constants
- Parse classes
- Parse methods
- Parse standalone functions
- Detect the program entry point

Author: Sourabh Kharche
Project: AI Code Tutor
"""

import ast
from pathlib import Path
from models import (
    PythonFile,
    ClassInfo,
    FunctionInfo,
)

# ==========================================================
# Python Parser
# ==========================================================
class PythonParser:
    """
    Converts Python source code into structured objects.
    """
    def parse(self, filepath):
        """
        Parses one Python source file.
        Parameters:
            filepath (Path): Path to the Python file.
        Returns:
            PythonFile
        """
        # Convert to a Path object.
        path = Path(filepath)

        # Read the source code.
        source = path.read_text(encoding="utf-8")

        # Build the Abstract Syntax Tree.
        tree = ast.parse(source)

        # Create the PythonFile model.
        python_file = PythonFile(
            name=path.name,
            path=path
        )

        # Save the AST for future analysis.
        python_file.tree = tree

        # Parse each section of the file.
        self.parse_imports(tree, python_file)
        self.parse_constants(tree, python_file)
        self.parse_classes(tree, source, python_file)
        self.parse_functions(tree, source, python_file)
        self.detect_entry_point(tree, python_file)

        return python_file

    # ======================================================
    # Imports
    # ======================================================
    def parse_imports(self, tree, python_file):
        """
        Extract all imports from the file.
        """
        for node in tree.body:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    python_file.imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""

                for alias in node.names:
                    python_file.imports.append(
                        f"{module}.{alias.name}"
                    )

    # ======================================================
    # Constants
    # ======================================================
    def parse_constants(self, tree, python_file):
        """
        Find global constants.
        A constant is assumed to be a variable with
        an uppercase name.
        """
        for node in tree.body:
            if not isinstance(node, ast.Assign):
                continue

            for target in node.targets:
                if isinstance(target, ast.Name):
                    if target.id.isupper():
                        python_file.constants.append(
                            target.id
                        )

    # ======================================================
    # Classes
    # ======================================================
    def parse_classes(self, tree, source, python_file):
        """
        Parse every class in the file.
        """
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue

            class_info = ClassInfo(
                name=node.name,
                docstring=ast.get_docstring(node) or "",
                source_code=ast.get_source_segment(source, node) or ""
            )

            # Parse methods.
            for item in node.body:
                if not isinstance(item, ast.FunctionDef):
                    continue

                arguments = []

                for argument in item.args.args:
                    arguments.append(argument.arg)

                method = FunctionInfo(
                    name=item.name,
                    arguments=arguments,
                    docstring=ast.get_docstring(item) or "",
                    source_code=ast.get_source_segment(source, item) or ""
                )
                class_info.methods.append(method)
            python_file.classes.append(class_info)

    # ======================================================
    # Standalone Functions
    # ======================================================
    def parse_functions(self, tree, source, python_file):
        """
        Parse standalone functions.
        Methods inside classes are ignored because
        they are handled in parse_classes().
        """
        for node in tree.body:
            if not isinstance(node, ast.FunctionDef):
                continue

            arguments = []

            for argument in node.args.args:
                arguments.append(argument.arg)

            function = FunctionInfo(
                name=node.name,
                arguments=arguments,
                docstring=ast.get_docstring(node) or "",
                source_code=ast.get_source_segment(source, node) or ""
            )
            python_file.functions.append(function)

    # ======================================================
    # Entry Point
    # ======================================================
    def detect_entry_point(self, tree, python_file):
        """
        Detect:
        if __name__ == "__main__":
        """
        for node in tree.body:
            if not isinstance(node, ast.If):
                continue

            test = node.test

            if (
                isinstance(test, ast.Compare)
                and isinstance(test.left, ast.Name)
                and test.left.id == "__name__"
                and len(test.comparators) == 1
                and isinstance(test.comparators[0], ast.Constant)
                and test.comparators[0].value == "__main__"
            ):
                python_file.has_entry_point = True