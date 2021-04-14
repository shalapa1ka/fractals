import turtle


class LSystem2D:
    def __init__(self, t: turtle.Turtle, axiom, width, length, angle):
        self.axiom = axiom
        self.state = axiom
        self.width = width
        self.length = length
        self.angle = angle
        self.t = t
        self.t.pensize(self.width)

    def draw_turtle(self, start_pos, start_angle):
        # **********************
        turtle.tracer(1, 0)  # The fast and furious mode
        self.t.up()
        self.t.setpos(start_pos)
        self.t.seth(start_angle)
        self.t.down()
        # **********************
        for move in self.state:
            if move == 'F':
                self.t.fd(self.length)
            elif move == '+':
                self.t.left(self.angle)
            elif move == '-':
                self.t.right(self.angle)

        turtle.done()


# **********************
# Screen setup
width = 1200
height = 600
screen = turtle.Screen()
screen.setup(width, height, (1920 - width) // 2, (1080 - height) // 2)
# **********************


# **********************
# turtle setup / create
t = turtle.Turtle()
t.ht()

pen_width = 2
f_len = 50
angle = 60
# **********************
