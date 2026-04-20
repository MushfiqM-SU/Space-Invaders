import sys, stdio, stddraw, stdaudio, math, threading, Player, enemies, TestColl
from picture import Picture

#Global variables to do checks for any changes in music
play_bg = True
current_song='menu_music'
music_changed=False # for if statements to trigger once
menu_mu=False
game_mu=False
over_mu=False
win_mu=False
enemy_direction = 1 # 1 == right, -1 == left

# creates enemy list (NB!!!! WILL HAVE TO ITERATE ROWS WHEN CREATE FINAL GAME LOOP)
enemy_list = enemies.init_enemies(2) #sets rows to 3 (0,1,2)


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
    global menu_mu, over_mu, game_mu, win_mu, player_x, enemy_direction, enemy_list
    
    bg_picture = Picture("funny.png")
    
    hold = 'm'
    stddraw.setCanvasSize(1280, 720)
    stddraw.setXscale(0, 1280)
    stddraw.setYscale(0, 720)
    
    threading.Thread(target=play_background_music, daemon=True).start()

    while True:
        
        stddraw.clear()
        hold = Player.inputs()
        
        if hold == 'm':
            menu()
        elif hold == 'x':
            break
        elif hold == 'p':
            game_over()
        elif hold == 'o':
            win_screen()
        else:
            game_mu=True 
            stddraw.picture(bg_picture, 1280/2, 720/2)
            # imports inputs and bullet specs from Player.py
            Player.bullet_movement()

                 # updates enemy direction using a function in the enemies.py file
            enemy_direction = enemies.update_enemies(enemy_list, enemy_direction)

                # Considers the player's bullets and the enemy list and returns a new bullet list minus the ones that hit an enemy.
            Player.bullets = TestColl.check_collisions(Player.bullets, enemy_list)

                # Each file controls it's own visuals
            Player.imagery()     # Draws the player and bullets
            enemies.draw_enemies(enemy_list)
            TestColl.current_score() # Draws the score

            if game_mu==True:
                change_music('game_music1')
                game_mu=False


               

        stddraw.show(20)

if __name__ == "__main__" : main()
