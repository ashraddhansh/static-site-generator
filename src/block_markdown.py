def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    clean = list(filter(lambda x: x is not None and x.strip() != "", blocks))
    return list(map(lambda x: x.strip(), clean))

