#======================================
# file name:python3_atan_func.py
# author:liangliangSu
# date of writing:2022-09-11 22:43
# description:
#======================================
#!/usr/bin/env python3
#Python3 atan() 函数
#Python3 数字 Python3 数字
#描述
#atan() 返回x的反正切弧度值。
#语法
#以下是 atan() 方法的语法:
#import math
#math.atan(x)
#注意：atan()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。
#参数
#x -- 一个数值。
#返回值
#返回x的反正切弧度值。
#实例
#以下展示了使用 atan() 方法的实例：
#!/usr/bin/python3
import math
print ("atan(0.64) : ",  math.atan(0.64))
print ("atan(0) : ",  math.atan(0))
print ("atan(10) : ",  math.atan(10))
print ("atan(-1) : ",  math.atan(-1))
print ("atan(1) : ",  math.atan(1))
#以上实例运行后输出结果为：
#atan(0.64) :  0.5693131911006619
#atan(0) :  0.0
#atan(10) :  1.4711276743037347
#atan(-1) :  -0.7853981633974483
#atan(1) :  0.7853981633974483
