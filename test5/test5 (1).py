from random import randrange
from string import ascii_letters
import fileinput


num = randrange(0, 100)
flag = 0
for i in range(8):
    try:
        guess = int(input("Please input an integer:"))
        if guess == num:
            print("You Won!")
            flag = 1
            break
        if guess > num:
            print("Try a smaller number.")
        if guess < num:
            print("Try a bigger number.")
    except ValueError:
        print("Not an Integer!")
if flag == 0:
    print("You failed! The correct number is ", num)

dict1 = dict.fromkeys(ascii_letters, 0)
try:
    with open('./abc.txt', 'r', encoding='utf-8') as f:
        file = f.read()
        for letter in file:
            if letter.encode('utf-8').isalpha():
                dict1[letter] += 1
except FileNotFoundError:
    print("No such file in the directory. Please check the file path.")
else:
    print(dict1)

for line in fileinput.input(files=('abc.txt', 'abcopy.txt'), inplace=True):
    newLine = "#" + str(fileinput.filelineno()) + line
    print(newLine)
fileinput.close()
