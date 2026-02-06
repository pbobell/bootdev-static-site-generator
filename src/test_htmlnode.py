import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "This is a link HTML node", None, {"href": "https://www.google.com"})
        proptext = ' href="https://www.google.com"'
        converted_prop = node.props_to_html()
        self.assertEqual(converted_prop, proptext)


if __name__ == "__main__":
    unittest.main()