from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super(Paddle, self).__init__()
      #  super().__init__()
        self.shape("circle")
        self.speed(0)
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.goto(position)

    def set_shape(self):
        self.shapesize(stretch_wid=1, stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
