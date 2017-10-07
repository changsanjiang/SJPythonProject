# Author:SanJiang
# Python3 基本数据类型


'''
Python 中的变量不需要声明. 每个变量在使用前都必须赋值, 变量赋值以后改变量才会被创建.
在 Python 中, 变量就是变量, 他没有类型, 我们所说的"类型"是变量所指的内存中对象的类型.
等号(=)用来给变量赋值.
等号(=)运算符左边是一个变量名, 等号(=)运算符右边是存储在变量中的值. 例如:

counter = 100   #   整型变量
miles = 1000.0  #   浮点型变量
name = "runoob" #   字符串

print(counter, miles, name)
'''


'''
多个变量赋值
    Python 允许同时为多个变量赋值. 例如: 
    a = b = c = 1
    a, b, c = 1, 2, "runoob"
'''

'''
标准数据类型
    Python 中有6个标准的数据类型:
    * Number
    * String
    * List 
    * Tuple
    * Sets
    * Dictionary
'''

'''
Number
    Python3 支持 int、float、bool、complex(复数).
   
    在 Python3 里, 只有一种整数类型 int, 表示为长整型, 没有 Python2 中的 Long.
   
    内置的 type() 函数可以用来查询变量所指的对象类型. 如下:
            a, b, c, d = 20, 5.5, True, 4+3j
            print(type(a), type(b), type(c), type(d))
            打印结果: <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
        也可以用 isinstance 来判断:
            a = 111
            print (isinstance(a, int))   
            打印结果: True
        isinstance 和 type 的区别在于:
            *   type() 不会认为子类是一种父类类型.
            *   isinstance() 会认为子类是一种父类类型.
        如下:     
        class A:
            pass

        class B(A):
            pass

        print( isinstance(A(), A) )     #   True
        print( type(A()) == A )         #   True
        print( isinstance(B(), A) )     #   True
        print( type(B()) == A )         #   False     
     
    注意：在 Python2 中没有布尔型, 他用数字 0 表示 False, 用 1 表示 True. 
         在 Python3 中, 把 True 和 False 定义成关键字了, 但他们的值还是 1 和 0, 他们可以和数字相加.
         
         
    当你为变量指定一个值时, Number 对象就会被创建:
        var1 = 1
        var2 = 10
    
    你也可以使用 del 语句删除一些对象引用.
        var1 = 1
        var2 = 2
        var3 = 3 
        del  var1, var2, var3
'''




'''
数值运算
    5 + 4       # 加法
    4.3 - 2     # 减法
    3 * 7       # 乘法  
    2 / 4       # 除法, 得到一个浮点数  
    2 // 4      # 除法, 得到一个整数
    17 % 3      # 取余
    2 ** 5      # 乘方

    注意：
        *   1. Python 可以同时为多个变量赋值, 如 a, b = 1, 2
        *   2. 一个变量可以通过赋值指向不同类型的对象
        *   3. 数值的除法(/)总是返回一个浮点数, 要获取整数使用(//)操作符
        *   4. 在混合计算时, Python 会把整型转换成为浮点数. 
        
    Python 还支持复数, 复数由实数部分和虚数部分构成, 可以用 a + bj, 或者complex(a, b)表示, 复数的实部a和虚部b都是浮点型.
    
'''




'''
String(字符串)
    Python 中的字符串用单引号(')或双引号(")括起来, 同时使用反斜杠(\)转义特殊字符.
    
    字符串的截取 语法如下:
        变量[头下标:尾下标]
        
        索引值以 0 为开始值, -1 为从末尾的开始位置.
    
'''






