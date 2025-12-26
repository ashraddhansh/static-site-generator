import unittest
from htmlnode import HTMLNode

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
        

if __name__ == "__main__":
    unittest.main()
