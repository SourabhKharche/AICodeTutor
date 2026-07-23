"""
context_builder.py

Creates AI-ready context from analyzed Python projects.
Responsibilities:
- Convert project data into readable text
- Prepare information for the AI model
- Provide focused explanations for specific symbols

Author: Sourabh Kharche
Project: AI Code Tutor
"""

# ==========================================================
# Context Builder
# ==========================================================
class ContextBuilder:
    """
    Converts analyzed project information into AI context.
    """
    # ======================================================
    # Project Context
    # ======================================================
    def build_project_context(self, project, analysis):
        """
        Creates a complete overview of the project.
        Parameters:
            project (Project)
            analysis (dict)
        Returns:
            str
        """
        context = ""
        context += "PROJECT OVERVIEW\n"
        context += "=" * 50
        context += "\n\n"

        # --------------------------------------------------
        # Statistics
        # --------------------------------------------------
        statistics = analysis["statistics"]
        context += "Statistics:\n"
        context += (
            f"Python Files: "
            f"{statistics['python_files']}\n"
        )
        context += (
            f"Classes: "
            f"{statistics['classes']}\n"
        )
        context += (
            f"Functions: "
            f"{statistics['functions']}\n"
        )
        context += "\n"

        # --------------------------------------------------
        # Files
        # --------------------------------------------------
        context += "FILES:\n"

        for python_file in project.files:
            context += "\n"
            context += f"File: {python_file.name}\n"

            for class_info in python_file.classes:
                context += (
                    f"  Class: "
                    f"{class_info.name}\n"
                )

                for method in class_info.methods:
                    context += (
                        f"    Method: "
                        f"{method.name}\n"
                    )

            for function in python_file.functions:
                context += (
                    f"  Function: "
                    f"{function.name}\n"
                )

        return context

    # ======================================================
    # File Context
    # ======================================================
    def build_file_context(self, python_file):
        """
        Creates context for a single Python file.
        Returns:
            str
        """
        context = ""
        context += (
            f"FILE: {python_file.name}\n"
        )
        context += "-" * 40
        context += "\n"

        # Imports
        if python_file.imports:
            context += "Imports:\n"

            for item in python_file.imports:
                context += (
                    f"- {item}\n"
                )
            context += "\n"

        # Classes
        if python_file.classes:
            context += "Classes:\n"

            for class_info in python_file.classes:
                context += (
                    f"\n{class_info.name}\n"
                )

                if class_info.docstring:
                    context += (
                        f"Purpose: "
                        f"{class_info.docstring}\n"
                    )
                context += "Methods:\n"

                for method in class_info.methods:
                    context += (
                        f"- {method.name}\n"
                    )

        # Functions
        if python_file.functions:
            context += "\nFunctions:\n"

            for function in python_file.functions:
                context += (
                    f"- {function.name}\n"
                )

        return context

    # ======================================================
    # Symbol Context
    # ======================================================
    def build_symbol_context(self, symbol):
        """
        Creates detailed context for one class/function.
        This will be used when a student clicks
        a specific piece of code in the UI.
        """
        context = ""
        context += (
            f"NAME: {symbol.name}\n"
        )
        context += "\n"

        # Documentation
        if symbol.docstring:
            context += (
                "DESCRIPTION:\n"
            )
            context += (
                symbol.docstring
            )
            context += "\n\n"

        # Source code
        if symbol.source_code:
            context += (
                "SOURCE CODE:\n"
            )
            context += (
                symbol.source_code
            )

        return context