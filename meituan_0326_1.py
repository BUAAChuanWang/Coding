# a = -12
# nums = 2 3 7 6 5 4 3 2 1
# -23
while 1:
    a = input()
    a_i = ["0"]
    a_i += input().split(" ")

    res = ""
    for i in range(len(a)):
        if i == 0 and a[i] == "-":
            res += "-"
            continue
        res += a_i[int(a[i])]
    print(int(res))