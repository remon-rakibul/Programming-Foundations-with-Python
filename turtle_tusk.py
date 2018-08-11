import turtle

def draw_square(some_turtle):
    #for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(120)
        some_turtle.forward(100)
        some_turtle.right(120)
        some_turtle.forward(100)
        some_turtle.right(120)
        some_turtle.forward(100)
        some_turtle.right(120)

window = turtle.Screen()
window.bgcolor('red')

flower = turtle.Turtle()
flower.shape('classic')
flower.color('blue')
#flower.speed(1)
for i in range(36):
    draw_square(flower)
    flower.right(10)
