from pypdf import PdfReader, PdfWriter

inputpdf = PdfReader(open("./data/device_fault_codes.pdf", "rb"))

len = len(inputpdf.pages)


for i in range(len):
    outputpdf = PdfWriter()
    outputpdf.add_page(inputpdf.pages[i])
    outputpdf.write(open("./data/output/output"+str(i)+".pdf", "wb"))
