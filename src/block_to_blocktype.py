from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    if markdown[0] == "#":
        return BlockType.HEADING
    elif markdown[:3] == "```" and markdown[-3:-1] == "```":
        return BlockType.CODE
    elif markdown[0] == ">":
        return BlockType.QUOTE
    elif markdown[0] == "-":
        return BlockType.UNORDERED_LIST
    elif markdown[0:2] == "1. ":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH