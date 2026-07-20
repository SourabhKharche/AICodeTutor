from scanner import FileScanner
from parser import PythonParser
from models import Project


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


def main():

    scanner = FileScanner("sample_projects")
    parser = PythonParser()

    project = Project()

    files = scanner.scan()

    for file in files:
        project.files.append(parser.parse(file))

    display_project(project)


if __name__ == "__main__":
    main()