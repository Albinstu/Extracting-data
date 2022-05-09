import numpy as np
import matplotlib.pyplot as plt
import re

file_path = '[your file path]/IceCube40StringData.txt'

def extract(file_path):
    with open(file_path, 'r') as file:
        
        for i in range(19):
            next(file, None)
            if i == 17:
                header = re.findall(r'[a-zA-z/]+', next(file, None))
                # print(header)

        pp = []
        a = list(map(int, re.findall(r'[0-9.]*[0-9]+', next(file))[6:8]))

        while True:
            b = list(map(int, re.findall(r'[0-9.]*[0-9]+', next(file))[6:8]))

            if b == [] or a == []:  #tar bort det sista värdet
                break
            
            
            if a[0] == b[0]:
                d = abs(a[1] - b[1])
                pp.append(d)
                
            else:
                d = abs(a[1] - b[1] - 3600 * 24)
                pp.append(d)
            
            a = b
        
        return np.array(sorted(pp)) 
