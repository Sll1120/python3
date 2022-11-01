#======================================
# file name:python3_hypot_func.py
# author:liangliangSu
# date of writing:2022-09-11 22:51
# description:
#======================================
#!/usr/bin/env python3
#Python3 hypot() 函数
#Python3 数字 Python3 数字
#描述
#hypot() 返回欧几里德范数 sqrt(x*x + y*y)。
#语法
#以下是 hypot() 方法的语法:
#import math
#math.hypot(x, y)
#注意：hypot()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。
#参数
#x -- 一个数值。
#y -- 一个数值。
#返回值
#返回欧几里德范数 sqrt(x*x + y*y)。
#实例
#以下展示了使用 hypot() 方法的实例：
#!/usr/bin/python3
import math
print ("hypot(3, 2) : ",  math.hypot(3, 2))
print ("hypot(-3, 3) : ",  math.hypot(-3, 3))
print ("hypot(0, 2) : ",  math.hypot(0, 2))
#以上实例运行后输出结果为：
#hypot(3, 2) :  3.605551275463989
#hypot(-3, 3) :  4.242640687119285
#hypot(0, 2) :  2.0
