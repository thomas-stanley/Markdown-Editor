def header():
    global main_text
    while True:
        level = int(input("Level: "))
        if level in range(1, 7):
            break
        print("The level should be within the range of 1 to 6")
    text = input("Text: ")
    hashes = "#" * level
    if len(main_text) == 0:
        main_text += f"{hashes} {text}\n"
    else:
        main_text += f"\n{hashes} {text}\n"


def bold():
    global main_text
    text = input("Text: ")
    main_text += f"**{text}**"


def italic():
    global main_text
    text = input("Text: ")
    main_text += f"*{text}*"


def plain():
    global main_text
    text = input("Text: ")
    main_text += f"{text}"


def inline_code():
    global main_text
    text = input("Text: ")
    main_text += f"`{text}`"


def new_line():
    global main_text
    main_text += "\n"


def link():
    global main_text
    label = input("Label: ")
    url = input("URL: ")
    main_text += f"[{label}]({url})"


def general_list():
    global main_text
    while True:
        rows_num = int(input("Number of rows: "))
        if rows_num > 0:
            break
        print("The number of rows should be greater than zero")
    for item in range(rows_num):
        element = input(f"Row #{item + 1}: ")
        if formatter == "unordered-list":
            main_text += f"* {element}\n"
        elif formatter == "ordered-list":
            main_text += f"{item + 1}. {element}\n"


def help_code():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")


def done():
    with open("output.md", "w") as file:
        file.write(main_text)
    quit()


def unknown_format():
    print("Unknown formatting type or command")


main_text = ""
available_formatters = {
    "header": header,
    "bold": bold,
    "italic": italic,
    "plain": plain,
    "link": link,
    "inline-code": inline_code,
    "new-line": new_line,
    "ordered-list": general_list,
    "unordered-list": general_list,
    "!help": help_code,
    "!done": done
}
while True:
    formatter = input("Choose a formatter: ")
    if formatter not in available_formatters:
        unknown_format()
    else:
        available_formatters[formatter]()
        print(main_text)
