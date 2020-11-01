import PyPDF2

pdf_file = open("Lab.pdf", 'rb') #Enter the pdf file name
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
pdf_writer = PyPDF2.PdfFileWriter()

for page_num in range(pdf_reader.numPages):
    pdf_writer.addPage(pdf_reader.getPage(page_num))

pdf_writer.encrypt("password") #Enter the password of the pdf File

result_pdf = open("encryptedfile.pdf", 'wb') #name the encrypted file
pdf_writer.write(result_pdf)
result_pdf.close()