#!/bin/bash
# Script to process all PDFs in the pdfs/ folder

# Check if pdfs folder exists
if [ ! -d "pdfs" ]; then
    echo "Error: 'pdfs' folder not found!"
    exit 1
fi

# Detect Python from virtual environment
# Windows (Git Bash, MSYS, etc.)
if [ -f "venv/Scripts/python.exe" ]; then
    PYTHON_CMD="venv/Scripts/python.exe"
# Linux/Mac
elif [ -f "venv/bin/python" ]; then
    PYTHON_CMD="venv/bin/python"
# Fallback to system Python
else
    PYTHON_CMD="python"
fi

# Process each PDF in the folder
for pdf_file in pdfs/*.pdf; do
    # Check if there are PDF files
    if [ ! -f "$pdf_file" ]; then
        echo "No PDF files found in pdfs/ folder"
        exit 0
    fi
    
    echo "=========================================="
    echo "Processing: $(basename "$pdf_file")"
    echo "=========================================="
    
    "$PYTHON_CMD" extract_invoice.py "$pdf_file"
    
    # Add a blank line between results
    echo ""
done

echo "Processing completed!"

