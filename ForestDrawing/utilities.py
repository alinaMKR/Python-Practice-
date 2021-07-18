import turtle #import turtle to implement graphics
import math #to find height of triangle
import random #to generate random size of trees


#set window size and color
w_width = 800
w_height = 800
bg_color = 'aliceblue' #background color simulating sky
turtle.setup(w_width, w_height)
turtle.bgcolor(bg_color)

turtle.speed(0)

#set global variables
x = -400 #global x coordinates, invisible before click within the border
y = -400 #global y coordinates, invisible before click within the border
click = 0 #declaring mode(tree/bird) global
tilt_angle = 0 #tilt angle value

#set border for interactive window
def set_border(point_x ,point_y, window_size, pen_size, angle):
    turtle.penup()
    turtle.goto(point_x,point_y)
    turtle.pendown()
    turtle.pensize(pen_size)
    #draw a square using for loop
    for i in range (4):
        turtle.forward(window_size)
        turtle.left(angle)
    turtle.hideturtle()#make turtle invisible

#write text for selectors
def write_word (word, start_x,start_y):
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.write(word, align='center', font=('Times New Roman', 12, 'bold'))

#create function to draw selectors
def draw_circle(centre_x, centre_y, radius, pen_color, fill_color):
    #set pen up if turtle is down
    turtle.pensize(1)
    if turtle.isdown():
        turtle.penup()
    #go to identified location
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.goto(centre_x, centre_y)
    turtle.pendown()
    turtle.circle(radius) #draw circle
    turtle.end_fill()


#create function to handle mouse click
def handle_click(x, y):
    global click #call global click
    print('detected a click at', x, y)
    turtle.hideturtle() #hide turtle
    turtle.penup()#hide turtle`s pen
    turtle.goto(x,y) #move turtle to click`s coordinates
    turtle.speed(0) #set animation on fastest speed
    if (-10 <= x <= 10 and 370 <= y <= 390): #check whether Tree selector was clicked
        draw_circle(0, 370, 10, 'black', 'royalblue') #mark Tree selector as chosen
        draw_circle(100, 370, 10, 'black', 'aliceblue') #mark Bird selector as disable
        click=1 #set Tree mode
        return click ##return mode
    #enable Tree drawings for Tree mode and default mode
    if click==0 or click==1:
        if (-350<x<350 and -350<y<350):#check if click`s within drawing border
            turtle.penup() #hide turtle`s pen
            turtle.goto(x,y) #move turtle to click`s coordinates
            turtle.pendown() #set turtle pen down
            r = random.uniform(0.7,1.3) #generate random number within from 0.7 to 1.3
            draw_triangle(r*100,'green', 'green') #draw tree leaves
            draw_rectangle(r*15, r*80,'sienna','sienna') #draw tree stem
    if(90 <= x <=110 and 370 <= y <= 390): #check whether Bird selector was clicked
        draw_circle(100, 370, 10, 'black', 'royalblue') #mark Bird selector as chosen
        draw_circle(0, 370, 10, 'black', 'aliceblue')#mark Tree selector as disable
        bird_icon() #display current bird icon
        click=2 #set Bird mode
        return click #return mode
    #enable Bird drawings for Bird mode
    if click==2:
        if (-350<x<350 and -350<y<350):#check if click`s within drawing border
            draw_bird(x, y, 'indigo', 'indigo')#make Bird`s stamp
            bird_icon() #display current tilt of turtle(Bird), no stamp


#draw triangles for tree leaves
def draw_triangle(width, pen_color, fill_color):
    #set pen up if turtle is down
    turtle.hideturtle()
    height =((width*math.sqrt(3))/2)#math formula to find height of regular triangle
    #set colors
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    for i in range (3): #start drawing 3 triangles in a row
        #draw regular triangle
        turtle.forward(width/2) #start from base centre
        turtle.left(120) #make angle of 60 degdrees
        turtle.forward(width)
        turtle.left(120)
        turtle.forward(width)
        turtle.left(120)
        turtle.forward(width/2)#finish with base centre
        for j in range (1): #exclude 3rd triangle
            turtle.left(90)
            turtle.penup()
            turtle.forward(height*0.4)#this is the point of a new triangle base (40% overlapping)
            turtle.right(90)
    turtle.end_fill()
    turtle.penup()#hide turtle`s pen
    turtle.right(90)
    turtle.forward((height*0.4)*3)#returns turtle to first triangle base`s centre

#create funtion to draw tree stem
def draw_rectangle(width, height, pen_color, fill_color):
    #set colors
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    #draw rectangle
    turtle.forward(height)#goes to rectangle`s base centre
    turtle.left(90)
    turtle.pendown()
    turtle.forward(width/2)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width/2)#finishes with rectangle`s base centre
    turtle.end_fill()



#create function to handle left key press
def left_keypress():
    global tilt_angle #calls global tilt
    tilt_angle += 20 #increases tilt angle on 20 degress
    turtle.tiltangle(tilt_angle) #turns tilt left on 20 degress
    bird_icon() #displays new position of bird
    return tilt_angle # returns new tilt


#create function to handle right key press
def right_keypress():
    global tilt_angle #calls global tilt
    tilt_angle -= 20 #decreases tilt angle on 20 degress
    turtle.tiltangle(tilt_angle) #turns tilt right on 20 degress
    bird_icon()#displays new position of bird
    return tilt_angle # returns new tilt


#set turtles icon as a bird to leave stamps
def draw_bird (bird_x, bird_y, fill_color, pen_color):
    turtle.penup()
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.goto(bird_x, bird_y)
    turtle.pendown()
    turtle.register_shape('bird', ((-22,-39),(-20,-7),(-7,3),(-11,7),(-12,9),(-11,10),(-9,10),(-3,7),
        (10,24),(30,16),(13,18),(4,0),(14,-6),(6,-13),(0,-4),(-14,-13),(-22,-39)))
    turtle.shape('bird')
    turtle.showturtle()
    turtle.end_fill()
    turtle.stamp() #saves bird on the screen


#set turtles icon as a bird
def bird_icon():
    pen_color='indigo'
    fill_color = 'indigo'
    turtle.penup()
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.goto(-340,370)
    turtle.pendown()
    turtle.register_shape('bird', ((-22,-39),(-20,-7),(-7,3),(-11,7),(-12,9),(-11,10),(-9,10),(-3,7),
        (10,24),(30,16),(13,18),(4,0),(14,-6),(6,-13),(0,-4),(-14,-13),(-22,-39)))
    turtle.shape('bird')
    turtle.showturtle()
    turtle.end_fill()
