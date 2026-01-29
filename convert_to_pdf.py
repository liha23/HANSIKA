#!/usr/bin/env python3
"""
Script to convert the DOCX report to PDF.
Requires LibreOffice to be installed.

Usage:
    python convert_to_pdf.py

On Windows with LibreOffice installed:
    - The script will use LibreOffice to convert DOCX to PDF

On Linux with LibreOffice installed:
    - Run: libreoffice --headless --convert-to pdf "Employee Payroll Management System - Project Report.docx"
"""

import os
import sys
import subprocess
import platform

def convert_docx_to_pdf():
    docx_file = "Employee Payroll Management System - Project Report.docx"
    pdf_file = "Employee Payroll Management System - Project Report.pdf"
    
    if not os.path.exists(docx_file):
        print(f"Error: {docx_file} not found!")
        return False
    
    system = platform.system()
    
    if system == "Windows":
        try:
            from docx2pdf import convert
            print(f"Converting {docx_file} to PDF...")
            convert(docx_file, pdf_file)
            print(f"✓ Successfully created {pdf_file}")
            return True
        except ImportError:
            print("Error: docx2pdf module not found. Install it with: pip install docx2pdf")
            return False
        except Exception as e:
            print(f"Error during conversion: {e}")
            return False
    
    elif system == "Linux" or system == "Darwin":  # Linux or macOS
        # Try using LibreOffice
        libreoffice_commands = [
            "libreoffice",
            "soffice",
            "/Applications/LibreOffice.app/Contents/MacOS/soffice"  # macOS path
        ]
        
        for cmd in libreoffice_commands:
            try:
                result = subprocess.run(
                    [cmd, "--headless", "--convert-to", "pdf", docx_file],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                if result.returncode == 0:
                    print(f"✓ Successfully created {pdf_file}")
                    return True
            except (FileNotFoundError, subprocess.TimeoutExpired):
                continue
        
        print("Error: LibreOffice not found!")
        print("Install LibreOffice with:")
        if system == "Linux":
            print("  Ubuntu/Debian: sudo apt-get install libreoffice-writer")
            print("  Fedora: sudo dnf install libreoffice-writer")
        else:
            print("  macOS: brew install --cask libreoffice")
        return False
    
    else:
        print(f"Error: Unsupported operating system: {system}")
        return False

if __name__ == "__main__":
    success = convert_docx_to_pdf()
    sys.exit(0 if success else 1)
