"""
print("hello world!")  #字符串
print(2333)    #整数
print(2.333)   #小数
print(True)    #布尔值
print(())     #元祖
print([])     #数组
print({})     #字典

print(5343)                     

print(2351)
print(2333) 
print(2563)
print("haha")
print(2<3)
print(3>2)
a = "张三"   #把张三这个值赋值给了名字叫a的变量
print(a)
"""
# a = float (input("请输入:"))
# b = float (input("请输入:"))
# print("input获取的内容:",a+b)
#数据格式的转换/
# print(type("哈哈"))
# print(type(2333))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

# a = input("a:")
# b = input("b:") 

# print("长度:",len(a)+len(b))



# 元祖,下标（从零开始标号）
# a = (1,2,3,4,"哈哈","哈哈","学习")
# print(a[-2])
# # 切片
# print(a[0:4]) #左闭右开
# print(a[4:5])
# print(a[:-2])
# # 0,1,2,3，4,5
   
# print(a[54])
# print(a.index("哈哈"))
# print(a.count("哈哈"))
#二维元祖

# # print(b[0][3])      
# # b = (a,"哈哈","嘻嘻")
# a = [1,2,3,4,"哈哈","哈哈","学习",True,False]
# a.append("天天")
# a.append("向上")
# print(a)
# # 元祖一旦写好过后不可以修改，而数组是可以修改的
# a.insert(4,"嘻嘻")
# print(a)
# b = a.pop(0)   #剪切
# c = a.pop(0)
# print(b+c)
# print(a)
# print(b)
# print(c)
# #a.clear()
# xx = ["你好","不好"]
# #a.extend(xx)
# print(a+xx)
# print(a)
# a.remove(1)
# print(a)
# 下标不要超出范围
"""
pythond的语法
所有的方法都是小括号结尾，比如：print(),input()
元祖，数组，字典的取值，都是用中括号，比如a[0]
元祖，数组，字典的定义，分别是(),[],{}
"""




"""
字典的特点
1,字典中的值没有顺序。
2，字典的结构必须是键值对的结构。 key : value
"""
a = {"name":"shadow",0:"哈哈",'age':25}

# 取值
# print(a["name"])
# # 新增
# a["high"] = "183cm"
# print(a)
# # 修改
# a['name'] = 'zhangsan'
# print(a)
# b = a.get('name')
# print(b)
a.update(nsame=1235)
print(a)
'''
获取用户输入的个人信息，并且存储到字典中
个人信息包括，name，age，sex。
'''

