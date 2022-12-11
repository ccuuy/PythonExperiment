
print(list(filter(lambda x: x == sum(
    list(filter(lambda i: x % i == 0, range(1, x)))), range(1, 1001))))


def upStairs(n):
    def _upStairs(n, step):
        n -= step
        if n == 0:
            return 1
        if n < 0:
            return 0
        return _upStairs(n, 1) + _upStairs(n, 2) + _upStairs(n, 3)
    return _upStairs(n, 1) + _upStairs(n, 2) + _upStairs(n, 3)


print(upStairs(10))

'''
def upStairs(n):
    res1 = []
    res2 = []

    def _upStairs(n, step):

        n -= step
        if n == 0:
            res1.append(step)
            res2.append(tuple(res1))
            res1.pop(-1)
            res1.pop(-1)
            return
        if n > 0:
            res1.append(step)
        if n < 0:
            return
        _upStairs(n, 1)
        _upStairs(n, 2)
        _upStairs(n, 3)

    _upStairs(n, 1)
    res1.clear()
    _upStairs(n, 2)
    res1.clear()
    _upStairs(n, 3)

    return res2


print(upStairs(10))


def upStairs(n, step, nums):
    if sum(nums) == n:
        print(nums)
    if sum(nums) > n:
        return
    if sum(nums) < n:
        for i in range(1, 4):
            nums.append(i)
            upStairs(n, i, nums)
            nums.pop()


upStairs(5, 0, [])

'''
