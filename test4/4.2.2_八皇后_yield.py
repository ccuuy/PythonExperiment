def isUnconflicted(ocpy, point):
    for item in ocpy:
        if point[0] == item[0] or abs(point[0]-item[0]) == abs(point[1]-item[1]):
            return 0
    return 1


def EightQueensWithYield(ocpy=[], n=8):
    for i in range(n):
        if isUnconflicted(ocpy, [i, len(ocpy)]):
            if len(ocpy) == n-1:
                yield [[i, len(ocpy)]]
            else:
                for j in EightQueensWithYield(ocpy+[[i, len(ocpy)]], n):
                    yield [[i, len(ocpy)]] + j


a = EightQueensWithYield()
while 1:
    try:
        print(next(a))
    except StopIteration:
        break
