'''
https://blog.csdn.net/samjustin1/article/details/52138733
'''
def swap(x, y):
    x = x + y  # x暂存两数之和
    y = x - y  # y为两数之和减去y，即原来的x
    x = x - y  # x为两数之和减去现在的y（原来的x），变成原来的y
    return x, y

    x ^= y  # x先存x和y两者的信息
    y ^= x  # 保持x不变，利用x异或反转y的原始值使其等于x的原始值
    x ^= y  # 保持y不变，利用x异或反转y的原始值使其等于y的原始值
    return x, y