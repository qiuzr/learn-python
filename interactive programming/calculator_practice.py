import simplegui

store=0
opp=0

def output():
    global store,opp
    print "store = " , store
    print "opp = " , opp

def add():
    global store,opp
    store = store + opp
    output()
    
def input(inp):
    global opp
    opp = float(inp)
    output()
    
    
    
frame = simplegui.create_frame("caculator", 200,200)
frame.add_button("add", add,100)
frame.add_button("output", output,100)
# frame.add_input ：将所输入的字符串(inp)赋给input函数中的形参
# 需要注意的是：返回给形参的都是字符串！按下回车键触发
inp = frame.add_input("input_opp", input, 100)
