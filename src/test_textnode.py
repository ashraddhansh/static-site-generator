import unittest
from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()
