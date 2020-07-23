"""
========================================================
Chiraag's simple interpreter of Turtle Graphics Language
========================================================
"""

import pygame	# Library to draw on the screen
import math	# Library for math and trignometric functions

# Initialize the game engine
pygame.init()

# Dictionary of acceptable colours in RGB
colours = {
           'black':(0,0,0),
           'white':(255,255,255),
           'blue':(0,0,255),
           'green':(0,255,0),
           'red':(255,0,0)
          }

# Set the screen
size = [800, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chiraag's Turtle Graphics")
screen.fill(colours['white'])
pygame.display.update()

# For looping until the user exits the interpreter
clock = pygame.time.Clock()
interpreter_on = True

# List of acceptable commands
commands = [
            'turtle', 
            'move', 
            'left', 
            'right', 
            'pen', 
            'colour', 
            'exit'
           ]

# Dictionary of turtles
turtles = {} 
# Note: Instead of defining a turtle object,
# I am using a dictionary for simplicity.
# Each turtle is list of 4 attributes namely:
# (1) position: list of two integers, like [30, 55],
#               which are x-y coordinates of the turtle
# (2) direction: float in degrees, like 42.5, which represents  
#                the direction in which the turtle is facing
# (3) colour: string, like 'green', which are acceptable 
#             colours as the keys of colours dictionary
# (4) pen_down: boolean, True means the pen is down and it will 
#               draw if the turtle moves while False means the 
#               pen is up and it won't draw if turtle moves 
#
# Example: turtles[name] = [pos,dir,col,pen_down] 
#                        = [[30,55],42.5,'green',True]

# Starting the interpreter
print("\nWelcome to Chiraag's simple turtle graphics interpreter!")
print("\nEnter commands below:")

while interpreter_on:

    # If user clicked close then to turn off the interpreter
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            interpreter_on=False

    # Reading user input
    text = raw_input('>>> ')
    tokens = text.split()
    if len(tokens)>0:

	# First token should be an acceptable command
        command = tokens[0]
        if command not in commands:
            print('Error: command not found')
    
	# To exit the interpreter
        elif command == 'exit':
            if len(tokens) == 1:
                interpreter_on = False     
            else:
                print('Error: there are tokens after the'+
                      ' exit command')

        # Creating one or more turtle objects
        elif command == 'turtle':

            if len(tokens)==1:
                print('Error: name of turtle(s) not found')

            else:
                unique_turtles = set(tokens[1:])
                num_of_turtles = len(unique_turtles)
                if num_of_turtles > 1:
                    print(str(num_of_turtles)+
                          ' turtles have been created in the'+
                          ' centre facing north.')
                else:
                    print('one turtle has been created in the'+
                          ' centre facing north.')
 
                # Adding new turtles to the turtles dictionary
                for name in unique_turtles:
                    turtles[name] = [
                                     # Middle of screen
                                     [size[0]/2,size[1]/2],
                                     0.0, 	# Facing north	
                                     'black',	# Pen's colour
                                     True	# Pen is down
                                    ]
                   
                    # Drawing a point in the middle of the screen 
                    pygame.draw.line(screen, 
                                     colours['black'], 
                                     [size[0]/2,size[0]/2], 	
                                     [size[0]/2,size[0]/2],
                                     2	# size of the point
                                    )

        # Turtle operations like move, left, right, pen, colour
        # require 3 tokens in the command and the second token
        # has to be a predefined turtle
        elif len(tokens) != 3:
            print('Error: incomplete command')
        elif tokens[1] not in turtles.keys():
            print('Error: turtle not found')

        # For 'move' operation, the third token should be an integer
        elif command == 'move':
            try:
                # steps or units to move
                steps = int(tokens[2])
                
                # Current position of the turtle
                start_pos = turtles[tokens[1]][0]

                # Current direction of the turtle in radians
                rad = math.radians(turtles[tokens[1]][1])

                # Current direction of the turtle in unit vector 
                direction = [math.sin(rad), -1*math.cos(rad)]

		# Final position of the turtle after the move
                end_pos = [start_pos[0]+(int(direction[0]*steps)), 
                           start_pos[1]+(int(direction[1]*steps))]

                # Draw a straight line if the pen is down
                if turtles[tokens[1]][3]:
                    pygame.draw.line(screen,
                                     colours[turtles[tokens[1]][2]],
                                     start_pos,
                                     end_pos,
                                     2 	# width of the line
                                    )
                
                # Update turtle's new position
                turtles[tokens[1]][0] = end_pos
           
            # If the steps is not an integer
            except:
                print('Error: steps to move should be an integer')


	# For 'left' operation, the third token should be a float  
        elif command == 'left':
            try:
                # rotation angle
                angle = float(tokens[2])
  
                # current direction
                start_direction = turtles[tokens[1]][1]
 
                # final direction after anticlockwise rotation
                end_direction = start_direction - angle
 
                # Update turtle's new direction
                turtles[tokens[1]][1] = end_direction

	    # If the angle is not a float
            except:
                print('Error: angle to rotate should be a'+
                      ' floating point number in degrees')


        # For 'right' operation, the third token should be a float
        elif command == 'right':
            try:
                # rotation angle
                angle = float(tokens[2])
  
                # current direction
                start_direction = turtles[tokens[1]][1]
 
                # final direction after clockwise rotation 
                end_direction = start_direction + angle
 
                # Update turtle's new direction
                turtles[tokens[1]][1] = end_direction
            
            # If the angle is not a float
            except:
                print('Error: angle to rotate should be a'+
                      ' floating point number in degrees')


        # For 'pen' operation, 
        # the third token should be 'up' or 'down' only
        elif command == 'pen':
            if tokens[2] not in ['up', 'down']:
                print("Error: the third token should be"+
                      " 'up' or 'down' only")
            else:
                if tokens[2] == 'up':
                    turtles[tokens[1]][3] = False
                else:
                    turtles[tokens[1]][3] = True

	# For 'colour' operation, 
        # the third token should be an acceptable colour
        elif command == 'colour':
            if tokens[2] not in colours.keys():
                print('Error: colour not found.\nChoose from'+
                      ' black, white, blue, green or red only.')
            else:
                turtles[tokens[1]][2] = tokens[2]

    pygame.display.update()

pygame.quit()
