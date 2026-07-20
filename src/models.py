from dataclasses import dataclass, field


@dataclass
class FunctionInfo:
    """
    Represents either a standalone function
    or a class method.
    """

    name: str

    parameters: list[str] = field(default_factory=list)

    decorators: list[str] = field(default_factory=list)

    return_type: str = ""

    docstring: str = ""


@dataclass
class ClassInfo:
    """
    Represents a Python class.
    """

    name: str

    parent_classes: list[str] = field(default_factory=list)

    methods: list[FunctionInfo] = field(default_factory=list)

    docstring: str = ""


@dataclass
class PythonFile:

    name: str
    path: str

    imports: list[str] = field(default_factory=list)

    constants: list[str] = field(default_factory=list)

    classes: list[ClassInfo] = field(default_factory=list)

    functions: list[FunctionInfo] = field(default_factory=list)

    has_entry_point: bool = False

    tree: object = None


@dataclass
class Project:
    """
    Represents an entire parsed Python project.
    """

    files: list[PythonFile] = field(default_factory=list)