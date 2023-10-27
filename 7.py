x = str(input('请输入一个三位以上的数'))
y = x[:: -1]
if x == y:
    print('True')
else:
    print('False')
