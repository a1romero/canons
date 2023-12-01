import pytesseract as pyt
from PIL import Image
from traceback import print_exc as pe
import glob

def Connect():
    pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

NEW_DATA_PATH = 'data_unloaded'
LOADED_DATA_PATH = 'data_loaded'

def GetNewData():
    file_names=glob(os.path.join(NEW_DATA_PATH, FILE_NAME_PATTERN))
    print(file_names)
    return(file_names)

def FileToPlaintext(img):
    plaintext=pyt.image_to_string(img, config='--psm 6')
    return plaintext

def LoadData():
    