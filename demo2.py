import turtle as t
import colorsys as cs

t.bgcolor('black')
t.setup(1200,800)
t.width(2)

t.speed(0)
t.tracer(20)

def go_to(pos):
    t.up()
    t.goto(pos[0],pos[1])
    t.down()

def draw_hexagon(size):
    for i in range(1,7):
        t.forward(size)
        t.right(60)

def drawDesign():
    position = []
    size = 260
    for i in range(6):
        t.forward(size)
        cur_pos = t.pos()
        t.backward(size/2)
        t.right(60)
        position.append((cur_pos,t.heading()))

    for i ,(pos,angle) in enumerate(position):
        go_to(pos)
        hue = (i*1)/6
        t.seth(angle)
        step = 5
        inner_list = range(step, size+step, step)
        inner_list_le = len(inner_list)
        for j,v in enumerate(inner_list):
            t.color(cs.hsv_to_rgb(hue,(j*1)/inner_list_le,1))
            start_pos = t.pos()
            t.forward(v)
            t.right(120)
            t.circle(-size,45)
            t.right(135)
            t.circle(-size,45)
            go_to(start_pos)
            t.seth(angle)
    cur_pos = t.pos()
    go_to((-96,96))
    for i in range(1,26):
        t.color(cs.hsv_to_rgb(i/25,0.3,1))
        draw_hexagon((size/2)-i*5)
        go_to((-(100-i*2.5), (100-i*4.5)))
go_to((-100,100))
drawDesign()
t.hideturtle()
t.done()


























