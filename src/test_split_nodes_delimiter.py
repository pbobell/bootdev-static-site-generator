import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType



class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_plain(self):
        old_nodes = [TextNode("This is a text node without delimiters.", TextType.TEXT)]
        split_result = [TextNode("This is a text node without delimiters.", TextType.TEXT)]
        self.assertEqual(split_result, split_nodes_delimiter(old_nodes, '**', TextType.BOLD))

    def test_split_nodes_delimiter_bold(self):
        old_nodes = [TextNode("This is a text node with **bold** delimiters.", TextType.TEXT)]
        split_result = [TextNode("This is a text node with ", TextType.TEXT),
                        TextNode("bold", TextType.BOLD),
                        TextNode(" delimiters.", TextType.TEXT)]
        self.assertEqual(split_result, split_nodes_delimiter(old_nodes, '**', TextType.BOLD))
