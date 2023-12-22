#!/usr/bin/env python3
import argparse
import pandas as pd
import sys

parsedesc="Convert a specified cell range from an Excel file to a CSV file."
parser = argparse.ArgumentParser(description=parsedesc)
parser.add_argument("file_path", help="Path to the Excel file")
parser.add_argument("--sheet", default="0",
                    help="Name of the worksheet")
parser.add_argument("cell_range", help="Cell range to extract, e.g., A1:D10")
args = parser.parse_args()

# Read the specified range from the Excel file into a DataFrame (same as before)
df = pd.read_excel(args.file_path, sheet_name=args.sheet_name, usecols=args.cell_range)

# Print the DataFrame as CSV to stdout
df.to_csv(sys.stdout, index=False)
