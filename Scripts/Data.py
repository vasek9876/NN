#debug
#import Convertor as cnv
#import Dataset as ds
#from Path import *

import Scripts.Convertor as cnv
import Scripts.Dataset as ds
from Scripts.Path import *


def read():
    #try
    file_input_path = path_to_sample_data + inputs + input_type
    file_output_path = path_to_sample_data + output + output_type
    try:
        X = [cnv.convert_jpg_to_CSV(file_input_path)]
        Y = [cnv.open_CSV(file_output_path)]
    except Exception as e:
        print("No data!", "\n",e)

    #run over 1000 sample data
    for n in range(999):
        file_input_path = path_to_sample_data + inputs +str(n) + input_type
        file_output_path = path_to_sample_data + output+str(n) + output_type
        try:
            x = cnv.convert_jpg_to_CSV(file_input_path)
            y = cnv.open_CSV(file_output_path)
            X,Y = ds.add_dataset(X,Y,x,y)
        except Exception as e:
            #print(e)
            break
    
    # random shuffle aplied on data
    X,Y = ds.shuffle(X,Y)

    return X,Y
