import unittest

from extract_from_markdown import extract_markdown_images, extract_markdown_links


class TestExtractFromMarkdown(unittest.TestCase):
    def test_extract_two_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        extracted_info = extract_markdown_images(text)
        self.assertEqual(extracted_info, expected_result)

    def test_extract_two_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_result = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        extracted_info = extract_markdown_links(text)
        self.assertEqual(extracted_info, expected_result)