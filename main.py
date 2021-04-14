import turtle


class LSystem2D:
    def __init__(self, t: turtle.Turtle, axiom, width, length, angle):
        self.axiom = axiom
        self.state = axiom
        self.width = width
        self.length = length
        self.angle = angle
        self.rules = {}  # dictionary for storing the rules of forming curves
        self.t = t
        self.t.pensize(self.width)

    def add_rule(self, *rules):
        for key, value in rules:
            self.rules[key] = value

    def generate_path(self, n_iter):
        for i in range(n_iter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key, value.lower())

            self.state = self.state.upper()

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
            elif move == 'S':
                self.t.up()
                self.t.fd(self.length)
                self.t.down()
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
f_len = 5
angle = 90
axiom = "F-F-F-F"
# **********************

l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
# l_sys.add_rule(("F", "F+F--F+F"))
l_sys.add_rule(("F", "F+FF-FF-F-F+F+FF-F-F+F+FF+FF-F"))
l_sys.generate_path(2)
l_sys.draw_turtle((-500, 0), 0)
