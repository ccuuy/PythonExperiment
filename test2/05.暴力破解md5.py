from hashlib import md5
from itertools import permutations
from string import ascii_letters, digits

flag = 0
for i in range(5, 11):
    for item in permutations(ascii_letters + digits, i):
        word = "".join(item)
        if md5(word.encode()).hexdigest() == "23eeeb4347bdd26bfc6b7ee9a3b755dd":
            print(word)
            break
        flag = 1
    if flag == 1:
        break
