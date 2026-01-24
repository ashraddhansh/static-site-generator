import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType


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

