import simplegui

#define global value

value = 3.12

# Handle single quantity
def convert_units(val, name):
    #val 是一个数字，int型 转换成字符串输出
    result = str(val) + " " + name
    
    
    if val > 1:
        result = result + "s"
    #当钱>1是，dollor和cent需要用复数，加s
    return result        
# convert xx.yy to xx dollars and yy cents
def convert(val): 
    # Split into dollars and cents
    dollars = int(val) #取整
    cents = int(round(100 * (val - dollars)))
    #不是所有的浮点型都能被准确计算，经常会产生一些偏差
    # round函数会考虑到这种情况，可以做一些四舍五入

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
    # 只输出分的语句就可以了
        return cents_string
    elif cents == 0:
    #只输出元的语句
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    
def input_handler(text):
    global value
    value = float (text)
    
# define draw handler
def draw(canvas):
    canvas.draw_text(convert(value),[60,100],24,"white") #必须把value强制转化成字符型
#define frame    
frame = simplegui.create_frame("Converter",400,200)
#register event handler
frame.set_draw_handler(draw)
frame.add_input("Enter Value",input_handler,100)
#star frame
frame.start()
