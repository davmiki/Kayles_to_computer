from turtle import Screen
from paddle import Paddle
from find_solution import Find_solution
import time
import random
from scoreboard import Scoreboard
list_ball = []
AZAZEL = 500
timer= None
click_list = []
click_list_old = []
ans = []
change_turn_to_computer = False
screen = Screen()
player_situation = True


def  is_all_0(listt):
    for item in listt:
        if item !=0:
            return False
    return True

def choice_random():
    end_choice =False
    while not end_choice:
        i = random.randint(0,len(list_ball)-1)
        if list_ball[i] == 1:
            print("i in random = ",i)
            end_choice= True
            return i

def manage_actors(nubc):
    global click_list
    global click_list_old
    global player_situation
    global change_turn_to_computer
    if not player_situation:
        print("This is Computer turn-The Program wil finish -No one winned!! ")
    else:  #Plyer Turn
        # print(f"len(click_list) = {len(click_list)}")
        # print(f"len(click_list_old) = {len(click_list_old)}")
        if len(click_list) - len(click_list_old) > 2:
            print("You pressed 3 or more time.You allow to remove maximum 2 buttos Prgram Halt!!")
            exit(1)
        print(f"click_list in manage layer = {click_list}")
        print(f"click_list_old iin manage layer = {click_list_old}")
        nubc = click_list[-1] # nubc = number of clicked button
        print(f"button_number_clicked = {nubc}")
        list1_new = remove_button(nubc, list_ball)
        print(f"list1_new = {list1_new}")
        if len(click_list) > 1:
            if abs(click_list[-1] - click_list[-2]) != 1:
                print("ILLEGAL MOVE ,YOU CLICKED ON 2 NON ADJACENT BUTTON!!!!")
                scoreboard.non_adjacent_press()
                exit(1)
        no_of_ball = len(list_ball)
        if is_all_0(list_ball):
            print("You are the WINNER!!!!")
            scoreboard.you_win()
            scoreboard.congratulation()
            exit(0)
        print(f"change_turn_to_computer = {change_turn_to_computer}")
        if len(click_list) - len(click_list_old) == 1:
            if nubc < no_of_ball-1 and list_ball[nubc+1] == 1 or nubc > 0 and list_ball[nubc -1] == 1:
                print("You can remove one more adjacent button")
                scoreboard.one_press_note()
        print("FINISH from main")
        if len(click_list) - len(click_list_old) == 2 or change_turn_to_computer == True or \
                nubc < no_of_ball-1 and list_ball[nubc+1] == 0 and nubc > 0 and list_ball[nubc -1] == 0:
            print("Now it is the Computer time!!!")
            scoreboard.actor_react()
            player_situation = False
            ans = find_solution.find_sol(list1_new)
            print(f"ANS = {ans}")
            if ans[0] == -1:
                print("THERE IS NO SOLUTION")
                num_to_remove = choice_random()
                print(f" num_to_remove = { num_to_remove}")
                x_org = paddle[num_to_remove].xcor()
                paddle[num_to_remove].goto(x_org, AZAZEL)  # remove button i
                list_ball[num_to_remove] = 0
                screen.update()
            else:
                if len(ans)> 0:
                    x_org = paddle[ans[0]].xcor()
                    paddle[ans[0]].goto(x_org, AZAZEL)  # remove button i
                    list_ball[ans[0]]=0
                    screen.update()
                    if len(ans) == 2:
                        paddle[ans[1]].goto(x_org, AZAZEL)  # remove button i
                        list_ball[ans[1]] = 0
                        screen.update()
            if is_all_0(list_ball):
                print("The Computer Win !!!")
                scoreboard.computer_win()
                scoreboard.comfort()
                exit(0)
            else:
                player_situation =True
                change_turn_to_computer = False
                click_list=[]
                click_list_old = click_list.copy()
                wait_for_mouse()

def wait_for_mouse():
    global click_list
    global click_list_old
#    print(f"len(click_list_old) = {len(click_list_old)}")
    if len(click_list) == len(click_list_old) :
        screen.ontimer(wait_for_mouse, t=100)
    else:
        print("CLICKER!!!")
        print("FRIDAY")
        print(f"click_list in wait mouse = {click_list}")
        manage_actors(click_list[-1])
        if len(click_list) - len(click_list_old) == 1:
            screen.ontimer(wait_for_mouse, t=100)


def calc_numbers_list(list_bal):
    liss = []
    i = -1
    print(f"list_bal in main = {list_bal}")
    print(f"len(list_bal) = {len(list_bal)}")
    while i < len(list_bal) - 1:
        #    print("i = ",i)
        i += 1
        if int(list_bal[i]) == 0:
            liss.append(0)
        else:  # !=0
            total = 1
            while i < len(list_bal) - 1 and int(list_bal[i + 1]) == 1:
                #        print("i in while = ", i)
                i += 1
                #         print("i in while after inc = ", i)
                total += 1
            liss.append(total)
    print(f"liss = {liss}")
    return liss

