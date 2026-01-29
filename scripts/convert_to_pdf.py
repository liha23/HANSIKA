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
    """
    Convert DOCX report to PDF using available tools.
    
    Returns:
        bool: True if conversion succeeded, False otherwise
    """
    docx_file = "Employee Payroll Management System - Project Report.docx"
    pdf_file = "Employee Payroll Management System - Project Report.pdf"
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(script_dir)
    docx_path = os.path.join(parent_dir, "docs", docx_file)
    pdf_path = os.path.join(parent_dir, "docs", pdf_file)
    
    if not os.path.exists(docx_path):
        print(f"Error: {docx_file} not found at {docx_path}!")
        print(f"Please run this script from the repository root or ensure the docs folder exists.")
        return False
    
    system = platform.system()
    
    if system == "Windows":
        try:
            from docx2pdf import convert
            print(f"Converting {docx_file} to PDF...")
            convert(docx_path, pdf_path)
            print(f"✓ Successfully created {pdf_file}")
            return True
        except ImportError:
            print("Error: docx2pdf module not found. Install it with: pip install docx2pdf")
            return False
        except OSError as e:
            print(f"Error: File operation failed - {e}")
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
                    [cmd, "--headless", "--convert-to", "pdf", "--outdir", 
                     os.path.dirname(pdf_path), docx_path],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                if result.returncode == 0:
                    print(f"✓ Successfully created {pdf_file}")
                    return True
                else:
                    print(f"LibreOffice exited with code {result.returncode}")
                    if result.stderr:
                        print(f"Error: {result.stderr}")
            except FileNotFoundError:
                continue
            except subprocess.TimeoutExpired:
                print(f"Warning: {cmd} timed out after 60 seconds")
                continue
            except OSError as e:
                print(f"Error running {cmd}: {e}")
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
