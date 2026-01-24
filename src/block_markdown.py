from enum import Enum

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

