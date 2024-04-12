import os
import sys
import pandas as pd
import yaml
from datetime import datetime

def get_keywords_from_csv(csv_path):
    """
    Reads keywords from the questionnaire_responses.csv file.
    Returns a list of unique keywords.
    """
    df = pd.read_csv(csv_path, sep=';')
    keywords = df['keyword'].unique().tolist()
    return keywords

def build_cff(csv_path):
    """
    Builds the .cff file with the keywords included from questionnaire_responses.csv file.
    Creates the .cff file in the same directory as the CSV file.
    """
    keywords = get_keywords_from_csv(csv_path)

    csv_dir = os.path.dirname(csv_path)
    cff_file_path = os.path.join(csv_dir, 'example.cff')

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
        "keywords": keywords,
        "repository-code": "https://github.com/exampleuser/exampleproject",
        "license": "MIT"
    }

    cff_output = yaml.dump(cff_data, sort_keys=False, allow_unicode=True)

    with open(cff_file_path, 'w', encoding='utf-8') as cff_file:
        cff_file.write(cff_output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the path to the CSV file as a command line argument.")
        sys.exit(1)

    csv_path = sys.argv[1]
    build_cff(csv_path)

# To run: cd into the csv_to_cff filder and type `python convert_to_cff.py questionnaire_responses.csv` in the terminal