total = 0

with open('mods.txt') as mods:
    for m in mods:
        m = float(m) / 3
        m = int(m)
        m = float(m) - 2
        total = total + m
        print(int(total))

