# -*- coding: utf-8 -*-
"""
Created on Thr Apr 08 2025
Usage help: python dat2cmm.py -h
@author: Aimin Cheng at Peking University
"""
#!/usr/bin/python

import argparse

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="python dat2cmm.py -h",epilog="script to convert coot dat to cmm for display hole in chimera/chimerax written by Aimin Cheng at Peking University")
    parser.add_argument("--i",help="input file, coot .dat file")
    parser.add_argument("--o",help="output file, chimera/chimerax .cmm file")
    args=parser.parse_args()
def convert_data_to_markers(input_file, output_file):
    """
    Convert each line of data to a marker element with increasing IDs.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    with open(output_file, 'w') as f:
        f.write('<marker_set name="marker set 1">\n')
        for i, line in enumerate(lines, 1):
            # Skip empty lines
            if not line.strip():
                f.write(line)
                continue
            parts = line.strip().split()
            # Extract values
            if len(parts) >= 7:
                x, y, z, r, g, b, color = parts[0:7]
                
                # Format the new line
                new_line =f'<marker id="{i}" x="{x}" y="{y}" z="{z}" ' + \
                          f'r="{r}" g="{g}" b="{b}" radius="0.1"/>\n'
                
                f.write(new_line)
            else:
                # If the line doesn't have enough parts, write it unchanged
                f.write(line)
        f.write("</marker_set>\n")

# Define the input and output file paths
input_file = args.i
output_file = args.o

# Convert the data
convert_data_to_markers(input_file, output_file)

print(f"Conversion complete. Output saved to {output_file}")
