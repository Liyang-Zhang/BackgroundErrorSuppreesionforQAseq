# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 13:56:20 2022

@author: liyang
Use this script to get summary about error signals in either pre-polished or polished databases FREQ files
"""
import pandas as pd
import os
import glob

# Specify output dir 
working_dir="C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\errorSuppression\\KLM\\UMIdb\\db\\report"
os.chdir(working_dir)

# Specify working files
working_files = "C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\errorSuppression\\KLM\\UMIdb\\db\\1-75*.txt"
fileNames=[]
for file in glob.glob(working_files):
    fileNames.append(file)

# create a dictionary to store infos
out_dict = {}
for working_file in fileNames:
    sampleID = working_file.split("\\")[-1].split("_")[0]
    out_dict[sampleID] = {"A>C":0,
                          "A>G":0,
                          "A>T":0,
                          "C>A":0,
                          "C>G":0,
                          "C>T":0,
                          "G>A":0,
                          "G>C":0,
                          "G>T":0,
                          "T>A":0,
                          "T>C":0,
                          "T>G":0}
    depth = 0
    working_df = pd.read_csv(working_file, sep="\t", lineterminator='\n')
    # obtain variant UMIkinds
    for index, row in working_df.iterrows():
        depth += row.DEPTH
        ref = row.REF
        As = row["A+"]
        Cs = row["C+"]
        Ts = row["T+"]
        Gs = row["G+"]
        if As > 0:
            out_dict[sampleID][ref + ">A"] += As
        if Cs > 0:
            out_dict[sampleID][ref + ">C"] += Cs
        if Ts > 0:
            out_dict[sampleID][ref + ">T"] += Ts
        if Gs > 0:
            out_dict[sampleID][ref + ">G"] += Gs
    # convert to error rate
    for value in out_dict[sampleID]:
        out_dict[sampleID][value] = 100 * out_dict[sampleID][value]/depth
        
out_df = pd.DataFrame(out_dict)
out_name = "75-NC_errorRate_prepolish.txt"
out_df.to_csv(out_name, sep = "\t", index = True)

        