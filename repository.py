import sys, stdio, stddraw, stdaudio, math, threading
from picture import Picture

#Global variables to do checks for any changes in music
play_bg = True
current_song='menu_music'
music_changed=False # for if statements to trigger once
menu_mu=False
game_mu=False
over_mu=False
win_mu=False
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

def inputs(key):
    global player_x, player_speed, player_width, player_height, aim_angle, aim_speed, bullet_speed, bullets 

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

def menu():
    #displays the main menu for the game
    global menu_mu
    if menu_mu==True:
        change_music('menu_music')
        menu_mu=False

    stddraw.clear(stddraw.DARK_BLUE)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(40)  #Default of 16
    stddraw.text(640,648,"Title goes here")
    stddraw.setFontSize(20)
    stddraw.text(640,504,"Instructions")
    stddraw.text(640,432,"[A] move left, [D] move right")
    stddraw.text(640,360,"[Q] rotate left, [E] rotate right")
    stddraw.text(640,288,"[Space] to shoot, [X] to quit, [M] for menu")
    stddraw.setFontSize(30)
    stddraw.text(640,144,"[S] to start")

def play_background_music():
    # This runs music in seperate loop to game
    global music_changed
    while play_bg:
        stdaudio.playFile(current_song)
        music_changed=False

def change_music(new_song_file):
    #pretty self-explainitory
    global current_song, music_changed
    if current_song != new_song_file:
        current_song = new_song_file
    #Used since stdaudio doesn't have a built in change function
    #The new song will play after current song finishes

def game_over():
    #gives the gameover screen
    global over_mu
    if over_mu==True:
        change_music('scary1')
        over_mu=False

    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.RED)
    stddraw.setFontSize(80)
    stddraw.text(640,504,"GAME OVER")
    stddraw.setFontSize(40)
    stddraw.text(640,396,"Score:")
    stddraw.setFontSize(20)
    stddraw.text(640,324,"Menu: [M]   Exit: [X]")

def win_screen():

    global win_mu
    if win_mu==True:
        change_music('win')
        win_mu=False

    stddraw.clear(stddraw.CYAN)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(80)
    stddraw.text(640,504,"YOU WON, CONGRATS!!")
    stddraw.setFontSize(40)
    stddraw.text(640,396,"Score")
    stddraw.setFontSize(20)
    stddraw.text(640,360,"Menu: [M] Exit: [X]")


def main():
    global menu_mu, over_mu, game_mu, win_mu, player_x
    
    #bg_picture = Picture("funny.png")
    
    hold = 'm'
    stddraw.setCanvasSize(1280, 720)
    stddraw.setXscale(0, 1280)
    stddraw.setYscale(0, 720)
    
    threading.Thread(target=play_background_music, daemon=True).start()

    while True:
        
        stddraw.clear()

        
        if stddraw.hasNextKeyTyped():
            temp = stddraw.nextKeyTyped()
            if temp == 'x':
                break
            elif temp == 'm':
                hold = 'm'
                menu_mu = True
            elif temp == 'p':
                hold = 'p'
                over_mu = True
            elif temp == 'o':
                hold = 'o'
                win_mu = True
            elif temp == 's':
                hold = 'game'
            
            if hold == 'game':
                inputs(temp)
                game_mu=True
        
        if hold == 'm':
            menu()
        elif hold == 'p':
            game_over()
        elif hold == 'o':
            win_screen()
        else:
            #stddraw.picture(bg_picture, 1280/2, 720/2)
            bullet_movement()
            imagery()
            if game_mu==True:
                change_music('game_music1')
                game_mu=False

        stddraw.show(20)

if __name__ == "__main__" : main()
