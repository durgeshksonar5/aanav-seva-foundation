import zipfile
import xml.etree.ElementTree as ET

def get_docx_text(path):
    """Simple parser for docx files using standard library."""
    try:
        with zipfile.ZipFile(path) as docx:
            xml_content = docx.read('word/document.xml')
            root = ET.fromstring(xml_content)
            
            # The namespace for docx elements
            namespaces = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            
            # Find all paragraph elements
            paragraphs = []
            for para in root.findall('.//w:p', namespaces):
                texts = [node.text for node in para.findall('.//w:t', namespaces) if node.text]
                if texts:
                    paragraphs.append("".join(texts))
            
            return "\n".join(paragraphs)
    except Exception as e:
        return f"Error: {e}"

text = get_docx_text("Aanav_Seva_Foundation_info.docx")
with open("docx_content.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Done extracting docx!")
