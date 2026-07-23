"""
learning_builder.py

Creates learning paths from analyzed Python projects.

Responsibilities:
- Understand project structure
- Create learning context
- Prepare prompts for AI lesson generation

Author:
Sourabh Kharche
Project:
AI Code Tutor
"""


# ==========================================================
# Learning Builder
# ==========================================================


class LearningBuilder:
    """
    Creates educational context from project analysis.
    """



    # ======================================================
    # Build Learning Context
    # ======================================================

    def build_learning_context(
        self,
        project,
        analysis
    ):
        """
        Creates a learning prompt from
        project information.

        Parameters:
            project:
                Parsed Project object

            analysis:
                Analyzer output dictionary

        Returns:
            str
                AI learning prompt
        """



        context = ""


        # --------------------------------------------------
        # Introduction
        # --------------------------------------------------

        context += """
You are an expert programming tutor.

Create a beginner-friendly learning path
for this Python project.

The student wants to understand:
- Python structure
- Object-oriented concepts
- Program flow
- Design decisions

"""


        # --------------------------------------------------
        # Project Statistics
        # --------------------------------------------------

        statistics = (
            analysis["statistics"]
        )


        context += "\nPROJECT STATISTICS\n"

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



        # --------------------------------------------------
        # Project Structure
        # --------------------------------------------------

        context += "\nPROJECT STRUCTURE\n"



        for python_file in project.files:


            context += (
                f"\nFile: {python_file.name}\n"
            )


            for class_info in python_file.classes:


                context += (
                    f"Class: "
                    f"{class_info.name}\n"
                )


                for method in class_info.methods:


                    context += (
                        f" Method: "
                        f"{method.name}\n"
                    )



            for function in python_file.functions:


                context += (
                    f"Function: "
                    f"{function.name}\n"
                )



        # --------------------------------------------------
        # AI Instructions
        # --------------------------------------------------

        context += """

Create:

1. Beginner concepts
2. Intermediate concepts
3. Advanced concepts
4. Explain the recommended learning order

Use simple language.
Give examples from the project.

"""


        return context