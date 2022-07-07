"""
Convert input jpg file into csv file with same shape

F:
convert_jpg_to_CSV(input_file_name); return csv
"""


# import required libraries
from PIL import Image
import numpy as gfg

def convert_jpg_to_CSV(input_file_name):
    # read an image and convert to graystyle
    img = Image.open(input_file_name).convert('L')
    
    # convert image object into array
    csv = gfg.asarray(img)
    
    return csv
def open_CSV(output_file_name):
    with open(output_file_name,"r") as f:

        
        Y_str = f.read().split(";")
        Y = list(map(int,Y_str))
    return Y
