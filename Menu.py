import sys
import stddraw
import stdio
import stdaudio
import threading
from picture import Picture

#Global variables to do checks for any changes in music
play_bg = True
current_song='menu_music'
music_changed=False # for if statements to trigger once

menu_mu=False
game_mu=False
over_mu=False


def menu():
    #displays the main menu for the game
    global menu_mu
    if menu_mu==True:
        change_music('menu_music')
        menu_mu=False

    stddraw.clear(stddraw.DARK_BLUE)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setXscale(0,100)
    stddraw.setYscale(0,100)
    stddraw.setFontSize(40)  #Default of 16
    stddraw.text(50,90,"Title goes here")
    stddraw.setFontSize(20)
    stddraw.text(50,70,"Instructions")
    stddraw.text(50,60,"[A] move left, [D] move right")
    stddraw.text(50,50,"[Q] rotate left, [E] rotate right")
    stddraw.text(50,40,"[Space] to shoot, [X] to quit, [M] for menu")
    stddraw.text(50,20,"Press any key to start")
    stddraw.show(100)

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
        change_music('scary')
        over_mu=False

    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.RED)
    stddraw.setFontSize(80)
    stddraw.text(50,70,"GAME OVER")
    stddraw.setFontSize(40)
    stddraw.text(50,55,"Score:")
    stddraw.setFontSize(20)
    stddraw.text(50,45,"Menu: [M]   Exit: [X]")


def main(): # most of this main is just for testing

    global menu_mu, over_mu, game_mu
    rx=50
    ry=50
    vx=25
    vy=25
    stddraw.setCanvasSize(700,700)
    threading.Thread(target=play_background_music, daemon=True).start() # starts to play music

    while not stddraw.hasNextKeyTyped():
        menu()
   
    while True: #game loop to keep game running

        if stddraw.hasNextKeyTyped():
            temp=stddraw.nextKeyTyped()#stores the imput form user
            if temp == 'x':break

            if temp == 'm':
                menu_mu=True
                menu()

            else: # this else is for the most of the functions
                
                change_music('game_music')
                img_path="funny.png"
                pic=Picture(img_path)
                stddraw.clear()
                stddraw.picture(pic,50,50)
                stddraw.setPenColor(stddraw.BLACK) 

                if temp== 'd':
                    rx+=vx
                elif temp=='a':
                    rx-=vx
                elif temp=='w':
                    ry+=vy
                elif temp=='s':
                    ry-=vy
                stddraw.filledCircle(rx,ry,5)
            
                if temp=='p':
                    over_mu=True
                    game_over()
                    

        

        stddraw.show(500)


        
if __name__=='__main__':main()
