import docx
doc = docx.Document('example_doc.docx')
print(len(doc.paragraphs))
print(doc.paragraphs[0].text)