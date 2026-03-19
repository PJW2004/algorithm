import sys
input_stdin = sys.stdin.readline
for _ in range(int(input_stdin())):
    # strip() 안넣으면 \n 제거 안됨.
    new_text = ''.join([
        chr(ord(character) + 32) if 
        ord(character) <= 90 else character 
        for character in input_stdin().strip()])
    print(new_text)