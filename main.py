formatted_text = []


def level_input():
    flag = True
    while flag:
        try:
            level = int(input("Level: "))
            if 0 < level < 7:
                return level
                flag = False
            else:
                print("The level should be within the range of 1 to 6")
        except ValueError:
            print("The level should be within the range of 1 to 6")


def header_formatter(level, text):
    if len(formatted_text) == 0:
        formatted_text.append("#" * level + " " + text + "\n")
    else:
        formatted_text.append("\n" + "#" * level + " " + text + "\n")


def bold_formatter(text):
    formatted_text.append(f"**{text}**")


def plain_formatter(text):
    formatted_text.append(text)


def italic_formatter(text):
    formatted_text.append("*" + text + "*")


def inline_code_formatter(text):
    formatted_text.append("`" + text + "`")


def new_line_formatter():
    formatted_text.append("\n")


def link_formatter():
    label = input("Label: ")
    url = input("URL: ")
    formatted_text.append("[" + label + "]" + "(" + url + ")")


def list_formatter(choose_formatter):
    while True:
        number_of_rows = int(input("Number of rows: "))
        if number_of_rows > 0:
            if choose_formatter == "ordered-list":
                for _ in range(1, number_of_rows + 1):
                    ordered_list_item = input(f"Row #{_}: ")
                    ordered_list_item_to_list = str(_) + ". " + ordered_list_item + "\n"
                    formatted_text.append(ordered_list_item_to_list)
                break
            elif choose_formatter == "unordered-list":
                for _ in range(1, number_of_rows + 1):
                    unordered_list_item = input(f"Row #{_}: ")
                    unordered_list_item_to_list = "* " + unordered_list_item + "\n"
                    formatted_text.append(unordered_list_item_to_list)
                break
        else:
            print("The number of rows should be greater than zero")


def formatted_text_printer():
    print("".join(str(x) for x in formatted_text))


def markdown_creator():
    available_formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list",
                            "unordered-list", "new-line"]
    special_commands = ["!help", "!done"]

    flag = True

    while flag:
        choose_formatter = input("Choose a formatter: ")
        if choose_formatter in available_formatters:
            if choose_formatter == "header":
                level = level_input()
                text = input("Text: ")
                header_formatter(level, text)
                formatted_text_printer()
            elif choose_formatter == "bold":
                text = input("Text: ")
                bold_formatter(text)
                formatted_text_printer()
            elif choose_formatter == "plain":
                text = input("Text: ")
                plain_formatter(text)
                formatted_text_printer()
            elif choose_formatter == "italic":
                text = input("Text: ")
                italic_formatter(text)
                formatted_text_printer()
            elif choose_formatter == "inline-code":
                text = input("Text: ")
                inline_code_formatter(text)
                formatted_text_printer()
            elif choose_formatter == "new-line":
                new_line_formatter()
                formatted_text_printer()
            elif choose_formatter == "link":
                link_formatter()
                formatted_text_printer()
            elif choose_formatter == "ordered-list" or choose_formatter == "unordered-list":
                list_formatter(choose_formatter)
                formatted_text_printer()
        elif choose_formatter == "!help":
            print("Available formatters: " + " ".join(str(x) for x in available_formatters))
            print("Special commands: " + " ".join(str(x) for x in special_commands))
        elif choose_formatter == "!done":
            name_file = open("output.md", "w")
            name_file.write("".join(str(x) for x in formatted_text))
            name_file.close()
            flag = False
        elif choose_formatter not in available_formatters:
            print("Unknown formatting type or command")


markdown_creator()