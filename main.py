from PyPDF2 import PdfFileWriter, PdfFileReader
from os import listdir, path, makedirs


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


if not path.exists('output'):
    makedirs('output')
if not path.exists('input'):
    makedirs('input')

input_names_list = listdir("input")
# input_name_path_list = [f"input/{file_name}" for file_name in listdir("input")]
wmarks = [f"watermarks/{file_name}" for file_name in listdir("watermarks")]
outs = [f"output/{file_name}" for file_name in listdir("watermarks")]

for input in input_names_list:
    for wmark, out in zip(wmarks, outs):
        print('Adding watermark to ' + out + ' ' + input)
        create_watermark(
            input_pdf=f'input/{input}',
            output=f'{out} {input}',
            watermark=wmark
        )
print("Done")
