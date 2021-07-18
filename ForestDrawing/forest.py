import turtle #import turtle module
import utilities #import utilities module to implement its functions

turtle.title("Wonderful Forest") #name the window

def main ():

    #set  border
    utilities.set_border(-350,-350,700,3,90)

    #draw circles for tree and bird selectors
    utilities.draw_circle(0,370,10,'black', 'royalblue')
    utilities.draw_circle(100,370,10,'black','aliceblue')

    #write texts for tree and bird selectors
    utilities.write_word('Tree', 40,370)
    utilities.write_word('Bird', 140,370)

    #track mouse click
    handle_click = utilities.handle_click
    turtle.listen()
    turtle.onscreenclick(handle_click, 1)#assign function name as parametr


    ##track key presses:

    #track left key press
    left_keypress = utilities.left_keypress
    turtle.listen()
    turtle.onkey(left_keypress, 'Left')

    #track right key press
    right_keypress = utilities.right_keypress
    turtle.listen()
    turtle.onkey(right_keypress, 'Right')

main()
