"""判断一个数是否为水仙花数"""
x = int(input('请输入一个三位数'))
ge = x % 10
shi = x // 10 % 10
bai = x // 100
y = ge ** 3 + shi ** 3 + bai ** 3
print('是否为水仙花数:', x == y, )

"""计算体质指数的程序"""
tizhong = float(input('请输入体重(kg)：'))
shengao = float(input('请输入身高(m)：'))
bmi = tizhong / shengao ** 2
print("体质指数=", bmi, )
