# Measure-Command { Get-Content 4447_refactoring.txt | python .\4447_refactoring.py > 4447_refactoring_out.txt }
d = ["NEUTRAL", "GOOD", "A BADDY"]
t, *s = open(0).read().splitlines()

for l in s:
    g = l.count('g') + l.count('G')
    b = l.count('b') + l.count('B')
    print(f"{l} is {d[(g>b)-(g<b)]}")