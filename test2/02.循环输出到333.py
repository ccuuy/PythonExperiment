for i in range(5):
    for j in range(5):
        for k in range(5):
            if i == 3 and j == 3 and k == 3:
                print("it's over")
                flag = 1
                break
            else:
                print(i, j, k)
        if "flag" in locals():
            break
    if "flag" in locals():
        break
