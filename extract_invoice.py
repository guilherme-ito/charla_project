"""Main script for extracting invoice data from PDF files.

This script orchestrates the invoice extraction process by using
services to extract and format invoice data from PDF files.
"""

import asyncio
import json
import sys
from datetime import date
from pathlib import Path

from config import get_settings
from services import create_extraction_agent, extract_invoice_data
from utils import format_cnpj_or_cpf, format_currency


async def main() -> None:
    """Main function to run the invoice extraction.

    Reads PDF path from command line argument, extracts data,
    and prints JSON output to console.
    """
    if len(sys.argv) < 2:
        print("Usage: python extract_invoice.py <pdf_path>", file=sys.stderr)
        sys.exit(1)

    pdf_path = Path(sys.argv[1])
    settings = get_settings()
    agent = create_extraction_agent(settings.groq_api_key)

    try:
        invoice_data = await extract_invoice_data(pdf_path, agent)
        # Output as JSON to console
        data_dict = invoice_data.model_dump()

        # Format data for display
        # Convert date to ISO format string for JSON serialization
        if "data_emissao" in data_dict and isinstance(
            data_dict["data_emissao"], date
        ):
            data_dict["data_emissao"] = data_dict["data_emissao"].isoformat()

        # Format CNPJ/CPF fields
        if "cnpj_prestador" in data_dict:
            data_dict["cnpj_prestador"] = format_cnpj_or_cpf(
                data_dict["cnpj_prestador"]
            )
        if "cnpj_destinatario" in data_dict:
            data_dict["cnpj_destinatario"] = format_cnpj_or_cpf(
                data_dict["cnpj_destinatario"]
            )

        # Format currency fields
        if "valor_servico" in data_dict:
            data_dict["valor_servico"] = format_currency(data_dict["valor_servico"])
        if "valor_total" in data_dict:
            data_dict["valor_total"] = format_currency(data_dict["valor_total"])
        if "valor_impostos" in data_dict:
            data_dict["valor_impostos"] = format_currency(
                data_dict["valor_impostos"]
            )

        print(json.dumps(data_dict, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
