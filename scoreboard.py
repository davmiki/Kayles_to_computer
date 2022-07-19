from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
#        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = "מחק כפתור מהלוח"
        self.r_score = "שחקן ימני ראשון"
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 200)
        self.write(self.l_score, align="center", font=("Courier", 24, "bold"))
        self.goto(350, 200)
        self.write(self.r_score, align="center", font=("Courier", 26, "bold"))

    def update_scoreboard1(self):
        self.clear()
        # self.goto(-300, 200)
        # self.write(self.l_score, align="center", font=("Courier", 24, "bold"))
        self.goto(100,0)
        self.write(self.r_score, align="center", font=("Courier", 27, "bold"))

    def l_point(self):
        self.l_score ="שמי דוד"
        self.update_scoreboard()

    def right_player_turn(self):
        self.r_score = "כעת תור השחקן הימני"
        self.update_scoreboard()

    def player_turn(self):
        self.r_score = "כעת תור השחקן להוריד כפתור/ים"
        self.update_scoreboard()

    def r_point(self):
        self.r_score = "כעת תור השחקן להוריד כפתורים"
        self.update_scoreboard()

    def docs(self):
        self.r_score = " הנחיות למשחק  קאילס הפוך \n כל אחד יכול להוריד כפתור אחד \nאו שני כפתורים צמודים \nמי שמוריד אחרון הוא המפסיד "
        self.update_scoreboard1()

    def docs_kayles(self):
        self.r_score = "ההנחיות למשחק \n------משחק קאילס ------\n כל אחד יכול להוריד כפתור אחד \nאו שני כפתורים צמודים \nמי שמוריד אחרון הוא המנצח\n "
        #   self.r_score = "ההנחיות למשחק nמשחק קאילס \n כל אחד יכול להוריד כפתור אחד \nאו שני כפתורים צמודים \nמי שמוריד אחרון הוא המנצח\n "
        self.update_scoreboard1()


    def docs_dawson(self):
        self.r_score = "  ***** משחק  דאוסון *****\n כל אחד יכול להוריד רק שני כפתורים צמודים   \n****  מי שמוריד אחרון הוא המנצח ****** "
        #    self.r_score = " הנחיות למשחק  קאילס הפוך \n כל אחד יכול להוריד כפתור אחד \nאו שני כפתורים צמודים \nמי שמוריד אחרון הוא המפסיד "
        self.update_scoreboard1()

    def left_player_turn(self):
        self.r_score = "כעת תור השחקן השמאלי"
        self.update_scoreboard()

    def one_press_note(self):
        self.l_score = "באפשרותך למחוק עוד או להעביר מחשב"
        self.update_scoreboard()

    def one_press_note_dw(self):
        self.l_score = "אתה נדרש למחוק עוד כפתור"
        self.update_scoreboard()
    def non_adjacent_press(self):
        self.l_score = "לחצת על יותר מכפתור אחד"
        self.update_scoreboard()

    def left_win(self):
        self.r_score = "!!השחקן השמאלי ניצח!!"
        self.update_scoreboard()

    def you_win(self):
        self.r_score = "!אתה ניצחת את המחשכ, הידד!!"
        self.update_scoreboard()

    def computer_win(self):
        self.r_score = "!!המחשב ניצח !"
        self.update_scoreboard()


    def right_win(self):
        self.r_score = "!!השחקן הימני ניצח!!"
        self.update_scoreboard()

    def actor_react(self):
        self.l_score = "כעת תורך שוב למחוק  כפתורים"
        self.update_scoreboard()

    def congratulation(self):
        self.l_score = " !! כ ל  ה כ ב ו ד !!"
        self.update_scoreboard()

    def comfort(self):
        self.l_score = " נקווה בפעם הבאה"
        self.update_scoreboard()