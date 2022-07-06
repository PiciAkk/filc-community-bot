def parse_message(message):
    splitted = message.split(" ")

    return splitted[1:] if splitted[0] == "!" \
                            else [splitted[0][1:]] + splitted[1:]