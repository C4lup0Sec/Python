from turtle import *
bgcolor("black")
speed(0)
colors=["blue", "magenta", "cyan", "yellow", "lime", "red", "violet", "white"]

def draw_spiral_flower():
    for i in range(1000):
        pencolor(colors[i % 8])
        circle(i * 0.5, 45)
        left(45)
        if i % 20 ==0:
            circle(i * 0.5, 45)

draw_spiral_flower()
done()