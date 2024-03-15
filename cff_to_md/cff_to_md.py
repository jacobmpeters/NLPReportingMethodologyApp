import yaml

def format_to_md(obj, level=4):
    """
    Recursively formats a given object (dict or list) into a markdown string.
    
    Parameters:
    - obj (dict | list): The object to format, typically parsed from a YAML file.
    - level (int): The current heading level for markdown formatting, with '####' as the default.
    
    Returns:
    - str: A markdown-formatted string representing the input object.
    """
    markdown = ""
    if isinstance(obj, dict):
        for key, value in obj.items():
            markdown += f"{'#' * level} {key}\n\n"
            markdown += format_to_md(value, level + 1)
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict):
                markdown += f"- "
                item_details = [f"**{key}:** {format_to_md(value, level + 1).strip()}" for key, value in item.items()]
                markdown += "<br>  ".join(item_details) + "\n\n"
            else:
                markdown += f"- {item}\n\n"
    else:
        markdown += f"{obj}\n\n"
    return markdown

def cff_to_md(file_path, starting_header_level=4):
    """
    Converts a .cff file into a markdown-formatted string.
    
    Parameters:
    - file_path (str): Path to the .cff file to be converted.
    - starting_header_level (int): The starting level for markdown headings.
    
    Returns:
    - str: The content of the .cff file formatted as a markdown string.
    """
    with open(file_path, 'r') as file:
        cff_content = yaml.safe_load(file)
    markdown = format_to_md(cff_content, starting_header_level)
    return markdown


