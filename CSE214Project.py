import sys
import stddraw
import stdio
from picture import Picture

def main():
    while True:
        while not stddraw.hasNextKeyTyped():
            stddraw.clear()
            stddraw.setXscale(0,1)
            stddraw.setYscale(0,1)
            stddraw.setFontSize(24)  #Default of 16
            stddraw.text(0.5,0.9,"Title goes here")
            stddraw.setFontSize(16)
            stddraw.text(0.5,0.7,"Instructions")
            stddraw.text(0.5,0.6,"[A] move left, [D] move right")
            stddraw.text(0.5,0.5,"[Q] rotate left, [E] rotate right")
            stddraw.text(0.5,0.4,"[Space] to shoot, [X] to quit")
            stddraw.text(0.5,0.2,"Press any key to start")
            stddraw.show(100)
            
    
        img_path="funny.png"
        pic=Picture(img_path)

        stddraw.clear()
        stddraw.picture(pic,0.5,0.5)
        stddraw.show(500)

        if stddraw.hasNextKeyTyped():
            done=stddraw.nextKeyTyped()
            if done == 'x':break

if __name__=='__main__':main()
