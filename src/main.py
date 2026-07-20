from scanner import FileScanner
from parser import PythonParser
from models import Project
from analyzer import ProjectAnalyzer

def display_project(project: Project):

    print("\n" + "=" * 60)
    print("PROJECT ANALYSIS")
    print("=" * 60)

    for python_file in project.files:

        print(f"\n📄 File: {python_file.name}")

        # -------------------------
        # Imports
        # -------------------------
        print("\nImports:")

        if python_file.imports:
            for module in python_file.imports:
                print(f"  • {module}")
        else:
            print("  None")

        # -------------------------
        # Constants
        # -------------------------
        print("\nConstants:")

        if python_file.constants:
            for constant in python_file.constants:
                print(f"  • {constant}")
        else:
            print("  None")

        # -------------------------
        # Classes
        # -------------------------
        print("\nClasses:")

        if python_file.classes:

            for class_info in python_file.classes:

                print(f"\n  {class_info.name}")

                if class_info.parent_classes:
                    print(
                        f"    Parent Classes: {', '.join(class_info.parent_classes)}"
                    )

                if class_info.docstring:
                    print(f"    Docstring: {class_info.docstring}")

                print("    Methods:")

                if class_info.methods:

                    for method in class_info.methods:

                        parameters = ", ".join(method.parameters)

                        print(f"      • {method.name}({parameters})")

                        if method.decorators:
                            print(
                                f"        Decorators: {', '.join(method.decorators)}"
                            )

                        if method.return_type:
                            print(
                                f"        Returns: {method.return_type}"
                            )

                        if method.docstring:
                            print(
                                f"        Docstring: {method.docstring}"
                            )

                else:
                    print("      None")

        else:
            print("  None")

        # -------------------------
        # Functions
        # -------------------------
        print("\nFunctions:")

        if python_file.functions:

            for function in python_file.functions:

                parameters = ", ".join(function.parameters)

                print(f"  • {function.name}({parameters})")

                if function.decorators:
                    print(
                        f"    Decorators: {', '.join(function.decorators)}"
                    )

                if function.return_type:
                    print(
                        f"    Returns: {function.return_type}"
                    )

                if function.docstring:
                    print(
                        f"    Docstring: {function.docstring}"
                    )

        else:
            print("  None")

def display_dependency_graph(graph):

    print("\n" + "=" * 60)
    print("DEPENDENCY GRAPH")
    print("=" * 60)

    for file, dependencies in graph.items():

        print(f"\n{file}")

        if dependencies:

            for dependency in dependencies:
                print(f"  └── {dependency}")

        else:
            print("  └── No internal dependencies")

def display_learning_order(order):

    print("\n" + "=" * 60)
    print("LEARNING ORDER")
    print("=" * 60)

    for index, file in enumerate(order, start=1):

        print(f"{index}. {file}")

def display_symbol_search(result):

    print("\n" + "=" * 60)
    print("SYMBOL SEARCH RESULT")
    print("=" * 60)


    if result is None:

        print("Symbol not found.")
        return


    if isinstance(result, list):

        for item in result:

            print("\nSymbol:")
            print(item["symbol"])

            print(
                "Type:",
                item["information"]["type"]
            )

            print(
                "File:",
                item["information"]["file"]
            )

        return


    print("Name:", result["name"])
    print("Type:", result["type"])
    print("File:", result["file"])

    if result["parent"]:

        print(
            "Class:",
            result["parent"]
        )

def main():

    scanner = FileScanner("sample_projects")
    parser = PythonParser()

    project = Project()

    files = scanner.scan()

    for file in files:
        project.files.append(parser.parse(file))

    display_project(project)

    analyzer = ProjectAnalyzer(project)

    analyzer.summary()
    entry_point = analyzer.find_entry_point()

    print("\n" + "=" * 60)
    print("ENTRY POINT")
    print("=" * 60)

    if entry_point:
        print(entry_point)
    else:
        print("No entry point detected.")
    dependency_graph = analyzer.dependency_graph()

    display_dependency_graph(dependency_graph)

    learning_order = analyzer.learning_order()

    display_learning_order(learning_order)

    analyzer.display_symbol_table()
    analyzer.display_call_graph()

    search_result = analyzer.find_symbol(
    "PhysicsEngine"
    )

    display_symbol_search(search_result)

if __name__ == "__main__":
    main()