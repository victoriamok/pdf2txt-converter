import getopt, io, os, sys
import argparse
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.layout import LAParams


def extract_text_from_pdf(pdf_path):
    # Create PDF resource manager and parameters object
    resource_manager = PDFResourceManager()
    laparams = LAParams(all_texts=True)
    # Create a fake file handle and a text converter object
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager,
                              fake_file_handle,
                              laparams=laparams)
    # Create a PDF page interpreter object
    page_interpreter = PDFPageInterpreter(resource_manager,
                                          converter)
    with open(pdf_path, 'rb') as fh:
        # Iterate through PDF pages and process each page
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
        # Get text from the fake file handle
        text = fake_file_handle.getvalue()
    # Close the converter
    converter.close()
    # Return the extracted text
    return text if text else None


def convert_multiple(pdf_dir, txt_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(txt_dir, exist_ok=True)  
    # Iterate through PDF files in the input directory
    for pdf in os.listdir(pdf_dir):
        # Check if the file has a .pdf extension
        if pdf.endswith('.pdf'):
            # Get the full path of the PDF file
            pdf_filename = os.path.join(pdf_dir, pdf)
            # Extract text from the PDF file
            text = extract_text_from_pdf(pdf_filename)
            # If text is extracted successfully
            if text is not None:
                # Original filename without extension
                filename = os.path.splitext(pdf)[0]  
                # Create the full path for the output text file
                text_filename = os.path.join(txt_dir, f"{filename}.txt")
                # Write the extracted text to the output text file
                with io.open(text_filename, 'w', encoding='utf-8') as text_file:
                    text_file.write(text)


def main():
    # Check if the number of command-line arguments is correct
    if len(sys.argv) != 3:
        print("Usage: python3 pdf2txt.py input_dir output_dir")
        sys.exit(1)

    # Extract input and output directories from command line arguments
    pdf_dir = sys.argv[1]
    txt_dir = sys.argv[2]
    
    # Convert PDF files to text
    convert_multiple(pdf_dir, txt_dir)


if __name__ == '__main__':
    main()
    