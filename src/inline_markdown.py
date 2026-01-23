from textnode import TextNode, TextType
import re
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) %2 != 0:
            raise Exception("Invalid Markdown Syntax: formatted section not closed")

        parts = []
        parts.extend(node.text.split(delimiter))
        split_nodes = []
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i%2 == 0:
                split_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(parts[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
        

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if links == []:
            new_nodes.append(old_node)
            continue
        first_link_tuple = links[0]
        link_text, url = first_link_tuple[0], first_link_tuple[1]
        sections = old_node.text.split(f"[{link_text}]({url})", 1)
        if len(sections) != 2:
            raise ValueError("invalid markdown, link section not closed")
        before, after = sections[0], sections[1]


        if before != "":
            before_node = TextNode(before,TextType.TEXT)
            new_nodes.append(before_node)
        link_node = TextNode(link_text, TextType.LINK, url)
        new_nodes.append(link_node)
        if after != "":
            after_node = TextNode(after, TextType.TEXT)
            new_nodes.append(after_node)

    for new_node in new_nodes:
        if new_node.text_type == TextType.TEXT and extract_markdown_links(new_node.text) != []:
            return split_nodes_link(new_nodes)

    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if images == []:
            new_nodes.append(old_node)
            continue
        first_image_tuple = images[0]
        alt_text, url = first_image_tuple[0], first_image_tuple[1]
        sections = old_node.text.split(f"![{alt_text}]({url})", 1)
        if len(sections) != 2:
            raise ValueError("invalid markdown, image section is not closed")
        before, after = sections[0], sections[1]

        if before != "":
            before_node = TextNode(before,TextType.TEXT)
            new_nodes.append(before_node)
        image_node = TextNode(alt_text, TextType.IMAGE, url)
        new_nodes.append(image_node)
        if after != "":
            after_node = TextNode(after, TextType.TEXT)
            new_nodes.append(after_node)

    for new_node in new_nodes:
        if new_node.text_type == TextType.TEXT and extract_markdown_images(new_node.text) != []:
            return split_nodes_image(new_nodes)

    return new_nodes

