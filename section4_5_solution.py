# Section 4 Solutions
# Random Circles
from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 40
N_CIRCLES = 40

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(N_CIRCLES):
        draw_random_circle(canvas)
        
def draw_random_circle(canvas):
    x = random.randint(0, CANVAS_WIDTH-CIRCLE_SIZE)
    y = random.randint(0, CANVAS_HEIGHT-CIRCLE_SIZE)
    color = random_color()
    canvas.create_oval(x, y, x+CIRCLE_SIZE, y+ CIRCLE_SIZE, color)
    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()

    
    
# Section 5 Solutions
from graphics import Canvas

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 0.01

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # animation loop 
    while True:
        # get the locations of the mouse
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        # check that the mouse location is in bounds
        if mouse_x >= 0 and mouse_x <= CANVAS_WIDTH and mouse_y >=0 and mouse_y <= CANVAS_HEIGHT:
            
            # draw a circle for where the mouse is
            canvas.create_oval(mouse_x, mouse_y, mouse_x + CIRCLE_SIZE, mouse_y + CIRCLE_SIZE, 'cyan')
        
        # typical animation loop code 
        # canvas.mainloop()  # Ignore this line for current solutions.
        time.sleep(DELAY)


if __name__ == "__main__":
    main()
    
    
    
    
    
