#Timers
# Simple "screensaver" program.

# Import modules
import simplegui
import random

# Global state
message = "Python is Fun!"
position = [50, 50]#list，用来描述文字在屏幕上的位置
width = 500
height = 500
interval = 2000#2000毫秒

# Handler for text box
def update(text):
    global message
    message = text
    
#把message变为text（你输入进来的文字），注意必须声明message是全局变量
# Handler for timer
def tick():
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y
    
#此处并没有改变整个position的值，没有给position赋值
#只是改变了position元素的值，这种情况下不需要声明position是全局变量

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, position, 36, "Red")
#36号字体，红色字，在position位置画出message；draw每秒运行60次

# Create a frame 
frame = simplegui.create_frame("Home", width, height)

# Register event handlers
text = frame.add_input("Message:", update, 150)
#input输入，按回车，运行update()函数，输入的文本存储在text变量中
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)
#每interval毫秒，运行一次tick

# Start the frame animation
frame.start()
timer.start()
