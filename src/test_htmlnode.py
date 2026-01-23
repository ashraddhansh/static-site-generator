import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("p", "This is paragraph",None,{"class": "para","href": "https://arpit.dev"})
        self.assertEqual(node.props_to_html(),' class="para" href="https://arpit.dev"')

    def test_tag(self):
        node = HTMLNode("p", "This is paragraph")
        self.assertEqual(node.tag,'p')
        self.assertEqual(node.value,'This is paragraph')
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "This is paragraph",None,{"class": "para","href": "https://arpit.dev"})
        #self.assertEqual(node.__repr__(),'HTMLNode(p, This is paragraph, children: None,  class="para" href="https://arpit.dev")')
        self.assertEqual(node.__repr__(),"HTMLNode(p, This is paragraph, children: None, {'class': 'para', 'href': 'https://arpit.dev'})")
        

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a","Click to Download",{"href": "https://kmclu.ac.in","class": "url"})
        self.assertEqual(node.to_html(), '<a href="https://kmclu.ac.in" class="url">Click to Download</a>')

    def test_leaf_to_html_b_i(self):
        node = LeafNode("b", "This is bold")
        node2 = LeafNode("i", "This is italic")
        self.assertEqual(node.to_html(), '<b>This is bold</b>')
        self.assertEqual(node2.to_html(), '<i>This is italic</i>')

    def test_leaf_to_html_notag(self):
        node = LeafNode(None,"Hello, World!")
        self.assertEqual(node.to_html(), 'Hello, World!')



if __name__ == "__main__":
    unittest.main()
