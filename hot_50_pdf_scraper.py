from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import argparse
import re
import pandas as pd


def obtain_args():
    '''
    Establish Command Line Arguments

    Returns:
        - args (class): Arguments given.
    
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--infile', type=argparse.FileType('r', encoding='UTF-8'), required=True, help="The name of the PDF outlook table you would like to read.")
    parser.add_argument('-c', '--create', required=True, help="What you would like the output csv to be called.")
    args = parser.parse_args()
    
    return args

def convert_pdf_to_txt(path):
    '''
    Returns text of inputted pdf.

    Input:
        - path (str): String of the pdf file path.

    Returns:
        - text (str): String of text within the pdf file.
    '''
    # Instantiate necessary objects
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams(all_texts=True, detect_vertical=False, 
                      line_overlap=0.5, char_margin=1000.0,
                      line_margin=0.5, word_margin=2,
                      boxes_flow=1)
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    # Read in PDF
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

def process_pdf_text(text):
    '''
    Takes in text from pdf documents and returns the columns as lists.

    Input:
        - text (str): The pdf as a string.

    Returns:
        - professions (list): A list containing the pdf professions.
        - annual_openings (list): A list containing the pdf annual openings of professions.
        - growth (list): A list containing the pdf projected growth of professions.
        - wages (list): A list containing the pdf of hourly wages of professions.
        - background (list): A list containing the pdf background necessary for professions.
    '''

    # Instantiate regex pattern
    pattern = r'\n{2}([A-Za-z\s&,-.]+)\s*(\d+\,?\d*)\s*(\d+\.?\d*)%\s*(\$\d+–\$\d+)\s*(.*)'
    matches = re.findall(pattern, text)
    
    # Create lists
    professions = [item[0].replace('&', 'and').strip() for item in matches]
    annual_openings = [item[1].replace(',', '').strip() for item in matches]
    growth = [item[2].strip() for item in matches]
    wages = [item[3].replace("–", "-").strip() for item in matches]
    backgrounds = [item[4].strip() for item in matches]
    
    return professions, annual_openings, growth, wages, backgrounds
    
if __name__ == '__main__':
    args = obtain_args()
    text = convert_pdf_to_txt(args.infile.name)
    args.infile.close()
    professions, annual_openings, growth, wages, backgrounds = process_pdf_text(text)

    # All lists maintain the same indices to create a dataframe
    df = pd.DataFrame({
        "Profession": professions,
        "Projected Annual Openings": annual_openings,
        "Projected Growth": growth,
        "Hourly Wage Range": wages,
        "Typical Education and Training": backgrounds
    })

    output_file = args.create if args.create.endswith('.csv') else args.create + ".csv"
    df.to_csv("Outputs\\" + output_file)