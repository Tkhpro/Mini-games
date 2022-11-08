import turtle as tur


t = tur.Turtle()
t.speed(50)

thickness = 1


def up():
    t.setheading(90)
    t.forward(10)
def down():
    t.setheading(-90)
    t.forward(10)
def left():
    t.setheading(180)
    t.forward(10)
def right():
    t.setheading(0)
    t.forward(10)
def upordown():
    if t.isdown():
        t.up()
    else:
        t.down()
def thickness_add():
    global thickness
    thickness +=1
    t.width(thickness)
def thickness_reduce():
    global thickness
    thickness -= 1
    if thickness<1:
        thickness +=1
    else:
        t.width(thickness)
def circle():
    for i in range(360):
        t.forward(1)
        t.right(1)
def spiral():
    for i in range(160):
        t.forward(i/10)
        t.left(15)
def square():
    for i in range(4):
        t.forward(10)
        t.right(90)
def clear():
    t.clear()
def black():
    t.color('black')
def red():
    t.color('red')
def orange():
    t.color('orange')
def yellow():
    t.color('yellow')
def green():
    t.color('green')
def blue():
    t.color('blue')
def indigo():
    t.color('indigo')
def violet():
    t.color('violet')
def initial_position():
    t.up()
    t.goto(0,0)
    t.down()

t.screen.onkeypress(up,'Up')
t.screen.onkeypress(down,'Down')
t.screen.onkeypress(left,"Left")
t.screen.onkeypress(right,'Right')
t.screen.onkeypress(upordown,'space')
t.screen.onkeypress(circle,'c')
t.screen.onkeypress(spiral,'s')
t.screen.onkeypress(thickness_add,'p')
t.screen.onkeypress(thickness_reduce,'l')
t.screen.onkeypress(square,'k')
t.screen.onkeypress(black,'1')
t.screen.onkeypress(red,'2')
t.screen.onkeypress(orange,'3')
t.screen.onkeypress(yellow,'4')
t.screen.onkeypress(green,'5')
t.screen.onkeypress(blue,'6')
t.screen.onkeypress(indigo,'7')
t.screen.onkeypress(violet,'8')
t.screen.onkeypress(clear,'n')
t.screen.onkeypress(initial_position,'i')
t.screen.listen()

t.screen.mainloop()