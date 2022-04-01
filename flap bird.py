from sense_hat import SenseHat
from random import randint
from time import sleep

num = randint(0,10)
sense = SenseHat()

r = (255,0,0)
b = (0,0,255)
garet = (97,35,35)
mr = (203, 76, 78)

game_over = False

x = 0

y = 0

score = 0

scroll_speed = .05



matrix = [[b for column in range(8)] for row in range(8)]


def flatten(matrix):
    flattened = [pixel for row in matrix for pixel in row]
    return flattened

def gen_pipes(matrix):
    for row in matrix:
        row[-1] = r
    gap = randint(1, 6)
    matrix[gap][-1] = b
    matrix[gap - 1][-1] = b
    matrix[gap + 1][+1] = b
    return matrix

def move_pipes(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i + 1]
        row[-1] = b
    return matrix
    
matrix = gen_pipes(matrix)

def draw_astronaut(event):
    global x
    global y
    global game_over
    sense.set_pixel(x, y, garet)
    if event.action == "pressed":
        if event.direction == "up" and y > 0:
            y -= 1
        elif event.direction == "down" and y < 7:
            y += 1
        elif event.direction == "right" and x < 7:
            x += 1
        elif event.direction == "left" and x > 0:
            x -= 1
    sense.set_pixel(x, y, garet)
    if matrix[y][x] == r:
        game_over = True
    
def check_collision(matrix):
    if matrix[y][x] == r:
        return True
    else:
        return False

sense.stick.direction_any = draw_astronaut
    
while not game_over:
    matrix = gen_pipes(matrix)
    score = score + 1
    if check_collision(matrix):
        game_over = True
    for i in range(3):
        matrix = move_pipes(matrix)
        sense.set_pixels(flatten(matrix))
        sense.set_pixel(x, y, garet)
        if check_collision(matrix):
            game_over = True
        sleep(.75)
sense.show_message('You lose' + 'Your score is ' + str(score), text_colour=mr, back_colour=b, scroll_speed =.08)