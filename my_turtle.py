from turtle import *

speed(10)
bgcolor('black')
color('red')

for i in range(250):
    circle(100, 90 - i)
    lt(i)
done
