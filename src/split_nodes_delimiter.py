from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            #print("Node isn't TEXT typed.")
            new_nodes.append(node)
        elif delimiter in node.text:
            #print("Delimiter found!")
            #print(f"Node: \n{node}")
            split_text = node.text.split(delimiter, 1)
            #print(f"Split text: \n{split_text}")
            if delimiter in split_text[1]:
                double_split_text = split_text[1].rsplit(delimiter, 1)
                #print(f"Double_split_text: {double_split_text}")
            else:
                raise Exception(f"Missing closing {delimiter}, invalid Markdown syntax")
            new_nodes.extend([TextNode(split_text[0], TextType.TEXT),TextNode(double_split_text[0], text_type), TextNode(double_split_text[1], TextType.TEXT)])
        else:
            new_nodes.append(node)
    
    return new_nodes