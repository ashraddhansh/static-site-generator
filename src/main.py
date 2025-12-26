from textnode import TextNode, TextType
def main():
    obj1 = TextNode("This is some anchor text", TextType.URL, "https://boot.dev")
    print(obj1)
main()
