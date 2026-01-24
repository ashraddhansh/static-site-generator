from enum import Enum
import re


from htmlnode import HTMLNode, LeafNode
from parentnode import ParentNode
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType, text_node_to_html_node

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    clean = list(filter(lambda x: x is not None and x.strip() != "", blocks))
    return list(map(lambda x: x.strip(), clean))

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered list"
    OLIST = "ordered list"

def block_to_block_type(markdown_text):
    def is_code_block(text):
        return text.startswith("```\n") and text.endswith("```")
    def is_quote_block(text):
        parts = text.split("\n")
        for part in parts:
            if not part.startswith("> "):
                return False
        return True
    def is_u_list(text):
        parts = text.split("\n")
        for part in parts:
            if not part.startswith("- "):
                return False
        return True

    def is_o_list(text):
        parts = text.split("\n")
        expected = 1
        for part in parts:
            if not part[0].isdigit():
                return False
            i = 0
            while i < len(part) and part[i].isdigit():
                i +=1

            if i+1 >= len(part):
                return False
            if part[i] != "." or part[i+1] != " ":
                return False
            num = int(part[:i])
            if num != expected:
                return False

            expected += 1
        return True


    def is_heading(text):
        if not text.startswith("#"):
            return False
        i = 0
        while i < len(text) and text[i] == "#":
            i += 1

        if i > 6:
            return False
        if i == len(text):
            return False
        if text[i] != " ":
            return False
        return True
       
    returned = BlockType.PARAGRAPH
    if is_heading(markdown_text):
        returned = BlockType.HEADING
    if is_quote_block(markdown_text):
        returned = BlockType.QUOTE
    if is_code_block(markdown_text):
        returned = BlockType.CODE
    if is_o_list(markdown_text):
        returned = BlockType.OLIST
    if is_u_list(markdown_text):
        returned = BlockType.ULIST
    return returned

def markdown_to_html_node(markdown):
    def text_to_children(text):
        nodes = [TextNode(text,TextType.TEXT)]
        nodes = split_nodes_delimiter(nodes, "**",TextType.BOLD)
        nodes = split_nodes_delimiter(nodes, "_",TextType.ITALIC)
        nodes = split_nodes_delimiter(nodes, "`",TextType.CODE)
        nodes = split_nodes_link(nodes)
        nodes = split_nodes_image(nodes)

        html_nodes = []
        for node in nodes:
            html_node = text_node_to_html_node(node)
            html_nodes.append(html_node)
        return html_nodes

    def to_ulist(block):
        items = block.split("\n")
        list_item = []
        for item in items:
            item_text = item[2:]
            childern = text_to_children(item_text)
            li_node = ParentNode("li",childern)
            list_item.append(li_node)
        return ParentNode("ul", list_item)
    
    def to_olist(block):
        items = block.split("\n")
        list_item = []
        for item in items:
            item_text = re.sub(r'^\d+\.\s*', '', item)
            childern = text_to_children(item_text)
            li_node = ParentNode("li", childern)
            list_item.append(li_node)
        return ParentNode("ol", list_item)

    def to_heading(block):
        i = 0
        while i < len(block) and block[i] == "#":
            i += 1
        heading_level = i
        heading_text = block[heading_level+1:]
        childern = text_to_children(heading_text)
        tag = "h" + str(heading_level)
        return ParentNode(tag,childern)
    
    def to_quote(block):
        items = block.split("\n")
        quote_lines = []
        for item in items:
            cleaned_lines = item[2:]
            quote_lines.append(cleaned_lines)
        quote_text = "\n".join(quote_lines)
        childern = text_to_children(quote_text)
        return ParentNode("blockquote", childern)

    def to_para(block):
        block = block.replace("\n", " ")
        childern = text_to_children(block)
        return ParentNode("p",childern)

    def to_code(block):
        code_text = block[4:-3]
        code_node = TextNode(code_text,TextType.TEXT)
        code_html = text_node_to_html_node(code_node)
        code_element = ParentNode("code", [code_html])
        return ParentNode("pre", [code_element])

    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        if block_to_block_type(block) == BlockType.CODE:
            nodes.append(to_code(block))
        elif block_to_block_type(block) == BlockType.QUOTE:
            nodes.append(to_quote(block))
        elif block_to_block_type(block) == BlockType.PARAGRAPH:
            nodes.append(to_para(block))
        elif block_to_block_type(block) == BlockType.HEADING:
            nodes.append(to_heading(block))
        elif block_to_block_type(block) == BlockType.ULIST:
            nodes.append(to_ulist(block))
        elif block_to_block_type(block) == BlockType.OLIST:
            nodes.append(to_olist(block))

    main_html_node = ParentNode("div",nodes)

    return main_html_node
