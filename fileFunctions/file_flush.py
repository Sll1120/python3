#!/usr/bin/env python3
#======================================
# file name:file_flush方法.py
# author:liangliangSu
# date of writing:2022-09-18 20:12
#======================================
#Python3 File flush() 方法
#Python3 File(文件) 方法 Pyt_hon3 File(文件) 方法
#概述
#flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
#一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。
#语法
#flush() 方法语法如下：
#fileObject.flush();
#参数
#返回值
#该方法没有返回值。
#实例
#以下实例演示了 flush() 方法的使用：
#!/usr/bin/python3
# 打开文件
fo = open("runoob1.txt", "wb")
print ("文件名为: ", fo.name)
# 刷新缓冲区
fo.flush()
# 关闭文件
fo.close()
#以上实例输出结果为：
#文件名为:  runoob1.txt
