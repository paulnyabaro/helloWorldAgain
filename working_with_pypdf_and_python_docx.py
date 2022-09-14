import PyPDF2
pdfFileObj = open('example_pdf.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)