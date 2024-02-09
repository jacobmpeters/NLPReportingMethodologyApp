import csv
import yaml

def convert_to_cff(input_file, output_file, delimiter=','):
    """
    Converts any CSV/TSV file to a Citation File Format (CFF) YAML file.

    Parameters:
    - input_file: Path to the input CSV/TSV file.
    - output_file: Path to the output CFF YAML file.
    - delimiter: Delimiter used in the input file, default is ',' for CSV.
    """
    with open(input_file, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        
        # Initialize an empty list to hold all entries (assuming multiple entries possible in the CSV)
        cff_entries = []

        for row in reader:
            # Create a dictionary for the current row
            cff_dict = {}
            
            # Add all CSV fields as custom fields
            for key, value in row.items():
                if value.strip():  # Only add non-empty fields
                    cff_dict[key] = value.strip()
            
            # Add the current dictionary to the entries list
            cff_entries.append(cff_dict)

        # Write all entries to the output CFF file
        with open(output_file, 'w') as yamlfile:
            yaml.dump_all(cff_entries, yamlfile, sort_keys=False, default_flow_style=False)
