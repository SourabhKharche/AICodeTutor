from models import Project
import ast
from symbol_table import SymbolTable
from call_graph import CallGraph
class ProjectAnalyzer:

    def __init__(self, project: Project):

        self.project = project

        self.symbol_table = SymbolTable()

        self.symbol_table.build(project)
        
        self.call_graph = CallGraph()

        self.call_graph.build(project)

    def find_symbol(self, name):
        """
        Finds a symbol by exact name or partial name.
        """

        # First try exact match

        result = self.symbol_table.find(name)

        if result:
            return result


        # Search for matching symbols

        matches = []


        for symbol, information in self.symbol_table.symbols.items():

            symbol_name = information["name"]


            if symbol_name == name:

                matches.append(
                    {
                        "symbol": symbol,
                        "information": information
                    }
                )


        return matches
    
    def display_symbol_table(self):
        self.symbol_table.display()

    def total_files(self):
        return len(self.project.files)

    def total_classes(self):
        return sum(len(file.classes) for file in self.project.files)

    def total_functions(self):
        return sum(len(file.functions) for file in self.project.files)

    def total_methods(self):
        return sum(
            len(class_info.methods)
            for file in self.project.files
            for class_info in file.classes
        )

    def total_imports(self):
        return sum(len(file.imports) for file in self.project.files)

    def total_constants(self):
        return sum(len(file.constants) for file in self.project.files)

    def learning_order(self):

        files = self.project.files

        def complexity(file):

            class_count = len(file.classes)

            function_count = len(file.functions)

            method_count = sum(
                len(class_info.methods)
                for class_info in file.classes
            )

            return (
                class_count
                + function_count
                + method_count
            )

        ordered_files = sorted(
        files,
        key=complexity
        )

        return [
        file.name
        for file in ordered_files
        ]
    
    def largest_file(self):
        if not self.project.files:
            return None

        return max(
            self.project.files,
            key=lambda file: len(file.classes) + len(file.functions)
        )

    def dependency_graph(self):
        project_modules = {
            file.name.replace(".py", "")
            for file in self.project.files
        }

        graph = {}

        for file in self.project.files:
            dependencies = []

        for imported in file.imports:

            module_name = imported.split(".")[0]

            if module_name in project_modules:
                dependencies.append(f"{module_name}.py")

        graph[file.name] = dependencies

        return graph
    
    def find_entry_point(self):

        for python_file in self.project.files:

            if python_file.has_entry_point:
                return python_file.name

        return None

    def summary(self):

        print("\nPROJECT SUMMARY")
        print("-" * 40)

        print(f"Python Files : {self.total_files()}")
        print(f"Imports      : {self.total_imports()}")
        print(f"Constants    : {self.total_constants()}")
        print(f"Classes      : {self.total_classes()}")
        print(f"Methods      : {self.total_methods()}")
        print(f"Functions    : {self.total_functions()}")

        largest = self.largest_file()

        if largest:
            print(f"Largest File : {largest.name}")

    def display_call_graph(self):
        self.call_graph.display()
    
    def get_calls(self, function_name):
        return self.call_graph.get_calls(function_name)