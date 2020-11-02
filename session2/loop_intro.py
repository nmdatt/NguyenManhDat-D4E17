from turtle import *
speed(-1)
for goc in range(3,6): 
    for i in range(goc):
        forward(100)
        left(360/goc)

mainloop()