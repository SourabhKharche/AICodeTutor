"""
ai_panel.py

Handles AI interaction UI.
Responsibilities:
- Explain selected code
- Ask questions about the project
- Display AI responses

Author: Sourabh Kharche
Project: AI Code Tutor
"""

import streamlit as st
from context_builder import ContextBuilder
from ai_service import AIService

# ==========================================================
# AI Panel
# ==========================================================
def render_ai_panel(
    project,
    results,
    selected_symbol
):
    """
    Displays AI tutor features.
    Parameters:
        project:
            Parsed project
        results:
            Analyzer output
        selected_symbol:
            Currently selected code element

    """
    st.header(
        "AI Code Tutor"
    )

    # ======================================================
    # Create Services
    # ======================================================
    context_builder = ContextBuilder()
    ai_service = AIService()

    if not ai_service.enabled:
        st.warning(
            "AI features disabled. "
            "Add GEMINI_API_KEY to enable explanations."
        )

    # ======================================================
    # Explain Code
    # ======================================================
    st.subheader(
        "Explain This Code"
    )

    if st.button(
        "Explain Selected Code"
    ):
        if selected_symbol is None:
            st.warning(
                "Please select code first."
            )

        else:
            with st.spinner(
                "Generating explanation..."
            ):

                context = (
                    context_builder
                    .build_symbol_context(
                        selected_symbol
                    )
                )

                prompt = f"""
                You are an expert programming tutor.

                Explain this code to a beginner.

                Please:
                - Describe what the code does.
                - Explain it step by step.
                - Define any programming concepts.
                - Mention any good programming practices used.
                - Suggest improvements if appropriate.
                - Format the response using Markdown headings and bullet points.

                {context}
                """

                explanation = (
                    ai_service.ask(
                        prompt
                    )
                )

            st.write(
                explanation
            )

    # ======================================================
    # Ask Question
    # ======================================================
    st.subheader(
        "Ask a Question"
    )

    question = st.text_input(
        "Ask about this project:"
    )

    if st.button(
        "Ask AI"
    ):
        if question:
            with st.spinner(
                "Thinking..."
            ):

                context = (
                    context_builder
                    .build_project_context(
                        project,
                        results
                    )
                )

                prompt = f"""
Project context:
{context}

Student question:
{question}

Explain using beginner-friendly language.
"""
                answer = (
                    ai_service.ask(
                        prompt
                    )
                )

            st.write(
                answer
            )

        else:
            st.warning(
                "Enter a question first."
            )