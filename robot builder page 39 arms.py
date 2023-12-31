import turtle as t

def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
      t.forward(horizontal)
      t.right(90)
      t.forward(vertical)
      t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')

#feet
t.goto(-100,-150)
rectangle(50,20,'blue')
t.goto(-30,-150)
rectangle(50,20,'blue')

#legs
t.goto(-25,-50)
rectangle(15,100,'grey')
t.goto(-55,-50)
rectangle(-15,100,'grey')

#body
t.goto(-90,100)
rectangle(100,150,'red')

#arms
t.goto(-150,70)
rectangle(60,15,'grey')
t.goto(-150,110)
rectangle(15,40,'grey')

t.goto(10,70)
rectangle(60,15,'grey')
t.goto(55,110)
rectangle(15,40,'grey')
    
    

    
