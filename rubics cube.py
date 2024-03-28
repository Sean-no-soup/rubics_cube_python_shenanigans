import tkinter as tk
import numpy as np
import random

red    = "#FF0000"
green  = "#00FF00"
blue   = "#0000FF"
white  = "#FFFFFF"
yellow = "#FFFF00"
orange = "#FF6622"

global colors
colors = [orange, green, blue, yellow, white, red]

def init_cube(): #solved for now
    global circle_pos      #2 list 0-2 row and col
    global squares_front   #3x3 array 0-5 
    global squares_back    #3x3 array 0-5
    global squares_left    #3x3 array 0-5
    global squares_right   #3x3 array 0-5
    global squares_up      #3x3 array 0-5
    global squares_down    #3x3 array 0-5
    global cube            #6 list of the above arrays
    global squares_display #9 list tk objects (grid and color stored)
    
    circle_pos = [1,1]

    squares_front = np.full((3, 3), 0) #orange
    squares_left  = np.full((3, 3), 1) #green
    squares_right = np.full((3, 3), 2) #blue
    squares_up    = np.full((3, 3), 3) #yellow
    squares_down  = np.full((3, 3), 4) #white
    squares_back  = np.full((3, 3), 5) #red
    
    cube = [squares_front,\
        squares_left,\
        squares_right,\
        squares_up,\
        squares_down,\
        squares_back,] #is there a specifc way to arrange this that would be more useful? if I even end up using it
     
    squares_display = []
    for i in range(3): #row
        for j in range(3): #col
            square = tk.Canvas(root, width=150, height=150, bg=colors[squares_front[j][i]], highlightthickness=1, highlightbackground="black")
            square.grid(row=i, column=j)
            squares_display.append(square)
    draw_circle()
    
def update_display():
    for i in range(3): #row
        for j in range(3): #col        
            squares_display[3*i+j].configure(bg=colors[squares_front[j][i]])
        
def randomize_front():
    for i in range(3): #row
        for j in range(3): #col   
            squares_front[j][i] = random.randint(0, 5)  #Random color from list

def draw_circle():
    square = squares_display[3*circle_pos[0]+circle_pos[1]] #0-8 Index of where the circle is
    x0, y0, x1, y1 = 10, 10, 140, 140  #per square Coordinates
    global circle_id
    circle_id = square.create_oval(x0, y0, x1, y1, width=5, outline='black') # Draw circle (and keep track of it)
    
def delete_circle():
    square = squares_display[3*circle_pos[0]+circle_pos[1]] #0-8 Index of where the circle is
    square.delete(circle_id)
    
def move(direction): #move pointer
    pass

def rotate(direction): #proto whole cube
    inx_left=[] #index list can re-order np arrays
    pass
    
def turn():
    #reverse of clockwise 
    #F,R,U,L,B,D face 
    #M,E,S slice
    #d<face> wide face
    #x,y,z whole cube (basically double wide R,U,F)
    pass

def on_left_key(event):move('left')
def on_up_key(event):move('up')
def on_right_key(event):move('right')
def on_down_key(event):move('down')
    
def on_space_key(event):
    update_display()

root = tk.Tk()
root.title("cube screeeee")

init_cube()

root.bind("<Left>", on_left_key)
root.bind("<Up>", on_up_key)
root.bind("<Right>", on_right_key)
root.bind("<Down>", on_down_key)
root.bind("<space>", on_space_key)

root.mainloop()
