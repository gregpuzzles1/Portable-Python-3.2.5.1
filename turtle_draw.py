import turtle as t

# Part I
#------------------------------

def triangle2d(sides, length):
    for x in range(sides):
        t.forward(length)
        t.right(360/sides)
    t.exitonclick()

def square2d(sides, length):
    for x in range(sides):
        t.forward(length)
        t.right(360/sides)
    t.exitonclick()

def pentagon2d(sides, length):
    for x in range(sides):
        t.forward(length)
        t.right(360/sides)
    t.exitonclick()

def hexagon2d(sides, length):
    for x in range(sides):
        t.forward(length)
        t.right(360/sides)
    t.exitonclick()

triangle2d(3, 30)
square2d(4, 30)
pentagon2d(5, 30)
hexagon2d(6, 30)

# Part II
#------------------------------

class object2d:

    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side
        
    def draw(self, sides):
        self.sides = sides
        varx = 1
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        for m in range(sides):
            t.forward(self.side)
            t.right(360/sides)
        t.exitonclick()
        print("varx = ", varx)
    
class triangle2d(object2d):
    print("Drawing triangle now ...")

class square2d(object2d):
    print("Drawing square now ...")

class pentagon2d(object2d):
    print("Drawing pentagon now ...")

class hexagon2d(object2d):
    print("Drawing hexagon now ...")

class polygon2d(object2d):
    print("Drawing polygon now ...")

t1 = triangle2d(-300, 100, 30)  # Instantiation of triangle
t1.draw(3)                      # Call
s1 = square2d(-200, 100, 30)    # Instantiation of square
s1.draw(4)                      # Call
p1 = pentagon2d(-100, 100, 30)  # Instantiation of pentagon
p1.draw(5)                      # Call
h1 = hexagon2d(0, 100, 30)      # Instantiation of hexagon
h1.draw(6)                      # Call

# Extra Credit
#------------------------------

pg1 = polygon2d(-200, 200, 100) # Instantiation of N sided 2D object
pg1.draw(12)                    # Call
