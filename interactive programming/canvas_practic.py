# first example of drawing on the canvas

import simplegui

# define draw handler

def draw(canvas):
    canvas.draw_text("Hello!",[100,100],24,"White")
    # [100,100]坐标在hello字符的左下角
    canvas.draw_circle([100,100],2,2,"red")


# create frame

frame = simplegui.create_frame( "Test" , 300 , 200)

# register draw handler    
frame.set_draw_handler(draw)

# start frame

frame.start()