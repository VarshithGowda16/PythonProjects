from turtle import Turtle as T,Screen as S

tim = T()
scr = S()

num_cir = 360 #it is the number of repetations required for 360 completion
angle = 5
draw = num_cir / angle
tim.speed(0)#0 is the fastest,0.5 is moderate speed,1 is minimum speed

tim.shape("circle")

for _ in range(int(draw)):
    tim.circle(100)
    tim.left(angle)


scr.exitonclick()