# **********************************************************
# * Author : liangliangsu
# * Email : sll917@hotmail.com
# * Create time : 2022-09-21 15:40
# * Filename : file_readline方法.py
#!/usr/bin/python3
# **********************************************************
#Python3 File readline() 方法
#Python3 File(文件) 方法 Python3 File(文件) 方法
#概述
#readline() 方法用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。
#语法
#readline() 方法语法如下：
#fileObject.readline(); 
#参数
#size -- 从文件中读取的字节数。
#返回值
#返回从字符串中读取的字节。
#实例
#以下实例演示了 readline() 方法的使用：
#文件 runoob.txt 的内容如下：
#1:www.runoob.com
#2:www.runoob.com
#3:www.runoob.com
#4:www.runoob.com
#5:www.runoob.com
#读取文件的内容：
#实例
#!/usr/bin/python3
# 打开文件
fo = open("runoob.txt", "r+")
print ("文件名为: ", fo.name)
line = fo.readline()
print ("读取第一行 %s" % (line))
line = fo.readline(5)
print ("读取的字符串为: %s" % (line))
fo.close()
fo = open("runoob.txt", "r+")
line = fo.readline(9)
print ("读取的字符串为: %s" % (line))
fo.close()
fo = open("runoob.txt", "r+")
line = fo.readline(16)
print ("读取的字符串为: %s" % (line))
# 关闭文件
fo.close()
#以上实例输出结果为：
#文件名为:  runoob.txt
#读取第一行 1:www.runoob.com
#读取的字符串为: 2:www
