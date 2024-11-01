import pytesseract
import fitz
from PIL import Image
import pandas as pd
from pandas import DataFrame as df
from io import StringIO
from pathlib import Path
import csv
import re

def pdf_to_data(pdf_path: str, output_folder: str, tesseract_path: str, include_pngs= False):
    '''Chop a given PDF into individual pages, then convert each PDF into an image (saved to the pngs folder). Convert OCR data about each page into a .csv.
        This function requires that you have a folder in the same level as your pdf for outputs, and then two folders within that folder titled 'pngs' and 'tsv_data'.
        For example:
            your pdf
            output folder
                pngs ** Only necessary if you want to see the processed pages-- set include_pngs to True'''
    
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    open_pdf = fitz.open(pdf_path)

    sum_string = ''
    tsv_total = pd.DataFrame()
    for page_num in range(open_pdf.page_count): # iterate through individual pages
        page = open_pdf[page_num]

        img = page.get_pixmap()
        

        # make the image
        pil_img = Image.frombytes("RGB", [img.width, img.height], img.samples) # convert to PIL Image
        # improve resolution
        scale_factor = 3 # try changing this to improve resolution
        new_size = img.width * scale_factor, img.height * scale_factor
        resize = pil_img.resize(new_size, Image.LANCZOS)
        

        # process image into tsv and clean some values
        png_to_data = pytesseract.image_to_data(resize, config = r'--psm 6') 
        data_to_tsv = StringIO(png_to_data)
        data_read = pd.read_csv(data_to_tsv, sep='\t', quoting=csv.QUOTE_NONE)
        tsv_clean = data_read[['line_num', 'word_num', 'left', 'top', 'text', 'conf']]
        tsv_total = pd.concat([tsv_total, tsv_clean])

        img_to_string = pytesseract.image_to_string(resize, config = r'--psm 6', lang = 'en')
        sum_string += img_to_string
        
        if include_pngs:
            output_png_path = Path(f"{output_folder}/pngs/page_{page_num + 1}.png")
            resize.save(output_png_path)

    output_tsv_total = Path(f"{output_folder}/location.csv")
    tsv_total.to_csv(output_tsv_total, sep= ',', index=False)
    output_str_path = Path(f"{output_folder}/str_data.txt")
    with open(output_str_path, 'w') as file:
        file.write(sum_string)
    print("Done!")