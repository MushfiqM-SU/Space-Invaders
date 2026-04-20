import stdio
import stddraw
from picture import Picture

# varibles used to control the grid and enemy infomation
COLS = 5


# start position for first enemy 
START_X = 10
START_Y = 700

# space between enemies
GAP_X = 55
GAP_Y = 55


ENEMY_RADIUS = 2
SPEED = 5
DROP = 30
BOUNDARY_MIN = 0
BOUNDARY_MAX = 1280


# Populate the enemies, a grid  ROW x COL 
def init_enemies(ROWS):
    enemies = []

    for i in range(ROWS):
        for j in range(COLS):
            x = START_X + j * GAP_X
            y = START_Y - i * GAP_Y

            enemy = {"x": x, "y": y, "alive": True}
            enemies += [enemy]

    return enemies

# This function finds the next positon for the entire grid of enemys, it checks the boundaries, thus determies whether the next position 
# for the grid is forward, downward, backward. Direction = 1 (left to right) , = -1 ( right to left). Also because the enemies store a
# boolean for alive, it always checks that and does nothing if it is dead. (it just skips the dead enemies when changeing the position of the enemies) 
def update_enemies(enemies, direction):
    
    #"hit = false" assumes no ones hit the wall in the start
    hit = False
    

    for i in enemies:
        if not i["alive"]:      
            continue                # if enemy hit with bullet, ignore it
        
        x_next = i["x"] + direction*SPEED               #checks enemies next move
        
        if x_next - ENEMY_RADIUS < BOUNDARY_MIN or x_next + ENEMY_RADIUS > BOUNDARY_MAX:
            hit = True          

    if hit:
        direction = -direction
        
        for i in enemies:
            if not i["alive"]:
                continue
            i["y"] -= DROP

    else:
        for i in enemies:
            if not i["alive"]:
                continue
            i["x"] += direction*SPEED

    return direction
            


    

# this function draws the alive enemies 
def draw_enemies(enemies):

    picture = Picture('enemy.png')

    for i in enemies:
        if not i["alive"]:
            continue

        stddraw.picture(picture,i["x"], i["y"])


def all_dead(enemies):
    for e in enemies:
        if e["Alive"]:
            return False
        return True



