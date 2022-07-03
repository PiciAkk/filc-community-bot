def transform(commands,message):
    print(f"commands: {commands}")
    print(f"message: {message}")
    for i in commands:
        if i in message:
            message = message.replace(f"{i} ","")
    print(message)
    return message