# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:31:12 2022

@author: Liyang
Goal: Convert mutation result to UMI FREQ format
The inputs need changed for different samples
INPUT: four result table(mutation.xlsx, design.xlsx, UMI_number.xlsx, reference.xlsx)
"""
import pandas as pd
import os
from pandas.core.frame import DataFrame
import glob


'''
reference for ABC: C:\\Users\\admin\\documents\\MRD\\standardResult\\new_design_3_21\\mutation\\H-1-reference.xlsx
reference for KLM: C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\mutation\\K\\254676_KLM_reference.xlsx
reference for DEF: C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\mutation\\F\\254674_DEF_reference.xlsx
reference for NPQ: C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\mutation\\N\\254677_NPQ_reference.xlsx
reference for RST: C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\mutation\\R\\254678_RST_reference.xlsx
reference for GHJ: C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\mutation\\H\\254675_GHJ_reference.xlsx
reference for AAABAC: C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\mutation\\AA\\79-AAABAC-reference.xlsx
reference for AGAHAJ: C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\mutation\\AH\\81-AGAHAJ-reference.xlsx
'''
# Specify working dir 
working_dir="C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\errorSuppression\\AAABAC\\UMIdb\\db"
os.chdir(working_dir)


# Specify reference and design table
reference_file = "C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\mutation\\AA\\79-AAABAC-reference.xlsx"
design_file = "C:\\Users\\admin\\Documents\\MRD\\standarddata\\standards_3rd\\design_R0254679.xlsx"

# Go through each file in mutation and depth file
# Specify base name!
base = "79-NC"
mut_files = "C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\mutation\\" + base +"\\*_varlist.xlsx"
fileNames=[]
for file in glob.glob(mut_files):
    fileNames.append(file)


for mut_file in fileNames:
    print(mut_file)
    depth_file = mut_file.replace("mutation", "datasummary").replace("_varlist", "_UMI_number")
    baseSuper = mut_file.split("\\")[-1].split("_")[0]
    #depth_file = "C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\datasummary\\79-NC\\1-79-NC12_UMI_number.xlsx"
    
    
    # store infos
    freq_dict = {}
    
    design_df = pd.read_excel(design_file)
    for index, row in design_df.iterrows():
        freq_dict[row.plex_id] = {}
        pos = row.ROI_start - row.start + 1
        freq_dict[row.plex_id]["POS"] = pos
        
    depth_df = pd.read_excel(depth_file)
    for index, row in depth_df.iterrows():
        freq_dict[row.amplicon_name]["DEPTH"] = row[2]
    
    ref_df = pd.read_excel(reference_file)
    for index, row in ref_df.iterrows():
        freq_dict[row.plex_id]["REF"] = row.ref
    
    mut_df_real = pd.read_excel(mut_file, "MRD")
    mut_df_fake = pd.read_excel(mut_file, "MRD_error")
    for index, row in mut_df_real.iterrows():
        if row["var"] == "A" and "A+" in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["A+"] += row.mol_count
        elif row["var"] == "A" and "A+" not in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["A+"] = row.mol_count
        if row["var"] == "C" and "C+" in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["C+"] += row.mol_count
        elif row["var"] == "C" and "C+" not in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["C+"] = row.mol_count
        if row["var"] == "T" and "T+" in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["T+"] += row.mol_count
        elif row["var"] == "T" and "T+" not in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["T+"] = row.mol_count
        if row["var"] == "G" and "G+" in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["G+"] += row.mol_count
        elif row["var"] == "G" and "G+" not in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["G+"] = row.mol_count
            
    for index, row in mut_df_fake.iterrows():
        if row["var"] == "A" and "A+" in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["A+"] += row.mol_count
        elif row["var"] == "A" and "A+" not in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["A+"] = row.mol_count
        if row["var"] == "C" and "C+" in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["C+"] += row.mol_count
        elif row["var"] == "C" and "C+" not in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["C+"] = row.mol_count
        if row["var"] == "T" and "T+" in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["T+"] += row.mol_count
        elif row["var"] == "T" and "T+" not in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["T+"] = row.mol_count
        if row["var"] == "G" and "G+" in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["G+"] += row.mol_count
        elif row["var"] == "G" and "G+" not in freq_dict[row.plex_id]:
            freq_dict[row.plex_id]["G+"] = row.mol_count
      
    for key, value in freq_dict.items():
        if "A+" not in value:
            value["A+"] = 0
        if "C+" not in value:
            value["C+"] = 0
        if "T+" not in value:
            value["T+"] = 0
        if "G+" not in value:
            value["G+"] = 0
        value["A-"] = 0
        value["C-"] = 0
        value["T-"] = 0
        value["G-"] = 0
        value["R-"] = 0
        value["R+"] = value["DEPTH"] - value["A+"] - value["C+"] - value["T+"] - value["G+"]
        
    freq_df = pd.DataFrame(freq_dict).T
    freq_df.reset_index(inplace=True)
    freq_df = freq_df.rename(columns = {'index':'CHR'})
    order = ["CHR", "POS", "DEPTH", "REF", "R+", "R-", "A+", "A-", "C+", "C-", "T+", "T-", "G+", "G-"]
    freq_df = freq_df[order]
    
    outputName = baseSuper+"_UMI_sorted.freq.allreads.Q30.txt"
    freq_df.to_csv(outputName, sep = "\t", index = False)