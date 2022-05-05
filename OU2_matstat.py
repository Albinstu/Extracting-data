import numpy as np
import matplotlib.pyplot as plt
import re

file_path = '[you file path]/IceCube40StringData.txt'

def load_file(file_path):
    with open(file_path, 'r') as file:
        
        for line in file:
            if '#'*5 not in line:
                continue
            else:
                next(file, None)
                header = re.findall(r'[a-zA-z/]+', next(file, None))
                print(header)
                break

        next(file, None)
        pp = [list(map(float, re.findall(r'[0-9.]*[0-9]+', line))) for line in file]

        pp.pop(-1) #tar bort det sista värdet då det ej passar in, är dessutom antal sekunder på ett dygn
        return np.array(pp)


data = load_file(file_path)
# print(data)



        


        
            
