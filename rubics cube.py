import tkinter as tk
import numpy as np
import random

red    = "#FF0000"
green  = "#00FF00"
blue   = "#0000FF"
white  = "#FFFFFF"
yellow = "#FFFF00"
orange = "#FF6622"
global cube_colors
cube_colors = [orange, green, blue, yellow, white, red, "#000000"]

global circle_data      #3 list 0-2 row, 0-2 col, color
circle_data = [1,1,6]

def init_cube(): #solved for now
    global cube            #6 list of 3x3 arrays
    #[front, left, right, up, down, back][0-2 row][0-2 col]
    cube = np.array([ 
        np.full((3, 3), 0), #front - orange             
        np.full((3, 3), 1), #left  - green
        np.full((3, 3), 2), #right - blue
        np.full((3, 3), 3), #up    - yellow 
        np.full((3, 3), 4), #down  - white
        np.full((3, 3), 5)])#back  - red
    
    global squares_display #9 list of tk objects (grid and color stored)            
    squares_display = []
    for i in range(3): #row
        for j in range(3): #col
            square = tk.Canvas(root, width=150, height=150, bg=cube_colors[cube[0][i][j]], highlightthickness=1, highlightbackground="black")
            square.grid(row=i, column=j)
            squares_display.append(square)

    draw_circle()
    
def update_display():
    for i in range(3): #row
        for j in range(3): #col        
            squares_display[3*i+j].configure(bg=cube_colors[cube[0][i][j]])
        
def randomize_front():
    for i in range(3): #row
        for j in range(3): #col   
            cube[0][j][i] = random.randint(0, 5)  #Random color from list

def draw_circle():
    square = squares_display[3*circle_data[0]+circle_data[1]] #0-8 Index of where the circle is
    x0, y0, x1, y1 = 10, 10, 140, 140  #per square Coordinates
    global circle_id
    circle_id = square.create_oval(x0, y0, x1, y1, width=5, outline=cube_colors[circle_data[2]]) # Draw circle (and keep track of it, there's only one)
    
def delete_circle():
    square = squares_display[3*circle_data[0]+circle_data[1]] #0-8 Index of where the circle is
    square.delete(circle_id)

def interact():
    delete_circle()
    temp = circle_data[2]
    circle_data[2] = cube[0][circle_data[0]][circle_data[1]]
    cube[0][circle_data[0]][circle_data[1]] = temp
    draw_circle()
    update_display()
    
def move(direction): #move circle not on same color and trigger rotations
    delete_circle()
    if direction ==    'up':
        if circle_data[0] == 0:
            if circle_data[2] != cube[3][2][circle_data[1]]:
                cube_rotate('x')
                circle_data[0] = 2
        elif circle_data[2] != cube[0][circle_data[0]-1][circle_data[1]]:
            circle_data[0] -= 1
        
    elif direction ==  'down':
        if circle_data[0] == 2:
            if circle_data[2] != cube[4][0][circle_data[1]]:
                cube_rotate('-x')
                circle_data[0] = 0
        elif circle_data[2] != cube[0][circle_data[0]+1][circle_data[1]]:
            circle_data[0] += 1
        
    elif direction ==  'left':
        if circle_data[1] == 0:
            if circle_data[2] != cube[1][circle_data[0]][2]:
                cube_rotate('-y')
                circle_data[1] = 2
        elif circle_data[2] != cube[0][circle_data[0]][circle_data[1]-1]:
            circle_data[1] -= 1

    elif direction == 'right':
        if circle_data[1] == 2:
            if circle_data[2] != cube[2][circle_data[0]][0]:
                cube_rotate('y')
                circle_data[1] = 0
        elif circle_data[2] != cube[0][circle_data[0]][circle_data[1]+1]:
            circle_data[1] += 1

    draw_circle()

def cube_rotate(direction):
    #x,y,z rotate whole cube (basically double wide R,U,F turns)
    #cube face rearrange, faces to rotate, direction to rotate 
    #[0front, 1left, 2right, 3up, 4down, 5back][0-2 row][0-2 col]
    
    if   direction == 'x' :#see down
        inx = np.array([3,1,2,5,0,4])
        face_rotate(2,'clockwise')
        face_rotate(1,'counterclockwise')
        
    elif direction == '-x':#see up
        inx = np.array([4,1,2,0,5,3])
        face_rotate(1,'clockwise')
        face_rotate(2,'counterclockwise')
        
    elif direction == '-y' : #see right
        inx = np.array([1,5,0,3,4,2])
        face_rotate(3,'clockwise')
        face_rotate(4,'counterclockwise')
        
    elif direction == 'y':#see left
        inx = np.array([2,0,5,3,4,1])
        face_rotate(4,'clockwise')
        face_rotate(3,'counterclockwise')
        
    elif direction == 'z' :#spin c
        inx = np.array([0,3,4,2,1,5])
        face_rotate(0,'clockwise')
        face_rotate(5,'counterclockwise')
        
    elif direction == '-z':#spin cw
        inx = np.array([0,4,3,1,2,5])
        face_rotate(5,'clockwise')
        face_rotate(0,'counterclockwise')
    
    global cube 
    cube = cube[inx]
    update_display()

def layer_turn():
    #F,R,U,L,B,D 
    pass
    
def slice_turn():
    #M,E,S slice
    pass

def wide_layer_turn():
    #d<layer turn>
    pass

def face_rotate(face,direction):
    global cube
    if direction == 'clockwise':cube[face] = np.rot90(cube[face],1)
    elif direction == 'counterclockwise': cube[face] = np.rot90(cube[face],-1)

def randomize():
    bag = []
    for i in range(6):
        bag += [i,i,i,i,i,i,i,i,i] #it was misbehaving
    random.shuffle(bag)
    for face in cube:
        for row in range(3):
            for col in range(3):  
                face[row][col] = bag.pop() #Random color from list
    update_display()

def scramble():
    pass

def on_left_key(event):move('left')
def on_up_key(event):move('up')
def on_right_key(event):move('right')
def on_down_key(event):move('down')
    
def on_space_key(event):
    print(cube)
    interact()

root = tk.Tk()
root.title("cube screeeee")

init_cube()
randomize()

root.bind("<Left>", on_left_key)
root.bind("<Up>", on_up_key)
root.bind("<Right>", on_right_key)    
root.bind("<Down>", on_down_key)
root.bind("<space>", on_space_key)

root.mainloop()