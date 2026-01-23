from textnode import TextNode, TextType
def main():
    obj1 = TextNode("This is some anchor text", TextType.LINK, "https://boot.dev")
    print(obj1)
main()
