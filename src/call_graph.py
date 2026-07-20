import ast


class CallGraph:

    def __init__(self):

        self.graph = {}


    def add_call(self, caller, called):

        if caller not in self.graph:

            self.graph[caller] = []


        if called not in self.graph[caller]:

            self.graph[caller].append(called)


    def analyze_function(
        self,
        node,
        function_name,
        class_name=None
    ):

        if class_name:

            caller_name = f"{class_name}.{function_name}"

        else:

            caller_name = function_name


        for child in ast.walk(node):

            if isinstance(child, ast.Call):

                called_name = None


                # Normal function call
                if isinstance(child.func, ast.Name):

                    called_name = child.func.id


                # Method call
                elif isinstance(child.func, ast.Attribute):

                    called_name = child.func.attr


                if called_name:

                    if class_name:

                        # Assume internal class calls
                        self.add_call(
                            caller_name,
                            f"{class_name}.{called_name}"
                        )

                    else:

                        self.add_call(
                            caller_name,
                            called_name
                        )


    def build(self, project):

        for python_file in project.files:

            tree = python_file.tree


            for node in ast.walk(tree):


                # Standalone functions

                if isinstance(node, ast.FunctionDef):

                    self.analyze_function(
                        node,
                        node.name
                    )


                # Classes

                if isinstance(node, ast.ClassDef):

                    for child in node.body:

                        if isinstance(
                            child,
                            ast.FunctionDef
                        ):

                            self.analyze_function(
                                child,
                                child.name,
                                node.name
                            )


        return self.graph


    def get_calls(self, function_name):

        return self.graph.get(
            function_name,
            []
        )


    def display(self):

        print("\n" + "=" * 60)
        print("CALL GRAPH")
        print("=" * 60)


        for caller, calls in self.graph.items():

            print(f"\n{caller}")


            if calls:

                for call in calls:

                    print(
                        f"  └── {call}"
                    )

            else:

                print(
                    "  └── No calls"
                )