import ast
from pathlib import Path

from models import PythonFile, ClassInfo, FunctionInfo


class PythonParser:

    def parse(self, filepath):
        path = Path(filepath)

        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)

        python_file = PythonFile(
            name = filepath.name,
            path = filepath
        )

        python_file.tree = tree

        for node in tree.body:
            # -------------------------
            # Entry Point
            # -------------------------
            if isinstance(node, ast.If):

                test = node.test

                if (
                    isinstance(test, ast.Compare)
                    and isinstance(test.left, ast.Name)
                    and test.left.id == "__name__"
                    and len(test.ops) == 1
                    and isinstance(test.ops[0], ast.Eq)
                    and len(test.comparators) == 1
                    and isinstance(test.comparators[0], ast.Constant)
                    and test.comparators[0].value == "__main__"
                ):
                    python_file.has_entry_point = True

            # -------------------------
            # import math
            # -------------------------
            if isinstance(node, ast.Import):

                for alias in node.names:
                    python_file.imports.append(alias.name)

            # -------------------------
            # from math import sqrt
            # -------------------------
            elif isinstance(node, ast.ImportFrom):

                module = node.module or ""

                for alias in node.names:
                    python_file.imports.append(f"{module}.{alias.name}")

            # -------------------------
            # Constants
            # Example:
            # GRAVITY = 9.81
            # -------------------------
            elif isinstance(node, ast.Assign):

                for target in node.targets:

                    if isinstance(target, ast.Name):

                        if target.id.isupper():
                            python_file.constants.append(target.id)

            # -------------------------
            # Classes
            # -------------------------
            elif isinstance(node, ast.ClassDef):

                parent_classes = []

                for base in node.bases:

                    if isinstance(base, ast.Name):
                        parent_classes.append(base.id)

                    elif isinstance(base, ast.Attribute):
                        parent_classes.append(base.attr)

                class_info = ClassInfo(
                    name=node.name,
                    parent_classes=parent_classes,
                    docstring=ast.get_docstring(node) or ""
                )

                for item in node.body:

                    if isinstance(item, ast.FunctionDef):

                        parameters = [
                            arg.arg
                            for arg in item.args.args
                        ]

                        decorators = []

                        for decorator in item.decorator_list:

                            if isinstance(decorator, ast.Name):
                                decorators.append(decorator.id)

                            elif isinstance(decorator, ast.Attribute):
                                decorators.append(decorator.attr)

                        return_type = ""

                        if item.returns:

                            if isinstance(item.returns, ast.Name):
                                return_type = item.returns.id

                            elif isinstance(item.returns, ast.Constant):
                                return_type = str(item.returns.value)

                        method = FunctionInfo(
                            name=item.name,
                            parameters=parameters,
                            decorators=decorators,
                            return_type=return_type,
                            docstring=ast.get_docstring(item) or ""
                        )

                        class_info.methods.append(method)

                python_file.classes.append(class_info)

            # -------------------------
            # Standalone functions
            # -------------------------
            elif isinstance(node, ast.FunctionDef):

                parameters = [
                    arg.arg
                    for arg in node.args.args
                ]

                decorators = []

                for decorator in node.decorator_list:

                    if isinstance(decorator, ast.Name):
                        decorators.append(decorator.id)

                    elif isinstance(decorator, ast.Attribute):
                        decorators.append(decorator.attr)

                return_type = ""

                if node.returns:

                    if isinstance(node.returns, ast.Name):
                        return_type = node.returns.id

                    elif isinstance(node.returns, ast.Constant):
                        return_type = str(node.returns.value)

                function = FunctionInfo(
                    name=node.name,
                    parameters=parameters,
                    decorators=decorators,
                    return_type=return_type,
                    docstring=ast.get_docstring(node) or ""
                )

                python_file.functions.append(function)

        return python_file