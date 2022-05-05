#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:12:59 2022

@author: stu
"""

import numpy as np
import matplotlib.pyplot as plt
import re
# import pandas
# import math

file_path = '/Users/stu/Library/CloudStorage/OneDrive-Privat/UU/Matematisk Statestik/OU2/IceCube40StringData.txt'

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
            
        # cunt = np.array(list(map(float, re.findall(r'[0-9.]*[0-9]+', next(file, None)))))
        next(file, None)
        pp = [list(map(float, re.findall(r'[0-9.]*[0-9]+', line))) for line in file]
        # print(pp)
        print(pp.pop(-1)) #tar bort det sista värdet då det ej passar in, är dessutom antal sekunder på ett dygn
        # for line in file:
            # np.append(cunt, list(map(float, re.findall(r'[0-9.]*[0-9]+', line))))
        return np.array(pp)


data = load_file(file_path)
# print(data)

# skrivit kod för data extrahering


        


        
            