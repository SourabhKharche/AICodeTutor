"""
ai_service.py

Handles communication with AI models.

Responsibilities:
- Connect to OpenAI API
- Send prompts
- Return AI responses
- Handle missing configuration safely

Author:
Sourabh Kharche

Project:
AI Code Tutor
"""


import os

from dotenv import load_dotenv
from openai import OpenAI



# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()



# ==========================================================
# AI Service
# ==========================================================


class AIService:
    """
    Handles AI requests.

    The service can run in disabled mode
    when no API key is available.
    """



    def __init__(self):
        """
        Creates AI client if API key exists.
        """


        self.client = None

        self.enabled = False



        api_key = os.getenv(
            "OPENAI_API_KEY"
        )



        # ----------------------------------------------
        # Create client only if key exists
        # ----------------------------------------------

        if api_key:


            self.client = OpenAI(
                api_key=api_key
            )


            self.enabled = True



    # ======================================================
    # Ask AI
    # ======================================================


    def ask(self, prompt):
        """
        Sends a prompt to AI.

        Returns:
            AI response or fallback message.
        """



        # ----------------------------------------------
        # Check availability
        # ----------------------------------------------

        if not self.enabled:


            return (
                "AI features are currently unavailable.\n\n"
                "Add OPENAI_API_KEY to your .env file "
                "to enable AI explanations."
            )



        # ----------------------------------------------
        # Send request
        # ----------------------------------------------

        try:


            response = (
                self.client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )
            )



            return (
                response
                .choices[0]
                .message
                .content
            )



        except Exception as error:


            return (
                "AI request failed.\n\n"
                f"Error: {error}"
            )