from textnode import TextNode, TextType
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
        




