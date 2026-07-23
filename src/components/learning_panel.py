"""
learning_panel.py

Displays project learning path.

Responsibilities:
- Generate learning roadmap
- Display concepts
- Explain recommended order

Author:
Sourabh Kharche

Project:
AI Code Tutor
"""


import streamlit as st



from learning_builder import LearningBuilder
from ai_service import AIService



# ==========================================================
# Learning Panel
# ==========================================================


def render_learning_panel(
    project,
    results
):
    """
    Displays learning mode.

    Parameters:

        project:
            Parsed project object

        results:
            Analyzer results

    """



    st.header(
        "📚 Learning Mode"
    )



    builder = LearningBuilder()

    ai_service = AIService()



    # ======================================================
    # Generate Learning Path
    # ======================================================


    if st.button(
        "Create Learning Path"
    ):


        with st.spinner(
            "Creating learning roadmap..."
        ):


            context = (
                builder.build_learning_context(
                    project,
                    results
                )
            )


            response = (
                ai_service.ask(
                    context
                )
            )


            st.session_state.learning_path = (
                response
            )



    # ======================================================
    # Display Result
    # ======================================================


    if (
        "learning_path"
        in st.session_state
    ):


        st.subheader(
            "Recommended Learning Order"
        )


        st.write(
            st.session_state.learning_path
        )


    else:


        st.info(
            "Generate a learning path to begin."
        )