import turtle as t
t.shape("turtle")

t.title("day_01_02")

"""
t.color("orange")
t.width(5)

t.forward(100) # =t.fd(100)

t.color("blue")
t.circle(100)
"""

t.bgcolor("gray")
t.color("darkorange")
t.width(3)

t.fillcolor("gold")
t.begin_fill()

t.fd(100)
t.left(120)
t.fd(100)
t.left(120)
t.forward(100)
t.left(120)

t.end_fill()

####################################

t.up()
t.goto(100, 100)
t.down()

t.color("green")
t.fillcolor("yellow")

t.begin_fill()

t.fd(100); t.lt(90)
t.fd(100); t.lt(90)
t.fd(100); t.lt(90)
t.fd(100); t.lt(90)

t.end_fill()

####################################

t.up()
t.goto(-150, -150)
t.down()

t.color("red")
t.fillcolor("cyan")

t.begin_fill()

for x in range(5):
    t.fd(100); t.lt(72)
# t.fd(100); t.lt(72)
# t.fd(100); t.lt(72)
# t.fd(100); t.lt(72)
# t.fd(100); t.lt(72)

t.end_fill()

####################################

t.done()