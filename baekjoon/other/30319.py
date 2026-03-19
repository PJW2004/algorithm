import sys
sys.stdout.write("TOO LATE\n" if sys.stdin.readline()[:10] > "2023-09-16" else "GOOD\n")