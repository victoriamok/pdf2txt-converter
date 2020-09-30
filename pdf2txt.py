import getopt, io, os, sys
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams


def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    laparams = LAParams(all_texts=True)
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager,
                              fake_file_handle,
                              laparams=laparams)
    page_interpreter = PDFPageInterpreter(resource_manager,
                                          converter)
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    converter.close()
    if text:
        return text


def convert_multiple(pdf_dir, txt_dir):
    if pdf_dir == '':
        pdf_dir = os.getcwd() + '\\'
    for pdf in os.listdir(pdf_dir):
        file_ext = pdf.split('.')[-1]
        if file_ext == 'pdf':
            pdf_filename = pdf_dir + pdf
            text = extract_text_from_pdf(pdf_filename)
            text_filename = txt_dir + pdf + '.txt'
            with io.open(text_filename, 'w', encoding='utf-8') as text_file:
                text_file.write(str(text))


def main(argv):
    pdf_dir = '/your/path/to/pdf/files/'
    txt_dir = '/your/path/to/txt/files/'
    try:
        opts, args = getopt.getopt(argv, 'ip:t:')
    except getopt.GetoptError:
        print('pdf2txt.py -p <pdfdirectory> -t <textdirectory>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-i':
            print('pdf2txt.py -p <pdfdirectory> -t <textdirectory>')
            sys.exit()
        elif opt == '-p':
            pdf_dir = arg
        elif opt == '-t':
            txt_dir = arg
    convert_multiple(pdf_dir, txt_dir)


if __name__ == '__main__':
    main(sys.argv[1:])
