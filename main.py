# pdf_watermarker.py

from PyPDF2 import PdfFileWriter, PdfFileReader
from os import listdir

def create_watermark(input_pdf, output, watermark):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

file = 'input.pdf'

wmarks = [f"input/{file_name}" for file_name in listdir("input")]
outs = [f"output/{file_name}" for file_name in listdir("input")]

for wmark, out in zip(wmarks, outs):
    create_watermark(
        input_pdf= file,
        output= out,
        watermark= wmark
    )
