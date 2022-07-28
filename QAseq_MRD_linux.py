import pandas as pd
import os
from pandas.core.frame import DataFrame
import openpyxl
import glob
import argparse

"""
Usage: get varinat information on target sites from mutation excels
Input: several excel files with one excel as reference:
Output: another sheet for each sample mutation excel
"""

def extract_mutation(input_path: str, sample_name: str):
    mutation_path = input_path + "/mutation"
    print("mutation files in: "+mutation_path)
    os.chdir(mutation_path)
    ref_path = input_path + "/reference/*"
    ref_file = glob.glob(ref_path)[0]
    print("the reference file is: "+ref_file)
    fileNames=[]
    sample_file = mutation_path + "/" + "*-" + sample_name + "*varlist.xlsx"
    for file in glob.glob(sample_file):
        fileNames.append(file)
    
    for working_file in fileNames:
        print("working on: "+working_file)
        xls_ref = pd.ExcelFile(ref_file)
        df_ref = pd.read_excel(xls_ref, 'final')
        df_ref.rename(columns={"Unnamed: 0":"index"}, inplace=True)
        xls_work = pd.ExcelFile(working_file)
        df_work = pd.read_excel(xls_work, 'raw')
        df_work.rename(columns={"Unnamed: 0":"index"}, inplace=True)
        MRD_real = []
        MRD_error = []
        
        
        # for normal results
        for _, row1 in df_ref.iterrows():
            for _, row2 in df_work.iterrows():
                if row1['chr'] == row2['chr'] and row1["start"] == row2["start"] and row1["stop"] == row2["stop"]:
                    if row1["var"] == row2["var"]:
                        MRD_real.append(row2)
                    elif row1["var"] != row2["var"]:
                        MRD_error.append(row2)
        
        '''
        # for cmm ref results
        for _, row1 in df_ref.iterrows():
            for _, row2 in df_work.iterrows():
                if row1['chr'] == row2['chr'] and row1["start"] == row2["start"]:
                    if row1["ref"] == row2["var"]:
                        MRD_real.append(row2)
                    elif row1["ref"] != row2["var"]:
                        MRD_error.append(row2)
        '''
        # Only export real MRD
        MRD_df = DataFrame(MRD_real)
        MRD_error_df = DataFrame(MRD_error)
        #MRD_df_all = pd.concat([MRD_df, MRD_error_df])
        
        # Use package openyxl to edit excel files
        wb = openpyxl.load_workbook(working_file)
        # Remove the existed "MRD" sheet
        if "MRD" in wb.sheetnames:
            ws = wb["MRD"]
            wb.remove(ws)
            wb.save(working_file)
        if "MRD_error" in wb.sheetnames:
            ws = wb["MRD_error"]
            wb.remove(ws)
            wb.save(working_file)
        with pd.ExcelWriter(working_file, mode="a", engine="openpyxl") as writer:
            MRD_df.to_excel(writer, sheet_name="MRD")
            MRD_error_df.to_excel(writer, sheet_name="MRD_error")
            """
            if "MRD_real" not in writer.sheets:
                MRD_df.to_excel(writer, sheet_name="MRD_real")
            if "MRD_error" not in writer.sheets:
                MRD_error_df.to_excel(writer, sheet_name="MRD_error")
            """

if __name__=='__main__':
        parser = argparse.ArgumentParser(description='the unmapped reads blat with hg38')
        parser.add_argument('-i', '--inputpath', type=str, help='the path of lane')
        parser.add_argument('-s', '--samplename', type=str, help='the sample ID name')
        parser.add_argument('-t', '--Thread1', type=int, help='Thread count')
        args = parser.parse_args()
        Inputpath = args.inputpath
        Samplename = args.samplename
        Thread1=args.Thread1
        if not Thread1:
                Thread1=5
        extract_mutation(Inputpath,Samplename)

