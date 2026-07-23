"""
ai_service.py

Handles communication with AI models.

Responsibilities:
- Connect to Gemini API
- Send prompts
- Return AI responses
- Handle missing configuration safely

Author: Sourabh Kharche
Project: AI Code Tutor
"""

import os
from dotenv import load_dotenv
from google import genai

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
            "GEMINI_API_KEY"
        )

        # ----------------------------------------------
        # Create client only if key exists
        # ----------------------------------------------
        if api_key:
            self.client = genai.Client(
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
                "Add GEMINI_API_KEY to your .env file "
                "to enable AI explanations."
            )

        # ----------------------------------------------
        # Send request
        # ----------------------------------------------
        try:
            response = (
                self.client.models.generate_content(
                    model="gemini-flash-latest",
                    contents=prompt
                )
            )

            return (
                response.text
            )

        except Exception as error:
            return (
                "AI request failed.\n\n"
                f"Error: {error}"
            )