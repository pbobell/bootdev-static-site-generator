from textnode import TextType, TextNode
from extract_from_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
        
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        image_info = extract_markdown_images(node.text)
        if not image_info:
            new_nodes.append(node)
            continue
        original_text = node.text
        for i in range(len(image_info)):
            current_text = original_text.split(f"![{image_info[i][0]}]({image_info[i][1]})", 1)
            if len(current_text) != 2:
                raise ValueError(f"Failed to split node around image markdown")
            if current_text[0] != "":
                new_nodes.append(TextNode(current_text[0], TextType.TEXT))
            new_nodes.append(TextNode(image_info[i][0], TextType.IMAGE, image_info[i][1]))
            original_text = current_text[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
        
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        link_info = extract_markdown_links(node.text)
        if not link_info:
            new_nodes.append(node)
            continue
        original_text = node.text
        for i in range(len(link_info)):
            current_text = original_text.split(f"[{link_info[i][0]}]({link_info[i][1]})", 1)
            if len(current_text) != 2:
                raise ValueError(f"Failed to split node around link markdown")
            if current_text[0] != "":
                new_nodes.append(TextNode(current_text[0], TextType.TEXT))
            new_nodes.append(TextNode(link_info[i][0], TextType.LINK, link_info[i][1]))
            original_text = current_text[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes