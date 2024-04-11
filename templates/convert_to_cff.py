import os
import sys
import pandas as pd
import yaml
from datetime import datetime

def get_keywords_from_excel(workbook_path, sheet_name):
    """
    Reads keywords from a specific sheet in an Excel workbook.
    Returns the keyword if found, otherwise returns "Keyword not found".
    """
    df = pd.read_excel(workbook_path, sheet_name=sheet_name)
    
    keyword = None
    for index, row in df.iterrows():
        if 'Keywords exported' in row.values:
            kw_exported_index = row.tolist().index('Keywords exported')
            keyword = row.iat[kw_exported_index + 1] if kw_exported_index + 1 < len(row) else None
            break
    
    return keyword if keyword is not None else "Keyword not found"

def build_cff(workbook_path):
    """
    Builds the .cff content with the keyword included from the specified Excel workbook.
    Creates the .cff file in the same directory as the Excel file.
    """
    # TODO: Should this be a  command line argument
    sheet_name = 'Scoring POC_v1'
    
    keyword = get_keywords_from_excel(workbook_path, sheet_name)
    
    workbook_dir = os.path.dirname(workbook_path)
    
    cff_file_path = os.path.join(workbook_dir, 'example.cff')
    
    cff_data = {
        "cff-version": "1.2.0",
        "message": "If you use this software in your work, please cite it using the following metadata.",
        "title": "Example Software Project",
        "version": "1.0.0",
        "date-released": datetime.today().strftime('%Y-%m-%d'),
        "authors": [
            {
                "name": "Jane Doe",
                "affiliation": "University of Somewhere",
                "orcid": "0000-0002-1825-0097"
            },
            {
                "name": "John Smith",
                "affiliation": "Another University",
                "orcid": "0000-0001-2345-6789"
            }
        ],
        "keywords": keyword,
        "repository-code": "https://github.com/exampleuser/exampleproject",
        "license": "MIT"
    }

    cff_output = yaml.dump(cff_data, sort_keys=False, allow_unicode=True)

    with open(cff_file_path, 'w', encoding='utf-8') as cff_file:
        cff_file.write(cff_output)

if len(sys.argv) < 2:
    print("Please provide the path to the Excel file as a command line argument.")
    sys.exit(1)

workbook_path = sys.argv[1]

build_cff(workbook_path)