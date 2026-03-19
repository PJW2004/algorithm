import sys
command_list = {
    "-":0,
    "\\":1,
    "(":2,
    "@":3,
    "?":4,
    ">":5,
    "&":6,
    "%":7,
    "/":-1
}
while (command_string := sys.stdin.readline().strip()) != "#":
    sum_data = 0
    for index, command in enumerate(command_string[::-1]):
        sum_data += (8**index)*(command_list[command])
    print(sum_data)