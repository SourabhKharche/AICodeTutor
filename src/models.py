"""
models.py

Contains all of the data models used by the AI Code Tutor.
These classes store information about:
- Functions
- Classes
- Python files
- Entire projects

Author: Sourabh Kharche
Project: AI Code Tutor
"""

from dataclasses import dataclass, field

# ==========================================================
# Function Information
# ==========================================================
@dataclass
class FunctionInfo:
    """
    Stores information about a Python function or class method.
    """
    # Name of the function
    name: str
    # List of function arguments
    arguments: list[str] = field(default_factory=list)
    # Function documentation (if available)
    docstring: str = ""
    # Original source code
    source_code: str = ""

# ==========================================================
# Class Information
# ==========================================================
@dataclass
class ClassInfo:
    """
    Stores information about a Python class.
    """
    # Name of the class
    name: str
    # List of methods inside the class
    methods: list[FunctionInfo] = field(default_factory=list)
    # Class documentation (if available)
    docstring: str = ""
    # Original source code
    source_code: str = ""

# ==========================================================
# Python File Information
# ==========================================================
@dataclass
class PythonFile:
    """
    Stores everything discovered while parsing one Python file.
    """
    # File name (Example: physics.py)
    name: str
    # Full path to the file
    path: str
    # Imported modules
    imports: list[str] = field(default_factory=list)
    # Global constants
    constants: list[str] = field(default_factory=list)
    # Classes found in this file
    classes: list[ClassInfo] = field(default_factory=list)
    # Standalone functions
    functions: list[FunctionInfo] = field(default_factory=list)
    # True if this file contains:
    # if __name__ == "__main__":
    has_entry_point: bool = False
    # Parsed Abstract Syntax Tree
    tree: object = None

# ==========================================================
# Project Information
# ==========================================================
@dataclass
class Project:
    """
    Represents an entire Python project.
    Every parsed Python file is stored here.
    """
    files: list[PythonFile] = field(default_factory=list)