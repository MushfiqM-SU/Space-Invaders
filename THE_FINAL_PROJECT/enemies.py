# 29297281
import stdio
import stddraw
from picture import Picture


# start position for first enemy
START_X = 10
START_Y = 537

# space between enemies
GAP_X = 55
GAP_Y = 85

# BOSS info
START_BOSS_X = 640
START_BOSS_Y = 575
BOSS_MAX_HEALTH = 10
BOSS_RADIUS = 40
BOSS_SPEED = 7


# Enemy info
ENEMY_RADIUS = 2
SPEED = 5
DROP = 75
BOUNDARY_MIN = 0
BOUNDARY_MAX = 1280


# End goal for enemies to win ( y-value)
GOAL_Y = 10


# Populate the enemies, a grid  ROW x COL
# Enemies have 3 elemants, x- value  , y-value, bool for alive
def init_enemies(COLS, ROWS):
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

    # "hit = false" assumes no ones hit the wall in the start
    hit = False

    for i in enemies:
        if not i["alive"]:
            continue  # if enemy hit with bullet, ignore it

        x_next = i["x"] + direction * SPEED  # finds the enemies next move

        if (
            x_next - ENEMY_RADIUS < BOUNDARY_MIN or x_next + ENEMY_RADIUS > BOUNDARY_MAX
        ):  # checks if the enemie's next move will be past the 2 boundarys,otherwise we need to change the direction and drop the entire grid of enemies.
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
            i["x"] += direction * SPEED

    return direction


# This function draws the alive enemies
def draw_enemies(enemies):

    picture = Picture("Enemy.png")

    for i in enemies:
        if not i["alive"]:
            continue

        stddraw.picture(picture, i["x"], i["y"])


# This function returns TRUE when all the enemies are dead
def all_dead(enemies):
    for e in enemies:
        if e["alive"]:
            return False
    return True


# initialize the boss, The boss has 5 elemnts
def init_BOSS():
    boss = []

    boss = {
        "x": START_BOSS_X,
        "y": START_BOSS_Y,
        "health": BOSS_MAX_HEALTH,
        "max_health": BOSS_MAX_HEALTH,
        "alive": True,
        "direction": 1,
    }
    return boss


def Update_BOSS(boss):
    if not boss["alive"]:
        return

    x_next = boss["x"] + boss["direction"] * BOSS_SPEED  # gets the boss next x value

    # Check if the boss needs to be droped and direction reversed, the same as the enemies
    if x_next - BOSS_RADIUS < BOUNDARY_MIN or x_next + BOSS_RADIUS > BOUNDARY_MAX:
        boss["direction"] = -boss["direction"]
        boss["y"] -= DROP

    boss["x"] += boss["direction"] * BOSS_SPEED

    # The boss dies when health reaches 0
    if boss["health"] <= 0:
        boss["health"] = 0
        boss["alive"] = False


# This function reduces the boss health
def boss_take_damage(boss, damage):
    if not boss["alive"]:
        return

    boss["health"] -= damage

    if boss["health"] <= 0:
        boss["health"] = 0
        boss["alive"] = False


def Draw_BOSS(boss):

    if not boss["alive"]:
        return

    picture = Picture("Boss.png")
    stddraw.picture(picture, boss["x"], boss["y"])


# These next 2 functions check whether the boss or enemies have hit the ground, thus they win
def enemies_reached_ground(enemy_list):
    for e in enemy_list:
        if e["alive"] and e["y"] <= GOAL_Y:
            return True
    return False


def boss_reached_ground(boss):
    if boss is None:
        return False
    return boss["alive"] and boss["y"] <= GOAL_Y


# This function checks whether the enemies have hit the player, and if yes then the enemies win
def deadzone(enemy_list, player_x, player_y, player_radius=35, enemy_radius=30):
    damage_Area = player_radius + enemy_radius

    for e in enemy_list:
        if not e["alive"]:
            continue

        distance = ((player_x - e["x"]) ** 2 + (player_y - e["y"]) ** 2) ** 0.5

        if distance < damage_Area:
            return True

    return False


# This function checks whether the enemies have hit the player, and if yes then the enemies win
def boss_hits_player(boss, player_x, player_y, player_radius=35):
    if boss is None:
        return False

    if not boss["alive"]:
        return False

    damage_Area = player_radius + BOSS_RADIUS
    distance = ((player_x - boss["x"]) ** 2 + (player_y - boss["y"]) ** 2) ** 0.5

    if distance < damage_Area:
        return True

    return False
