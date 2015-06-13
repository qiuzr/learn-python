#x是全局变量
x = 5

def fun1(y):
    # 这里必须声明x是global变量，因为x=x+y给x重新赋值了
    global x
    x=x+y
    return y

print fun1(3)
print "x=",x

def fun2(y):
    #不用声明x是global变量，没有给x赋值
    y=x+y
    #这里直接把全局变量x的值引用过来即可
    return y

print fun2(3)
print "x=",x

def fun3(y):
    #这里直接把全局变量x的值引用过来即可
    return x+y

print fun3(3)
print "x=",x