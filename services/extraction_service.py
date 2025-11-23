"""Service layer for invoice data extraction.

This module contains the business logic for extracting invoice data
from PDF files using PydanticAI agents.
"""

import os
from pathlib import Path

from pydantic import ValidationError
from pydantic_ai import Agent
from pydantic_ai.exceptions import AgentRunError, ModelHTTPError
from pydantic_ai.models.groq import GroqModel

from config import EXTRACTION_SYSTEM_PROMPT, get_settings
from repositories import extract_text_from_pdf
from schemas import InvoiceData


def create_extraction_agent(api_key: str) -> Agent[InvoiceData]:
    """Create a PydanticAI agent for invoice extraction.

    Args:
        api_key: Groq API key for LLM access.

    Returns:
        Configured agent instance for invoice data extraction.
    """
    # Set API key as environment variable for GroqModel
    os.environ["GROQ_API_KEY"] = api_key
    model = GroqModel("llama-3.3-70b-versatile")
    agent = Agent(
        model,
        output_type=InvoiceData,
        system_prompt=EXTRACTION_SYSTEM_PROMPT,
    )
    return agent


async def extract_invoice_data(
    pdf_path: Path, agent: Agent[InvoiceData]
) -> InvoiceData:
    """Extract invoice data from a PDF file.

    First extracts text from PDF using pdfplumber, then uses PydanticAI
    agent to extract structured data from the text.

    Args:
        pdf_path: Path to the PDF invoice file.
        agent: Configured extraction agent.

    Returns:
        Extracted and validated invoice data.

    Raises:
        FileNotFoundError: If PDF file doesn't exist.
        ValueError: If extraction fails or data is invalid.
    """
    try:
        # Extract text from PDF first
        pdf_text = extract_text_from_pdf(pdf_path)

        if not pdf_text or len(pdf_text.strip()) < 50:
            raise ValueError(
                "Could not extract sufficient text from PDF. "
                "The file may be corrupted or be an image."
            )

        # Send extracted text to the agent for structured extraction
        result = await agent.run(pdf_text)
        return result.output
    except ValidationError as e:
        raise ValueError(
            f"Validation error for extracted data: {str(e)}"
        ) from e
    except ModelHTTPError as e:
        error_msg = str(e)
        # Detect rate limit and provide more useful message
        if "429" in error_msg or "rate_limit" in error_msg.lower():
            raise ValueError(
                f"Rate limit reached on Groq API. "
                f"Please wait a few minutes before trying again. "
                f"Error: {error_msg}"
            ) from e
        raise ValueError(
            f"Error communicating with Groq API: {error_msg}"
        ) from e
    except AgentRunError as e:
        raise ValueError(
            f"Error during agent execution: {str(e)}"
        ) from e
    except Exception as e:
        raise ValueError(
            f"Error extracting data from PDF: {str(e)}"
        ) from e

