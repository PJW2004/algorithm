# ------------- 1. fast, memory‑light input -------------
import sys
stdin = sys.stdin.readline          # local alias → cheaper look‑ups

# base date: eight single‑digit integers read in one line
BASE: tuple[int, ...] = tuple(map(int, stdin().strip()))     # (Y1,Y2,Y3,Y4,M1,M2,D1,D2)

# ------------- 2. tight arithmetic kernel -------------
def bio_rhythm(date: str, base: tuple[int, ...] = BASE) -> int:
    """Squared-difference product without intermediate containers."""
    return (
        ((base[0] - (d0 := ord(date[0]) - 48)) ** 2             # year    (4 digits)
         + (base[1] - (d1 := ord(date[1]) - 48)) ** 2
         + (base[2] - (d2 := ord(date[2]) - 48)) ** 2
         + (base[3] - (d3 := ord(date[3]) - 48)) ** 2)
        * ((base[4] - (d4 := ord(date[4]) - 48)) ** 2           # month   (2 digits)
           + (base[5] - (d5 := ord(date[5]) - 48)) ** 2)
        * ((base[6] - (d6 := ord(date[6]) - 48)) ** 2           # day     (2 digits)
           + (base[7] - (d7 := ord(date[7]) - 48)) ** 2)
    )

# ------------- 3. streaming scan for the maximum -------------
best_date, best_score = "", -1
for _ in range(int(stdin())):               # no list‑build → O(1) extra memory
    s = stdin().strip()
    score = bio_rhythm(s)
    if score >= best_score:                 # resolves ties in favour of later dates
        best_date, best_score = s, score

print(best_date)
