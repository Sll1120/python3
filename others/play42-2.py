for item in range(3):
    pwd=input('请输入密码：')
    if pwd=='8888':
        print('密码输入正确')
        break
    else:
        print('密码输入错误')
else:
    print('三次密码均输入错误')

