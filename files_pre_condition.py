# _*_ coding:utf-8 _*_
'''

@description: split the original data into small pieces
@author: xing

'''
import os     #系统操作
import glob   #查找符合特定规则的文件路径名
import sys
import pandas as pd   #csv文件处理模块
import numpy as np    #数组运算
import matplotlib.pyplot as plt     #绘图
from src.Parameters.parameters import *

"""
Paramters
"""
SAVE_AS_TXT = True

def file_split(file_path=DATASET_BASE_PATH,data_len=DATA_LEN):               #定义函数方法
    dir_name = file_path.split(os.sep)[-1]                                   #切分路径，返回倒数第一个路径
    new_dir_name = "".join([dir_name,'_new'])                                #在被切分的路径后添加_new并返回给new_dir_name
    dir_paths = os.listdir(file_path)                                        #列出该路径下所有文件名称

    for dir_path in dir_paths:                                               #将dir_paths列表中项目依次循环操作
        new_file_path = os.path.join(file_path,dir_path).replace(dir_name, new_dir_name)     #将file_path（总路径）与dir_path（已列出的目录中的文件名）连接成为新路径，再用new_dir_name替换掉dir_name,返回值是一个路径
        if os.path.exists(new_file_path)==False:                             #检查是否重名
            os.makedirs(new_file_path)                                       #不重名则创建该文件夹
    files_lists = glob.glob(os.path.join(file_path, '*','*.csv'))            #所有新数据文件的路径.
    
    for file_list in files_lists:
        print('Current file handled: %s' % file_list)
        wave_data = pd.read_csv(file_list,header=None).values[:,1]           #读取数据文件中所有文件的第一列数据
        wave_len = len(wave_data)                                            #数据长度
        split_num = int(wave_len // data_len)
        i = 0
        while (split_num > 0):
            split_num -= 1
            slice_num_l = int(DATA_LEN*i)
            slice_num_h = int(DATA_LEN*(i+1))
            if SAVE_AS_TXT:
                save_file_name = file_list.replace(dir_name, new_dir_name).replace('.csv', '_' + str(i) + '.txt')       #SAVE_AS_TXT=True则存为txt文件
                np.savetxt(save_file_name, wave_data[slice_num_l:slice_num_h], fmt='%4.6f')
            else:
                save_file_name = file_list.replace(dir_name, new_dir_name).replace('.csv', '_' + str(i) + '.csv')       #否则依旧存为csv文件
                df_wave = pd.DataFrame(wave_data[slice_num_l:slice_num_h])
                df_wave.to_csv(save_file_name)
            i += 1
    print('File split completely')
    print('The data length is %d' %data_len)
    

    
        
if __name__ == '__main__':
    file_split()


