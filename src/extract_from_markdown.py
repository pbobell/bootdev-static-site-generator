import re

def extract_markdown_images(text):
    list_of_image_tuples = []
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    list_of_image_tuples = matches

    return list_of_image_tuples

def extract_markdown_links(text):
    list_of_link_tuples = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return list_of_link_tuples