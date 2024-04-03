"""Snake, classic arcade game """
# Import the Turtle , random and freegame module for graphics , random no and freegame module
from turtle import *  
from random import randrange 
from freegames import square, vector  

# Initialize the food position ,snake with a single segment at a specific position and direction of movement
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    # Check if the snake hits 
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # Check if the snake eats the food
    if head == food:
        #print the length of the snake
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Draw snake
    for body in snake:
        square(body.x, body.y, 9, 'black')
    # Draw food
    square(food.x, food.y, 9, 'green')

    update()
    # call the move function again after a specified time interval
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
# arrow key to the change function to control the snake's movement
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()

done()
print("MY ID IS 22CS003 - PRATHAM")

