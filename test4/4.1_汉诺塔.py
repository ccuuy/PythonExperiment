def hannoi(num, src, dst, temp):
    if num == 1:
        globals()[dst].append(globals()[src].pop())
        print(globals()[dst][-1], ":  from", src, "to", dst,
              "\nA:", A, "\nB:", B, "\nC:", C)
    if num > 1:
        hannoi(num-1, src, temp, dst)
        globals()[dst].append(globals()[src].pop())
        print(globals()[dst][-1], ":  from", src, "to", dst,
              "\nA:", A, "\nB:", B, "\nC:", C)
        hannoi(num-1, temp, dst, src)


A = list(range(0, 64))
A.reverse()
B = []
C = []
hannoi(64, 'A', 'C', 'B')
