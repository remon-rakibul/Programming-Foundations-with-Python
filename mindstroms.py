import turtle

def create_canvas():
    canvas = turtle.Screen()
    canvas.bgcolor('red')
    return canvas

def exit_canvas(canvas):
    canvas.exitonclick()

def draw_square():
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow', 'green')
    brad.speed(1)

    for line in range(4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.speed(1)

    angie.circle(100)

def draw_triangle():
    reggie = turtle.Turtle()
    reggie.shape('triangle')
    reggie.color('black')
    reggie.speed(1)

    for line in range(3):
        reggie.forward(120)
        reggie.left(120)

create_canvas()
draw_square()
draw_circle()
draw_triangle()
exit_canvas(create_canvas())
