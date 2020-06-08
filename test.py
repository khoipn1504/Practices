def what_to_do(instructions):
    if instructions.endswith("Simon says"):
        return "I "+instructions[:instructions.find("Simon says")-1]
    elif instructions.startswith("Simon says"):
        return "I "+instructions[len("Simon says")+1:]
    else:
        return "I won't do it!"


what_to_do("Simon says make a wish")
