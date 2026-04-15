import math, sys, stdio, stddraw
from picture import Picture


Player = Picture("Player1.png")
Bullet = Picture("Bullet1.png")

# Set players starting position and speed
player_x = 1280 / 2
player_y = 50
player_width = 50
player_height = 77
player_speed = 50

# Aiming specifications
aim_angle = math.pi / 2
aim_speed = 0.1

# Bullet specifications
bullets = []
bullet_speed = 30


def inputs():
    global player_x, player_speed, player_width, player_height, aim_angle, aim_speed, bullet_speed, bullets

    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()

        # Player movement
        if key == "a" and player_x - player_width > 0:
            player_x -= player_speed

        elif key == "d" and player_x + player_width < 1280:
            player_x += player_speed

            # Aiming
        elif key == "j" and aim_angle < math.pi:
            if aim_angle > math.pi:
                aim_angle = math.pi
            aim_angle += aim_speed
        elif key == "l" and aim_angle > 0:
            if aim_angle < 0:
                aim_angle = 0
            aim_angle -= aim_speed

            # Shooting
        elif key == " ":
            vx = bullet_speed * math.cos(aim_angle)
            vy = bullet_speed * math.sin(aim_angle)
            bullets.append([player_x, player_y + player_height, vx, vy])


def bullet_movement():
    global bullets
    # Storing and updating position of each bullet on screen
    new_bullets = []

    for b in bullets:
        b[0] += b[2]
        b[1] += b[3]

        if 0 <= b[0] <= 1280 and 0 <= b[1] <= 720:
            new_bullets.append(b)

    bullets = new_bullets


def imagery():
    # Drawing player
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.picture(Player, player_x, player_y)

    # Drawing bullets
    for b in bullets:
        Degrees = math.degrees(aim_angle)
        stddraw.picture(Bullet, b[0], b[1])


def main():

    # Making the pop-up fullscreen
    stddraw.setCanvasSize(1280, 720)
    # Making the co-ordinate system match the canvas size
    stddraw.setXscale(0, 1280)
    stddraw.setYscale(0, 720)

    # Start of "Game loop"
    while True:
        stddraw.clear()  # sets screen to white for each frame
        stddraw.picture(Picture("Forest.jpg"), 1280 / 2, 720 / 2)

        inputs()
        bullet_movement()
        imagery()

        stddraw.show(10)  # shows each frame for 20ms (game runs at 1000ms/20ms = 50fps)


if __name__ == "__main__":
    main()
