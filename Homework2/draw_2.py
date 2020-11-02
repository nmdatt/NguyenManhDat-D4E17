from turtle import *

for i in range(3,7):
    for j in range(i):
        if (i%2==1):
            pencolor('blue')
            
        else:
            pencolor('red')
        forward(100)
        left(360/i)
mainloop()
