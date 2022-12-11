def calc():
    def _calc():
        i = 1
        sum = 0
        while 1:
            try:
                num = int(input("输入数字(输入任意字母结束)："))
            except ValueError:
                break
            sum += num
            rvg = sum / i
            yield rvg
            i += 1
    g = _calc()
    while 1:
        try:
            print(next(g))
        except StopIteration:
            break


calc()
