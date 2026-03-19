from sys import stdin
input_stdin=stdin.readline
for _ in range(int(input_stdin())):
    hour,minute,second=map(int, input_stdin().split(':'))
    hour_binary,minute_binary,second_binary=map(lambda number: bin(number)[2:].rjust(6, '0'), [hour,minute,second])
    
    three_row = ''.join(''.join(chunk) for chunk in zip(hour_binary,minute_binary,second_binary))
    three_column = ''.join([hour_binary,minute_binary,second_binary])
    print(f"{three_row} {three_column}")