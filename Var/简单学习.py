'''
    编码
    默认情况下, Python3源码文件以 UTF-8 编码, 所有字符串都是 unicode 字符串.
    也可以指定不同的编码: coding: cp-1252
'''
# -*- coding: UTF-8 -*-


'''
    注释
    1. 单行注释以 # 开头
        #  注释...
    2. 多行注释 以三个 ' 开头和结尾
'''

'''
    保留字
    保留字即关键字, 我们不能把他们用作任何标识符名称. Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字:
    import keyword
    print(keyword.kwlist)
    
    ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''

'''
    行与缩进
    Python 最具特色的就是使用缩进来表示代码块，不需要使用大括号({})
    缩进的空格数是可变的, 但是同一个代码块的语句必须包含相同的缩进空格数
    if True:
        print("True")
    else:
        ptint("False")
'''


'''
    多行语句
    Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠来实现多行语句
    total = "item_one" + \
            'item_two' + \
            'item_three'
    但是在 [], {} 或 () 中的多行语句, 不需要使用反斜杠.
    total = ['item_one',
             'item_two']
'''



'''
    数据类型
    * Python 中有四种类型: 整数、长整数、浮点数和复数
        整数， 如 1
        长整数是比较大的整数
        浮点数 如 1.23, 3e-2
        复数 如 1 + 2j, 1.1 + 2.2j
'''


'''
    字符串
    * Python 中单引号和双引号使用完全相同.
    * 使用三引号或"""可以指定一个多行字符串.  例如:     
        str = """
                i
                am  
                a 
                bad
                man
            """
    * 转义符 \
    * 自然字符串, 通过在字符串前加 r 或 R，如 r"this is a line with \n" 则\n 会显示, 并不是换行.
    * Python 允许处理 unicode 字符串, 加前缀 u 或 U，如 u"this is an unicode string".
    * 字符串是不可变的
    * 按字面意义级连字符串, 如 "this" "is" "String" 会被转换成 thisisstring
'''


'''
    空行
    函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
    空行与代码缩进不同，空行并不是Python语法的一部分。 书写时不插入空行，Python 解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
    记住： 空行也是程序的一部分。
'''



'''
    等待输入
    inputStr = input("\n\n按下 enter 键后退出.\n")
    print(inputStr)
    代码中 \n\n 在结果输出前会输出两个新的 空行, 一旦用户按下 enter 键盘， 程序将退出.
'''



'''
    同一行显示多条语句
    Python 可以在同一行中使用多条语句, 语句之间使用分号(;)分割
    import sys; x = 'runoob'; sys.stdout.write(x + '\n')    
    执行结果会在终端输出 runood 加一个换行.
'''


'''
    多个语句构成代码组
    缩进相同的一组语句构成一个代码块，我们称之为代码组。
    像if、while、def和class这样的复合语句，首行以关键字开始，以冒号(:)结束，该行之后的一行或多行代码构成代码组。
    我们将首行及后面的代码组，称为一个子句(clause)
    if expression:
        suite
    elif expression:
        suite
    else:
        suite
    
'''



'''
    print 输出
    print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
    str = 'hello Python'
    print(str, end="      ")
    print(str)
'''



'''
    import 和 from...import
    在 Python 中，用 import 或者 from...import 来导入相应的模块。
    将整个模块导入，格式为： import somemodule
    从某个模块中导入某个函数，格式为：from somemodule import somefunction
    从某个模块中导入多个函数，格式为：from somemodule import firstfunc, secondfunc, thirdfunc
    将某个模块中的全部函数导入，格式为：from somemodule import *
'''


'''
    命令行参数
    很多程序可以执行一些操作来查看一些基本信息，Python 可以使用-h参数查看各参数帮助信息；
'''