'''
合法名字
时间限制： 3000MS
内存限制： 589824KB
题目描述：
现在的调查问卷越来越多了，所以出现了很多人恶意刷问卷的情况，已知某问卷需要填写名字，如果名字仅由大小写英文字母组成且长度不超过10，则我们认为这个名字是真实有效的，否则就判定为恶意填写问卷。

请你判断出由多少有效问卷（只要名字是真实有效的，就认为问卷有效）。



输入描述
输入第一行包含一个正整数n，表示收到的问卷数量。(1<=n<=2000)

接下来有n行，每行有一个由大小写英文字母，数字，下划线组成的字符串，分别表示一份问卷的名字，字符串长度不超过100。

输出描述
输出只有一个整数，表示有效问卷数量。


样例输入
5
BA
aOWVXARgUbJDG
OPPCSKNS
HFDJEEDA
ABBABBBBAABBBAABAAA
样例输出
3

提示
输入样例2
2
E_DB2C
DC
输出样例2
1
'''
while 1:
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    res = 0
    for i in range(n):
        flag = True
        if len(names[i]) > 10:continue
        for c in names[i]:
            if "a" <= c <= "z" or "A" <= c <= "Z":
                continue
            else:
                flag = False
                break
        if flag: res += 1
    print(res)
