from turtle import Turtle as T,Screen as S

tim = T()
scr = S()

num_cir = 360 #it is the number of repetations required for 360 completion
tim.speed(0)#0 is the fastest,0.5 is moderate speed,1 is minimum speed
angle = 5

tim.shape("circle")

for _ in range(36):#because 360 divided by 5 is 72 this is the number os circles drawn
    tim.circle(100)
    tim.left(angle)


scr.exitonclick()