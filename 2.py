x = int(input('请输入一个三位数：'))
ge = x % 10
shi = x // 10 % 10
bai = x // 100
print('个位', ge, '十位', shi, '百位', bai,)
