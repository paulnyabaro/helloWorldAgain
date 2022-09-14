import docx
doc = docx.Document('example_doc.docx')
print(len(doc.paragraphs))