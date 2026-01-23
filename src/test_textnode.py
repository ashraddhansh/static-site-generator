from typing import Text
import unittest
import htmlnode
from textnode import TextNode, TextType
from textnode import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node,node2)
    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node,node2)
    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "google.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "google.com")
        self.assertEqual(node,node2)

    def test_repr(self):
        node = TextNode("This is text node", TextType.TEXT, "https://arpit.dev")
        self.assertEqual("TextNode(This is text node, text, https://arpit.dev)", repr(node))

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code(self):
        node = TextNode("This is code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code text")

    def test_link(self):
        node = TextNode("This is link text", TextType.LINK,"www")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is link text")

    def test_image(self):
        node = TextNode("This is image text", TextType.IMAGE, "www")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
                html_node.props,
                {"src": "www", "alt": "This is image text"}
                )


if __name__ == "__main__":
    unittest.main()
