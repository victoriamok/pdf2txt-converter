# PDF-TXT-converter

Small and simple pdf-to-txt converter based on the pdfminer package. 

## Requirements

Python (3.6 or above) \
[PDFMiner](https://pypi.org/project/pdfminer/) 

## How to use:

**1. Clone the repository**
```
git clone https://github.com/victoriamok/pdf2txt-converter.git
```
**2. Create a virtual environment (for MacOS or Linux)**
```
python3 -m venv <name_of_virtualenv>
```
Activate your virtual environment
```
source <name_of_virtualenv>/bin/activate
```
**3. Install the required packages**
```
cd <name_of_virtualenv>
pip3 install -r requirements.txt
```
**4. Set the pdf source and output path**
```
pdf_dir = '/your/path/to/pdf/files/'
txt_dir = '/your/path/to/txt/files/'
```
**4. Run the script**
```
python3 pdf2txt.py 
```
