import PyPDF2
pdfFileObj = open('example_pdf.pdf', 'rb') # Read in binary mode as we write in binary mode
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0) # The first page is 0 and the second 1 PyPDF2 uses a zero-based index for getting pages

print(pageObj.extractText())