from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link
from split_nodes_delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    if type(text) is not str:
        raise Exception("Input isn't a string of text!")
    
    source = [TextNode(text, TextType.TEXT)]
    imaged = split_nodes_image(source)
    linked = split_nodes_link(imaged)
    bolded = split_nodes_delimiter(linked, "**", TextType.BOLD)
    italicized = split_nodes_delimiter(bolded, "_", TextType.ITALIC)
    coded = split_nodes_delimiter(italicized, "`", TextType.CODE)

    return coded