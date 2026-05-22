import sys

try:
    import docx
    print("docx installed")
except ImportError:
    print("docx NOT installed")

try:
    import pypdf
    print("pypdf installed")
except ImportError:
    print("pypdf NOT installed")

try:
    import pdfplumber
    print("pdfplumber installed")
except ImportError:
    print("pdfplumber NOT installed")

try:
    import fitz # PyMuPDF
    print("pymupdf installed")
except ImportError:
    print("pymupdf NOT installed")
