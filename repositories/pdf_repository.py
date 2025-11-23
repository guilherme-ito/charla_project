"""Repository for PDF file operations.

This module handles reading and extracting text from PDF files.
"""

from pathlib import Path

import pdfplumber


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract text content from PDF file using pdfplumber.

    Args:
        pdf_path: Path to the PDF invoice file.

    Returns:
        Extracted text content from all pages.

    Raises:
        FileNotFoundError: If PDF file doesn't exist.
        ValueError: If PDF reading fails.
    """
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    try:
        text_parts = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_parts.append(page_text)
        return "\n\n".join(text_parts)
    except Exception as e:
        raise ValueError(
            f"Error reading PDF file: {str(e)}"
        ) from e

