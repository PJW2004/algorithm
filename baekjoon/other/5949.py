commas=input()
string=[]
for index, character in enumerate(commas[::-1]):
    if index % 3 == 0 and index != 0:
        string.append(",")
    string.append(character)
print("".join(string[::-1]))