def calc_lists(lis):
  #  print(f"lis in calc = {lis}")
    global list_ball
    list_ball = []
    #Caculate list of balls=>list_ball and list of the number that point each ball=>list_of_i
    for i in range(len(lis)):
  #     print(f"len of lis in calc = {len(lis)}")
        if lis[i] == 0:
            list_ball.append(0)
        else: #item != 0
            for j in range(lis[i] ):
                list_ball.append(1)
    #print(f"list_balli in calc = {list_ball}")
    return list_ball


def remove_button(num_of_button,list_ball_old):
    print(f"list_ball_old  in remove button= {list_ball}")
    x_org = paddle[num_of_button].xcor()
  #  time.sleep(0.25)
    paddle[num_of_button].goto(x_org,AZAZEL)# remove button i
    list_ball[num_of_button]=0
    print(f"list_ball_new = {list_ball}")
    list1_new = calc_numbers_list(list_ball)
    print(f"list1_new = {list1_new}")
    return list1_new


def clicked(x, y):
  #  print("You clicked ", x, ",", y)
    wait_for_click = False
    global change_turn_to_computer
#    global count1
    for i in range(len(list_ball)):
        if paddle[i].distance(x, y) < 20:
   #         print(f"Yoe clicked on paddle[{i}]")
            click_list.append(i)
    #        print("click_list = ", click_list)
    if paddle[len(list_ball)].distance(x, y) < 20:
  #      count1 = 0
        print("YOU CLICKED ON CHANGR TURN TO COMPUTER")
        print("VERY VERY GOOD")
        change_turn_to_computer = True

     #       remove_button(i,list_ball)

def to_canonic(list):
    # Append 0 to lis_to_exa
    listemp = list.copy()
    for item in listemp:
        if item  == 0:
            list.remove(item)
    print(f"list = {list}")
    lis1 = []
    for  item in list:
            lis1.append(item)
            lis1.append((0))
    del lis1[-1]
    return lis1
#START
#def do_staff():
click_list = []
lis_to_exam=[]
# answer1 = (screen.textinput("Kayles Game","משחק קאילס- כל אחד יכול להוריד כפתור אחד או שני כפתורים צמודים. \nמי שמוריד אחרון הוא המנצח, נא לחץ על כפתור 'אוקיי' להתחלת המשחק  "))
# print(answer1)

answer = (screen.textinput("Kayles Game", "Enter list of numbers with space seperation"))
print(answer)
#Input list to examine
lis_to_exam= [int(x) for x in answer.split()]
#lisss= lis_to_exam.copy()
print(f"lis_to_exam in main = {lis_to_exam}")
lis_canon = to_canonic(lis_to_exam)
print(f"lis_canon = {lis_canon}")
list1 = lis_canon
#list1 = lisss
print("list1 ",list1)
#Intialize

screen.bgcolor("black")
screen.setup(width=1300, height=500)
screen.title("Kayles")
screen.tracer(0)
scoreboard = Scoreboard()
scoreboard.docs_kayles()
screen.update()
time.sleep(4)
scoreboard.r_point()
# scoreboard.l_point()
# scoreboard.one_press_note
screen.update()
list_ball = calc_lists(list1)

no_of_balls= len(list_ball)
print(f"list_ball in main= {list_ball}")
print(f"no_of_balls in main= {no_of_balls} list_ball ={list_ball}")
if len(list_ball) >48:
    print("The graphi support up to 23 balls maximum,TRY AGAIN!!")
    exit(1)
more_ball =  len(list_ball) >24  and  len(list_ball) <=48
paddle = []
space = 0
jj = -1
x_shift = int(no_of_balls*50 /2)
if more_ball:
    x_shift = int(no_of_balls*25/2)
print("x_shift = ",x_shift)

print("no_of_balls = ",no_of_balls)
print("len(list_ball) = ",len(list_ball))
jj= -1
#for i in range(-x_shift +25  , x_shift , 25):
if more_ball:
    step = 25
else:
    step = 50
for i in range(-x_shift , x_shift, step):
    jj +=1
    print("jj near paddle = ",jj)
    print("i near paddle = ", i)
    padd = Paddle((i, 0))
    if more_ball:
        padd.set_shape()
    paddle.append(padd)
    if list_ball[jj] == 0:
        paddle[jj].goto(i,AZAZEL)
    screen.update()
padd = Paddle((-230, 100))
padd.shape("square")
padd.hideturtle()
padd.write('לאחר מחיקה ראשונה: אם תרצה עבור למחשב  => ' ,align='center', font=("Courier", 15, "bold"))
padd = Paddle((50, 100))
padd.shape("square")
paddle.append(padd)
print(f"len of paddle = {len(paddle)}")

screen.update()

print('the computer will start now')
screen.update()
print("Your turn now-take 1 or 2 adjacent buttons")
#print("END!!!")
#do_staff()
click_list_old =click_list.copy()
print(f"list1 bef find_sol..  = {list1}")
find_solution = Find_solution(list1)

wait_for_mouse()

screen.onscreenclick(clicked)

game_is_on = True
while game_is_on:
    screen.update()

# screen.mainloop()
