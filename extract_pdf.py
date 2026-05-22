import pypdf

reader = pypdf.PdfReader("Aanav Profile English.pdf")
print(f"Total pages: {len(reader.pages)}")

with open("pdf_content.txt", "w", encoding="utf-8") as f:
    for i, page in enumerate(reader.pages):
        f.write(f"--- PAGE {i+1} ---\n")
        f.write(page.extract_text() or "")
        f.write("\n\n")

print("Done! Extracted text to pdf_content.txt")
