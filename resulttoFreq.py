# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 17:32:39 2022

@author: Liyang
Goal: Convert background polishing freq results to easy-reading excel format
Input: FREQ files
Output: highlighted and classified FREQ files 
Issues: too complex, any ways to simplify the code
"""

import pandas as pd
import os
from pandas.core.frame import DataFrame
import openpyxl
import glob
import re


working_dir="C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\errorSuppression\\DEF"
os.chdir(working_dir)

mutation_ref_dir="C:\\Users\\admin\\documents\\MRD\\standardResult\\standard_3rdtrial\\mutation\\J\\"
writer = pd.ExcelWriter('J_UMI_polished_FREQ.xlsx', engine='xlsxwriter')

# Read in rmbg.txt files
fileNames=[]
for file in glob.glob("*-J*.txt"):
    fileNames.append(file)
   



for working_file in fileNames:
    base = working_file.split('_')[0]
    mutation_ref_name = mutation_ref_dir + base + "_varlist.xlsx"
    work_df = pd.read_csv(working_file, sep='\t')
    mut_df_real = pd.read_excel(mutation_ref_name, 'MRD')
    mut_df_fake = pd.read_excel(mutation_ref_name, 'MRD_error')
    work_df.to_excel(writer, sheet_name=base)
    # Get the xlsxwriter workbook and worksheet objects.
    workbook  = writer.book
    worksheet = writer.sheets[base]
    # Add 2 formats. Light red fill with dark red text.
    format1 = workbook.add_format({'bg_color': 'yellow',
                                   'font_color': 'gold'})
    format2 = workbook.add_format({'bg_color': '#FFC7CE',
                                   'font_color': '#9C0006'})
    for index, row in work_df.iterrows():
        # Judge if "T" in the row is non-zero and the locus appaers in the mut_real sheet
        if ( row['T+'] != 0 and row['CHR'] in mut_df_real['plex_id'].values ):
            var = mut_df_real.loc[mut_df_real['plex_id'] == row['CHR'], "var"].values[0]
            # if the MRD sheet's variant type for this NuMRD is consistent with the row
            if var == "T":
                start_row = index + 1
                start_col = 11
                end_row = start_row
                end_col = start_col
                worksheet.conditional_format(start_row, start_col, end_row, end_col,
                                             {'type':     'cell',
                                              'criteria': '>',
                                              'value':    0,
                                              'format':   format1})
            else:
                start_row = index + 1
                start_col = 11
                end_row = start_row
                end_col = start_col
                worksheet.conditional_format(start_row, start_col, end_row, end_col,
                                             {'type':     'cell',
                                              'criteria': '>',
                                              'value':    0,
                                              'format':   format2})
        
        elif (row['T+'] != 0 and row['CHR'] not in mut_df_real['plex_id'].values):
            start_row = index + 1
            start_col = 11
            end_row = start_row
            end_col = start_col
            worksheet.conditional_format(start_row, start_col, end_row, end_col,
                                         {'type':     'cell',
                                          'criteria': '>',
                                          'value':    0,
                                          'format':   format2})
        if ( row['A+'] != 0 and row['CHR'] in mut_df_real['plex_id'].values ):
            var = mut_df_real.loc[mut_df_real['plex_id'] == row['CHR'], "var"].values[0]
            #var_fake = mut_df_fake.loc[mut_df_real['plex_id'] == row['CHR'], "var"].values[0]
            if var == "A":
                start_row = index + 1
                start_col = 7
                end_row = start_row
                end_col = start_col
                worksheet.conditional_format(start_row, start_col, end_row, end_col,
                                             {'type':     'cell',
                                              'criteria': '>',
                                              'value':    0,
                                              'format':   format1})
            else:
                start_row = index + 1
                start_col = 7
                end_row = start_row
                end_col = start_col
                worksheet.conditional_format(start_row, start_col, end_row, end_col,
                                             {'type':     'cell',
                                              'criteria': '>',
                                              'value':    0,
                                              'format':   format2})
        elif (row['A+'] != 0 and row['CHR'] not in mut_df_real['plex_id'].values):
            start_row = index + 1
            start_col = 7
            end_row = start_row
            end_col = start_col
            worksheet.conditional_format(start_row, start_col, end_row, end_col,
                                         {'type':     'cell',
                                          'criteria': '>',
                                          'value':    0,
                                          'format':   format2})
        if ( row['C+'] != 0 and row['CHR'] in mut_df_real['plex_id'].values ):
            var = mut_df_real.loc[mut_df_real['plex_id'] == row['CHR'], "var"].values[0]
            #var_fake = mut_df_fake.loc[mut_df_real['plex_id'] == row['CHR'], "var"].values[0]
            if var == "C":
                start_row = index + 1
                start_col = 9
                end_row = start_row
                end_col = start_col
                worksheet.conditional_format(start_row, start_col, end_row, end_col,
                                             {'type':     'cell',
                                              'criteria': '>',
                                              'value':    0,
                                              'format':   format1})
            else:
                start_row = index + 1
                start_col = 9
                end_row = start_row
                end_col = start_col
                worksheet.conditional_format(start_row, start_col, end_row, end_col,
                                             {'type':     'cell',
                                              'criteria': '>',
                                              'value':    0,
                                              'format':   format2})
        elif (row['C+'] != 0 and row['CHR'] not in mut_df_real['plex_id'].values):
            start_row = index + 1
            start_col = 9
            end_row = start_row
            end_col = start_col
            worksheet.conditional_format(start_row, start_col, end_row, end_col,
                                         {'type':     'cell',
                                          'criteria': '>',
                                          'value':    0,
                                          'format':   format2})                
        if ( row['G+'] != 0 and row['CHR'] in mut_df_real['plex_id'].values ):
            var = mut_df_real.loc[mut_df_real['plex_id'] == row['CHR'], "var"].values[0]
            #var_fake = mut_df_fake.loc[mut_df_real['plex_id'] == row['CHR'], "var"].values[0]
            if var == "G":
                start_row = index + 1
                start_col = 13
                end_row = start_row
                end_col = start_col
                worksheet.conditional_format(start_row, start_col, end_row, end_col,
                                             {'type':     'cell',
                                              'criteria': '>',
                                              'value':    0,
                                              'format':   format1})
            else:
                start_row = index + 1
                start_col = 13
                end_row = start_row
                end_col = start_col
                worksheet.conditional_format(start_row, start_col, end_row, end_col,
                                             {'type':     'cell',
                                              'criteria': '>',
                                              'value':    0,
                                              'format':   format2})
        elif (row['G+'] != 0 and row['CHR'] not in mut_df_real['plex_id'].values):
            start_row = index + 1
            start_col = 13
            end_row = start_row
            end_col = start_col
            worksheet.conditional_format(start_row, start_col, end_row, end_col,
                                         {'type':     'cell',
                                          'criteria': '>',
                                          'value':    0,
                                          'format':   format2})
    

    
# Close the Pandas Excel writer and output the Excel file.
writer.save()

