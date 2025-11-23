"""Script to process all PDFs in the pdfs/ folder.

This script processes all PDF files found in the pdfs/ folder
by calling extract_invoice.py for each one.
"""

import subprocess
import sys
from pathlib import Path


def main() -> None:
    """Main function to process all PDFs."""
    pdfs_dir = Path("pdfs")

    if not pdfs_dir.exists():
        print("Error: 'pdfs' folder not found!", file=sys.stderr)
        sys.exit(1)

    # Find all PDF files
    pdf_files = list(pdfs_dir.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in pdfs/ folder")
        sys.exit(0)

    print(f"Found {len(pdf_files)} PDF file(s) to process.\n", flush=True)

    # Process each PDF by calling extract_invoice.py
    for pdf_file in pdf_files:
        print("=" * 50, flush=True)
        print(f"Processing: {pdf_file.name}", flush=True)
        print("=" * 50, flush=True)

        try:
            # Call extract_invoice.py for each PDF
            # Direct stdout and stderr to maintain correct order
            subprocess.run(
                [sys.executable, "extract_invoice.py", str(pdf_file)],
                check=False,
                stdout=sys.stdout,
                stderr=sys.stderr,
            )
            print()  # Blank line between results
        except Exception as e:
            print(
                f"Error processing {pdf_file.name}: {str(e)}",
                file=sys.stderr,
                flush=True,
            )
            print()  # Blank line even on error

    print("Processing completed!")


if __name__ == "__main__":
    main()

