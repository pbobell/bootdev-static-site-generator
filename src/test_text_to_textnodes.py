import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType



class TestSplitNodesDelimiter(unittest.TestCase):
    def test_text_to_textnodes_example(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        conversion_result = [
                                TextNode("This is ", TextType.TEXT),
                                TextNode("text", TextType.BOLD),
                                TextNode(" with an ", TextType.TEXT),
                                TextNode("italic", TextType.ITALIC),
                                TextNode(" word and a ", TextType.TEXT),
                                TextNode("code block", TextType.CODE),
                                TextNode(" and an ", TextType.TEXT),
                                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                                TextNode(" and a ", TextType.TEXT),
                                TextNode("link", TextType.LINK, "https://boot.dev"),
                            ]
        self.assertEqual(conversion_result, text_to_textnodes(text))