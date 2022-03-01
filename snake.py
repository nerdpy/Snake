from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.squares = []  #list vytvořených čtverců - had je složený ze tří čtverečků
        self.create_snake()

    def create_snake(self):
        for position in POSITIONS:
            self.add_square(position)   #na každou pozici přidá jeden čtvereček


    def add_square(self, position):
        sq = Turtle("square")
        sq.penup()
        sq.color("white")
        sq.goto(position)
        self.squares.append(sq)


    def extend(self):
        """add a square to a snake"""
        self.add_square(self.squares[-1].position()) #na poslední pozici v listu čtverečků a
                                        # zjistíme jeho pozici - position()



    def move(self):
        """3.čtverec se posune na 2.pozici a ten se posune na 1.pozici"""
        for sq_num in range(len(self.squares) - 1, 0,
                            -1):  # start=2, stop=0, step=-1 - jdem od 2 do 0 (v listu suares - position
            new_x = self.squares[sq_num - 1].xcor()  # sq_num je 2-1 =) 1
            new_y = self.squares[sq_num - 1].ycor()
            self.squares[sq_num].goto(x=new_x, y=new_y)  # sq_num je 2- range začíná na dvojee
        self.squares[0].forward(MOVE_DISTANCE)  # musíme posunout také první čtvereček

    def up(self): #aby se nemohl obrátit ze směru dolů hned nahoru
        if self.squares[0].heading() != DOWN:
            self.squares[0].setheading(UP)

    def down(self):
        if self.squares[0].heading() != UP:
            self.squares[0].setheading(DOWN)

    def left(self):
        if self.squares[0].heading() != RIGHT:
            self.squares[0].setheading(LEFT)

    def right(self):
        if self.squares[0].heading() != LEFT:
            self.squares[0].setheading(RIGHT)

