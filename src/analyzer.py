from models import Project


class ProjectAnalyzer:

    def __init__(self, project: Project):
        self.project = project

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