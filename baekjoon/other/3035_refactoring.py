import sys

def main() -> None:
    rd = sys.stdin.readline
    wr = sys.stdout.write

    R, _, ZR, ZC = map(int, rd().split())

    for _ in range(R):
        line = rd().rstrip('\n')
        horiz = ''.join(ch * ZC for ch in line)
        wr((horiz + '\n') * ZR)

if __name__ == "__main__":
    main()
