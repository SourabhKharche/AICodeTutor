# AI Code Tutor

AI Code Tutor is a beginner-friendly Python learning assistant that helps students understand and learn from existing Python projects.

Instead of only displaying code, AI Code Tutor analyzes a project, understands its structure, and transforms it into an interactive learning experience.

The goal is to help students answer questions like:

- What does this file do?
- How are different parts of the program connected?
- What should I learn first?
- Why was this code written this way?

---

# Features

## Automatic Project Analysis

AI Code Tutor scans Python projects and extracts:

- Python files
- Imports
- Constants
- Classes
- Methods
- Functions
- Entry points

Example:

```
physics.py

Class:
    PhysicsEngine

Methods:
    __init__()
    apply_gravity()
    update_position()
    simulate()


Functions:
    distance()
    detect_collision()
    clamp()
```

---

# Code Explorer

Students can explore the codebase without manually searching through files.

The Code Explorer provides:

- Class browsing
- Function browsing
- Method browsing
- Documentation display
- Source code viewing

This allows beginners to understand code one piece at a time.

---

# Project Understanding

AI Code Tutor creates a structured view of the project:

- Project statistics
- File relationships
- Code organization
- Symbol information

Students can quickly understand the overall architecture of unfamiliar projects.

---

# Dependency and Call Graphs

The application generates visual graphs showing relationships between code components.

Students can understand:

- Which functions call each other
- How classes interact
- How information flows through the program

---

# Learning Mode

AI Code Tutor creates a recommended learning order based on the analyzed project.

Example:

```
Recommended Learning Order:

1. Understand Python functions
2. Learn classes and objects
3. Study PhysicsEngine
4. Understand the simulation loop
5. Explore collision detection
```

The learning path is created from the actual project structure.

---

# AI Tutor

With Google Gemini integration enabled, students can ask questions about the code.

Examples:

```
Why does this class exist?
```

```
Explain this function like I am a beginner.
```

```
How does the player object interact with physics?
```

The AI uses project context to provide explanations.

---

# Project Architecture

```
AI Code Tutor

src/

├── scanner.py
│   └── Finds Python files inside projects
│
├── parser.py
│   └── Extracts Python structure using AST
│
├── models.py
│   └── Stores project information
│
├── analyzer.py
│   └── Performs project analysis
│
├── symbol_table.py
│   └── Stores searchable code elements
│
├── call_graph.py
│   └── Creates function relationships
│
├── context_builder.py
│   └── Creates AI learning context
│
├── ai_service.py
│   └── Handles AI communication
│
├── learning_builder.py
│   └── Creates learning paths
│
├── github_importer.py
│   └── Imports GitHub repositories
│
├── ui.py
│   └── Main Streamlit application
│


components/

├── project_view.py
│   └── Displays project information
│
├── code_explorer.py
│   └── Code browsing interface
│
├── ai_panel.py
│   └── AI explanation interface
│
├── learning_panel.py
│   └── Learning mode interface
│
└── graph_panel.py
    └── Graph visualization interface
```

---

# 🛠️ Technologies Used

## Programming Language

- Python

## User Interface

- Streamlit

## Code Analysis

- Python AST Module

## Visualization

- PyVis

## Artificial Intelligence

- Google Gemini API

## Version Control

- Git

---

# Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd AICodeTutor
```

---

## 2. Create Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

---

# AI Configuration

AI features require an Google Gemini API key.

Create a file named:

```
.env
```

in the project root.

Add:

```env
GEMINI_API_KEY = api_key_here
```

If no API key is provided:

- Project analysis still works
- Code exploration still works
- Graph visualization still works
- AI explanations are disabled

---

# Running the Application

Start the Streamlit application:

```bash
streamlit run src/ui.py
```

The application will open in your browser.

---

# How Students Use AI Code Tutor

## Step 1

Select a Python project.

---

## Step 2

Run project analysis.

The tool discovers:

- Files
- Classes
- Functions
- Relationships

---

## Step 3

Explore the project.

Students can browse:

- Project structure
- Individual functions
- Classes
- Source code

---

## Step 4

Learn with AI.

Students can:

- Ask questions
- Request explanations
- Understand programming concepts

---

# Problem This Project Solves

Many beginners struggle when reading real-world software because:

- Projects contain many files
- Code lacks explanations
- Program flow is difficult to follow
- Documentation may be missing

AI Code Tutor transforms complex codebases into guided learning experiences.

---

# Future Improvements

Possible future features:

- Interactive debugging lessons
- Code execution visualization
- Support for more programming languages
- AI-generated quizzes
- Student progress tracking
- Personalized learning paths
- Classroom integration

---

# Author

**Sourabh Kharche**

Project:

**AI Code Tutor**

---

# License
This project is created for educational purposes.