def isUnconflicted(ocpy, point):
    for item in ocpy:
        if point[0] == item[0] or abs(point[0]-item[0]) == abs(point[1]-item[1]):
            return 0
    return 1


def EightQueens(ocpy=[], y=0, n=8):
    res = 0
    if len(ocpy) == n:  # 找到一种成功情况
        ocpy.pop(-1)
        print(ocpy)
        return 1
    for i in range(0, n):
        if isUnconflicted(ocpy, [i, y]):
            ocpy.append([i, y])
            res += EightQueens(ocpy, y+1, n)
    if len(ocpy) > 0:  # 回溯到上一列
        ocpy.pop(-1)
    return res


print("总数为", EightQueens())
