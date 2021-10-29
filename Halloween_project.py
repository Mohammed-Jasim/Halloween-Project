#halloween art group project
#made by: William Bahou and Mohammed Jasim

#--------import statements-----
import turtle as tri
import random as rand
import turtle as trtl
import turtle as score_writer
#-------config-------
tri = tri.Turtle()
#--------initialize-------
new_xpos = 0
new_ypos = 0
score = 0

tri.shape("square")
tri.fillcolor("blue")
tri.color("blue")

trtl.speed(0)
trtl.penup()
trtl.goto(-250, 250)
trtl.color("red")
trtl.hideturtle()


score_writer.speed(0)
score_writer.penup()
score_writer.goto(-250, 250)
score_writer.hideturtle()




font_setup = ("Arial", 20, "normal")
timer = 15
counter_interval = 1000

def spot_clicked(x, y):
    update_score(x, y)
    change_position(x, y)
def update_score(x, y):
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
def countdown():
  global timer, timer_up
  trtl.clear()
  if timer <= 0:
    trtl.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    trtl.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    trtl.getscreen().ontimer(countdown, counter_interval)

score = 0
def change_position(x,y):
    tri.penup()
    global score
    score += 1
    new_xpos = rand.randint(-400, 400)
    new_ypos = rand.randint(-300, 300)
    tri.goto(new_xpos, new_ypos)
    print(str(new_xpos) + ", " + str(new_ypos))
    



while timer == 0:
    if score > 30:
        print("good_job!")
    else: 
        print("how you so bad")



#----events---------
tri.speed(0)

wn = trtl.Screen()

wn.bgpic('background.gif')
wn.addshape('candy1.gif')
tri.shape('candy1.gif')
tri.shapesize(0.5)
tri.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval)
while timer_up == True:
    if score < 30:
        wn.bgpic('scary.gif')

wn.mainloop()