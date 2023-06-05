'''more details of the instruction in the readme file'''
'''this is my code and it is incomplete. We should find a better code or ask teachers the right code '''

from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # TODO: set the orriginal squares
    player_next_left_x = 0
    player_next_top_y = 0
    goal_next_left_x = 360
    goal_next_top_y = 360
    player = canvas.create_rectangle(player_next_left_x,player_next_top_y,player_next_left_x+20,player_next_top_y+20,"blue")
    goal = canvas.create_rectangle(goal_next_left_x,goal_next_top_y,goal_next_left_x+20,goal_next_top_y+20,"orange")
    
    # Animate
    x=10
    y=0
    while True:
        canvas.move(player, x, y)
        time.sleep(0.1)
        # Detecting collisions
        now_x = canvas.get_left_x(player)
        now_y = canvas.get_top_y(player)
        if now_x>=400 :
            print('Go out of bounds, game is over!')
            break
        
        # key press
        # key = "ArrowLeft"
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            print('left arrow pressed!')
            x=-10
            y=0
            if now_x<=-20:
                print('Go out of bounds, game is over!')
                break
        if key == 'ArrowRight':
            print('right arrow pressed!')
            x=10
            y=0
            if now_x>=400:
                print('Go out of bounds, game is over!')
                break
        if key == 'ArrowUp':
            print('up arrow pressed!')
            y=-10
            x=0
            if now_y<=-20:
                print('Go out of bounds, game is over!')
                break
        if key == 'ArrowDown':
            print('down arrow pressed!')
            y=10
            x=0
            if now_y>=400:
                print('Go out of bounds, game is over!')
                break
        
        if now_x == goal_next_left_x and now_y == goal_next_top_y:
            print("Get the goal, go to next round")
            player_next_left_x = random.randint(0, 380)
            player_next_top_y = random.randint(0, 380)
            goal_next_left_x = random.randint(0, 380)
            goal_next_top_y = random.randint(0, 380)
            canvas.moveto(player, player_next_left_x, player_next_top_y)
            canvas.moveto(goal, goal_next_left_x, goal_next_top_y)

if __name__ == '__main__':
    main()
