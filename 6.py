a = float(input("请输入第一条边的长度："))
b = float(input("请输入第二条边的长度："))
c = float(input("请输入第三条边的长度："))
L = (a + b + c) / 2
s = (L * (L - a) * (L - b) * (L - c)) ** 0.5
print("三角形的面积为：{:.2f}".format(s))