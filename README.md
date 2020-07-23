# Simple_Turtle_Graphics_Interpreter
A simple implementation of an interpreter for a simple version of the Turtle Graphics Language. It allows users to enter programs using simple commands, and to see the appropriate graphical output on the screen.

## Requirements
#### Python 2.x

#### Pygame 
`$ pip install pygame` should be enough to install this library. If not then please refer to https://www.pygame.org/wiki/GettingStarted.

## Instructions
Save `$ chiraag_imperial_turtle.py` in your working directory.

Now simply run the script to start the interpreter

`$ python chiraag_imperial_turtle.py`

You will see a white display screen open up and a prompt `>>> ` in the terminal.

You can now enter the commands of the simple turtle graphics language and see the corresponding graphical outputs on the screen.

To exit the interpreter and the screen, type `>>> exit` and press enter.

## Sample Commands
The following sample command draws the graphical image below:
```
$ python chiraag_imperial_turtle.py 
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html

Welcome to Chiraag's simple turtle graphics interpreter!

Enter commands below:
>>> turtle trump boris modi
3 turtles have been created in the centre facing north.
>>> colour trump red
>>> colour boris blue
>>> colour modi green
>>> move trump 200
>>> left boris 90
>>> move boris 100
>>> right modi 90
>>> move modi 150
>>> pen boris up
>>> move boris 50
>>> pen boris down
>>> move boris 50
```
![](sample.png)

