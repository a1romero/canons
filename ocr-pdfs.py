from PIL import Image
import pytesseract
import pandas as pd
from pandas import DataFrame as df

# Set the path to local tesseract instance
# be sure to download the tesseract instance from the tesseract website
def Start():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    return

def toc_text(img):
    return pytesseract.image_to_string(img, config=r'--psm 6')

def plaintext(img):
    return pytesseract.image_to_string(img)

def toc_dataframe(img, filename):
    todata=pytesseract.image_to_data(img)

    writefile = open(r'{}'.format(todata))
    writefile.write(todata)
    writefile.close()
    