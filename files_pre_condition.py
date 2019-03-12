# _*_ coding:utf-8 _*_
'''

@description: split the original data into small pieces
@author: xing

'''
import os
import glob
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.Parameters.parameters import *

"""
Paramters
"""
SAVE_AS_TXT = True

def file_split(file_path=DATASET_BASE_PATH,data_len=DATA_LEN):
    dir_name = file_path.split(os.sep)[-1]
    new_dir_name = "".join([dir_name,'_new'])
    dir_paths = os.listdir(file_path)
    
    for dir_path in dir_paths:
        new_file_path = os.path.join(file_path,dir_path).replace(dir_name, new_dir_name)
        if os.path.exists(new_file_path)==False:
            os.makedirs(new_file_path)
    files_lists = glob.glob(os.path.join(file_path, '*','*.csv'))
    
    for file_list in files_lists:
        print('Current file handled: %s' % file_list)
        wave_data = pd.read_csv(file_list,header=None).values[:,1]
        wave_len = len(wave_data)
        split_num = int(wave_len // data_len)
        i = 0
        while (split_num > 0):
            split_num -= 1
            slice_num_l = int(DATA_LEN*i)
            slice_num_h = int(DATA_LEN*(i+1))
            if SAVE_AS_TXT:
                save_file_name = file_list.replace(dir_name, new_dir_name).replace('.csv', '_' + str(i) + '.txt')
                np.savetxt(save_file_name, wave_data[slice_num_l:slice_num_h], fmt='%4.6f')
            else:
                save_file_name = file_list.replace(dir_name, new_dir_name).replace('.csv', '_' + str(i) + '.csv')
                df_wave = pd.DataFrame(wave_data[slice_num_l:slice_num_h])
                df_wave.to_csv(save_file_name)
            i += 1
    print('File split completely')
    print('The data length is %d' %data_len)
    

    
        
if __name__ == '__main__':
    file_split()


