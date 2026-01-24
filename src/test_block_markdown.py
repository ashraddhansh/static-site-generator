import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node


class TestBlockMarkdown(unittest.TestCase):
        def test_markdown_to_blocks1(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )


        def test_markdown_to_blocks_with_whitespaces_and_extra_newline(self):
            md = """
  This is **bolded** paragraph


  This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line  


- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )
        
        def test_block_to_block_type_paragraph(self):
            text = "This is Arpit"
            type = block_to_block_type(text)
            self.assertEqual(type,BlockType.PARAGRAPH)

            text = "- This is Arpit"
            type = block_to_block_type(text)
            self.assertNotEqual(type,BlockType.PARAGRAPH)

            text = "1. This is Arpit"
            type = block_to_block_type(text)
            self.assertNotEqual(type,BlockType.PARAGRAPH)

        def test_block_to_block_type_heading1(self):
            text = "# Heading 1"
            type = block_to_block_type(text)
            self.assertEqual(type,BlockType.HEADING)

            text = "Heading 1"
            type = block_to_block_type(text)
            self.assertNotEqual(type,BlockType.HEADING)

            text = "#Heading 1"
            type = block_to_block_type(text)
            self.assertNotEqual(type,BlockType.HEADING)

            text = "####### Heading 1"
            type = block_to_block_type(text)
            self.assertNotEqual(type,BlockType.HEADING)

            text = "##"
            type = block_to_block_type(text)
            self.assertNotEqual(type,BlockType.HEADING)

        def test_block_to_block_type_code(self):
            text = "```\nprint('hello')```"
            type = block_to_block_type(text)
            self.assertEqual(type,BlockType.CODE)

            text = "```\nprint('hello')\n```"
            type = block_to_block_type(text)
            self.assertEqual(type,BlockType.CODE)

            text = "``\nprint('hello')```"
            type = block_to_block_type(text)
            self.assertNotEqual(type,BlockType.CODE)

            text = "```\nprint('hello')"
            type = block_to_block_type(text)
            self.assertNotEqual(type,BlockType.CODE)

        def test_block_to_block_type_quote(self):
            text = "> Hello this is quote1\n> this is quote 2"
            type = block_to_block_type(text)
            self.assertEqual(type,BlockType.QUOTE)

            text = "> Hello this is quote1\n>this is quote 2"
            type = block_to_block_type(text)
            self.assertNotEqual(type,BlockType.QUOTE)

        def test_block_to_block_type_olist(self):
            text = "1. hello this is arpit\n2. Hello this is again me"
            type = block_to_block_type(text)
            self.assertEqual(type, BlockType.OLIST)

            text = "1. hello this is arpit\n2. Hello this is again me"
            type = block_to_block_type(text)
            self.assertEqual(type, BlockType.OLIST)

            text = "1. hello this is arpit\n3. Hello this is again me"
            type = block_to_block_type(text)
            self.assertNotEqual(type, BlockType.OLIST)

            text = "2. hello this is arpit\n3. Hello this is again me"
            type = block_to_block_type(text)
            self.assertNotEqual(type, BlockType.OLIST)

            text = "1.hello this is arpit\n2. Hello this is again me"
            type = block_to_block_type(text)
            self.assertNotEqual(type, BlockType.OLIST)

        def test_block_to_block_type_ulist(self):
            text = "- first element\n- second element"
            type = block_to_block_type(text)
            self.assertEqual(type, BlockType.ULIST)

            text = "-first element\n- second element"
            type = block_to_block_type(text)
            self.assertNotEqual(type, BlockType.ULIST)

            text = "- first element\n-second element"
            type = block_to_block_type(text)
            self.assertNotEqual(type, BlockType.ULIST)

        def test_paragraphs(self):
            md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

        def test_codeblock(self):
            md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
            )
        def test_quote(self):
            md = """> This is a **quoted** line
> This is another line"""
    
            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><blockquote>This is a <b>quoted</b> line\nThis is another line</blockquote></div>",
            )

        def test_unordered_list(self):
            md = """- Item **one**
- Item _two_
- Item three"""
    
            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
            html,
            "<div><ul><li>Item <b>one</b></li><li>Item <i>two</i></li><li>Item three</li></ul></div>",
            )

        def test_ordered_list(self):
            md = """1. First item with **bold**
2. Second item with _italic_
3. Third item"""
    
            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
            html,
            "<div><ol><li>First item with <b>bold</b></li><li>Second item with <i>italic</i></li><li>Third item</li></ol></div>",
            )

        def test_heading(self):
            md = """## Heading with **bold** text"""
    
            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
            html,
            "<div><h2>Heading with <b>bold</b> text</h2></div>",
            )
