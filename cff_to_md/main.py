import sys
sys.path.append('cff_to_md')

from cff_to_md import cff_to_md

# Example usage
file_path = 'cff_to_md/example.cff'  # Specify the path to your .cff file
formatted_markdown = cff_to_md(file_path, 
                               starting_header_level=5)  # Adjust the starting header level as needed

# Specify the output markdown file name
output_md_file = 'cff_to_md/example.md'

# Write the formatted markdown to the file
with open(output_md_file, 'w') as md_file:
    md_file.write(formatted_markdown)

print(f"Markdown formatted content has been written to {output_md_file}")