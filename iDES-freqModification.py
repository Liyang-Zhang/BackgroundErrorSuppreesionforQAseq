# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 11:28:16 2022

@author: Liyang
Goal: Use this script to modify the read level backgrounf database FREQ files, and only retain the design sites' information
Input:

"""
import pandas as pd
import os
from pandas.core.frame import DataFrame
import glob

# Specify working dir 
working_dir="C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\errorSuppression\\ABC\\readdb_50loci\\db"
os.chdir(working_dir)

# Specify design table and working freq files
design_file = "C:\\Users\\admin\\Documents\\MRD\\standarddata\\standards_3rd\\design_R0254673.xlsx"
working_files = "C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\errorSuppression\\ABC\\readdb\\db\\*sorted.freq.allreads.Q30.txt"

fileNames=[]
for file in glob.glob(working_files):
    fileNames.append(file)

freq_dict = {}
design_df = pd.read_excel(design_file)
for index, row in design_df.iterrows():
    freq_dict[row.plex_id] = {}
    pos = row.ROI_start - row.start + 1
    freq_dict[row.plex_id]["POS"] = pos
    
for working_file in fileNames:
    outName = working_file.split("\\")[-1].split("_")[0] + "_50loci_" + working_file.split("\\")[-1].split("_")[1]
    working_df = pd.read_csv(working_file, sep="\t", lineterminator='\n')
    out_df = pd.DataFrame(columns=['CHR', 'POS', 'DEPTH', 'REF', 'R+', 'R-', 'A+', 'A-', 'C+', 'C-', 'T+', 'T-', 'G+', 'G-'])
    for key, value in freq_dict.items():
        print(working_df.loc[(working_df["CHR"] == key) & (working_df["POS"] == value["POS"])])
        out_df = out_df.append(working_df.loc[(working_df["CHR"] == key) & (working_df["POS"] == value["POS"])])
    out_df.to_csv(outName, sep="\t", index=False, header=True)

