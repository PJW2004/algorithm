import sys
from itertools import chain
n = int(sys.stdin.readline())
sys.stdout.writelines([f"{n}\n", ' '.join(chain(("1", "2"), map(str,range(3, n)), ("997",)))])