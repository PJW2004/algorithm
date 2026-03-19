for index in range(int(input())):
    alphabet = input()
    front_alphabet = ""
    for _alphabet in alphabet:
        if _alphabet == "Z":
            front_alphabet += "A"
        else:
            front_alphabet += chr(ord(_alphabet) + 1)
    print(f"String #{index+1}")
    print(front_alphabet)
    print()