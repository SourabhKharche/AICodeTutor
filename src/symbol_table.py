class SymbolTable:

    def __init__(self):

        self.symbols = {}


    def add_symbol(
        self,
        name,
        symbol_type,
        file,
        parent=None
    ):

        if parent:

            full_name = f"{parent}.{name}"

        else:

            full_name = name


        self.symbols[full_name] = {
            "name": name,
            "type": symbol_type,
            "file": file,
            "parent": parent
        }


    def build(self, project):

        for python_file in project.files:


            # Classes
            for class_info in python_file.classes:

                self.add_symbol(
                    class_info.name,
                    "Class",
                    python_file.name
                )


                # Methods inside classes
                for method in class_info.methods:

                    self.add_symbol(
                        method.name,
                        "Method",
                        python_file.name,
                        class_info.name
                    )


            # Functions
            for function in python_file.functions:

                self.add_symbol(
                    function.name,
                    "Function",
                    python_file.name
                )


        return self.symbols


    def find(self, name):

        return self.symbols.get(name)


    def display(self):

        print("\n" + "=" * 60)
        print("SYMBOL TABLE")
        print("=" * 60)


        for symbol, information in self.symbols.items():

            print(f"\n{symbol}")

            print(
                f"  Type: {information['type']}"
            )

            print(
                f"  File: {information['file']}"
            )

            if information["parent"]:

                print(
                    f"  Class: {information['parent']}"
                )