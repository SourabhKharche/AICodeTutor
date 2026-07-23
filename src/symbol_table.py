"""
symbol_table.py

Builds a symbol table for an entire Python project.

A symbol table allows the analyzer to quickly locate:
- Classes
- Standalone functions
- Class methods

Author: Sourabh Kharche
Project: AI Code Tutor
"""


# ==========================================================
# Symbol Table
# ==========================================================

class SymbolTable:
    """
    Stores references to every class, function,
    and method in the project.
    """

    def __init__(self):
        """
        Create an empty symbol table.
        """

        self.symbols = {}

    # ======================================================
    # Build Symbol Table
    # ======================================================

    def build(self, project):
        """
        Build the symbol table from the parsed project.
        """

        # Clear previous data.
        self.symbols.clear()

        # Visit every parsed Python file.
        for python_file in project.files:

            # ---------------------------------------------
            # Store classes
            # ---------------------------------------------
            for class_info in python_file.classes:

                self.symbols[class_info.name] = class_info

                # -----------------------------------------
                # Store methods
                # -----------------------------------------
                for method in class_info.methods:

                    symbol_name = (
                        f"{class_info.name}.{method.name}"
                    )

                    self.symbols[symbol_name] = method

            # ---------------------------------------------
            # Store standalone functions
            # ---------------------------------------------
            for function in python_file.functions:

                self.symbols[function.name] = function

    # ======================================================
    # Lookup
    # ======================================================

    def lookup(self, name):
        """
        Return a symbol by name.

        Parameters:
            name (str)

        Returns:
            ClassInfo, FunctionInfo, or None
        """

        return self.symbols.get(name)

    # ======================================================
    # Check if Symbol Exists
    # ======================================================

    def contains(self, name):
        """
        Returns True if the symbol exists.
        """

        return name in self.symbols

    # ======================================================
    # Get All Symbol Names
    # ======================================================

    def get_symbol_names(self):
        """
        Returns every symbol name in alphabetical order.
        """

        names = list(self.symbols.keys())

        names.sort()

        return names

    # ======================================================
    # Display
    # ======================================================

    def display(self):
        """
        Print the contents of the symbol table.
        """

        print("\n" + "=" * 60)
        print("SYMBOL TABLE")
        print("=" * 60)

        if not self.symbols:

            print("\nNo symbols found.")

            return

        for name in self.get_symbol_names():

            symbol = self.symbols[name]

            symbol_type = type(symbol).__name__

            print(f"{name:<35} {symbol_type}")