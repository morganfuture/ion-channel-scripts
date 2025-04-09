# -*- coding: utf-8 -*-
"""
Created on Thr Apr 08 2025


Usage help: python cmm-extraction.py -h

@author: Aimin Cheng at Peking University

"""
#!/usr/bin/python

import re
import os
import argparse

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="python cmm-extraction.py -h",epilog='''
    script to extract pseudoatom coordinate and convert into cif for display hole in pymol
    written by Aimin Cheng @ Peking University''')
    parser.add_argument("--i",help="cmm format input file,e.g. kcsa.cmm")
    parser.add_argument("--o",help="cif format output file,e.g. kcsa.cif")
    args=parser.parse_args()

def extract_marker_data(input_file, output_file):
    # Regular expression to extract the required values
    pattern = r'<marker.*?x="(.*?)".*?y="(.*?)".*?z="(.*?)".*?r="(.*?)".*?g="(.*?)".*?b="(.*?)".*?/>'
    
    # Read the input file
    with open(input_file, 'r') as f:
        content = f.read()
    
    # Find all matches
    matches = re.findall(pattern, content, re.DOTALL)
    
    # Write to output file
    with open(output_file, 'w') as f:
        f.write("      data_foo"+"\n")
        f.write("loop_"+"\n")
        f.write("_atom_site.Cartn_x"+"\n")
        f.write("_atom_site.Cartn_y"+"\n")
        f.write("_atom_site.Cartn_z"+"\n")
        f.write("_atom_site.ignore_size_a"+"\n")
        f.write("_atom_site.ignore_size_b"+"\n")
        f.write("_atom_site.ignore_size_c"+"\n")
        for match in matches:
            line = '\t'.join(match)
            f.write(line + '\n')
    
    print(f"Extraction complete. Data written to {output_file}")
    print(f"Processed {len(matches)} marker entries")

# Example usage
input_file=args.i  #"kcsa.cmm"  # Your input file
output_file=args.o  #"extracted_marker_data.txt"  # Output file

# Check if input file exists
if os.path.exists(input_file):
    extract_marker_data(input_file, output_file)
else:
    print(f"Error: Input file '{input_file}' not found.")
