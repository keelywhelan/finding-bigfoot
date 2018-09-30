#Keely Whelan
#EECS12
#HW 5

from graphics import *
import random
import time

#def move()
#moves Bigfoot by randomly incerementing/decrementing coords
#checks if Bigfoot is out of bounds or not moving 
#returns new coordinates of Bigfoot
def move(x, y):
    
    movX=random.randint(-1,1)
    movY=random.randint(-1,1)
    
    while(1>=(x+movX) or (x+movX)>=4 or 1>=(y+movY) or (y+movY)>=4 or (movX==0 and movY==0)):

        if(x+movX==x and y+movY==y):
            movX=random.randint(-1,1)
            movY=random.randint(-1,1)
        if(1>=(x+movX) or (x+movX)>=4):
            movX=random.randint(-1,1)
        if(1>=(y+movY) or (y+movY)>=4): 
           movY=random.randint(-1,1)
    newX=x+movX
    newY=y+ movY
    
    return(newX,newY)

#def showClick()
#leaves a yellow circle at user click point and blue rectangle in grid square user clicked
#returns coordinates of user click 
def showClick(win):


    #draw marks 
    gC = win.getMouse()
    converted_x = int(gC.x)
    converted_y = int(gC.y)
    redGridPnt1 = Point(converted_x,converted_y)
    redGridPnt2 = Point(converted_x+1,converted_y+1)
    redGrid = Rectangle(redGridPnt1,redGridPnt2)
    redGrid.setFill("lightblue")
    redGrid.draw(win)
    cirPoint=Point(gC.x,gC.y)
    clickCir=Circle(cirPoint,.3)
    clickCir.setFill("yellow")
    clickCir.draw(win)

    time.sleep(.3)
    
    #remove marks 
    redGrid.undraw()
    clickCir.undraw()

    return(gC.x,gC.y)

def main():
    win = GraphWin("Bigfoot-template",600,600)
    win.setCoords(0,0,6,6)
    
    #Times left information 
    numTry = 0
    
    #draw grid
    for i in range(5):
        index = i+1
        p1 = Point(index,1)
        p2 = Point(index,5)
        Line(p1,p2).draw(win)
        p3 = Point(1,index)
        p4 = Point(5,index)
        Line(p3,p4).draw(win)

    #Text
    pntMsg = Point(3,5.5 )
    txtMsg = Text(pntMsg, "click a cell to catch Bigfoot")
    txtMsg.setStyle("bold")
    txtMsg.setTextColor("blue")
   
    txtMsg.draw(win)

    pntMsgA = Point(3,.68 )
    pntMsgB = Point(3,.325) 
    
    #num tries text intialized 
    msg=("moves left: %d" %(5))
    tryMsg = Text(pntMsgA, msg)
    tryMsg.setStyle("bold")
    tryMsg.setTextColor("green")
    tryMsg.draw(win)

    #score intialized
    scMsg=("Score: %d" %100)
    scoreMsg = Text(pntMsgB, scMsg)
    scoreMsg.setStyle("bold")
    scoreMsg.setTextColor("blue")
    scoreMsg.draw(win)
    
    
    #initialize position of Bigfoot and show it
    initPnt = Point(1.5,1.5)
    bigfoot = Image(initPnt,"bigfoot.gif")
    bigfoot.draw(win)
    
    #repeat until 5 times

    # convert user click and mark the grid
    gCx,gCy=showClick(win)
    x=initPnt.x    
    y=initPnt.y
    converted_x = int(gCx)
    converted_y = int(gCy)
    while ((gCx>=1)and (gCx<=5) and (gCy>=1)and (gCy<=5)):
        
        # move the bigfoot
        x,y=move(x, y)
        bigfoot.undraw()
        newPoint=Point(x,y)
        bigfoot = Image(newPoint,"bigfoot.gif")
        bigfoot.draw(win)
        
        # check if bigfoot is there, break if so
        bigfootGridX=int(x)
        bigfootGridY=int(y)

        
        #game won. replace bigfoot image with bigfoot captured image 
        if ( bigfootGridX==converted_x and bigfootGridY==converted_y):
            aPnt = Point(bigfootGridX+.5,bigfootGridY+.5)
            capturedBigfoot = Image(aPnt,"bigfoot-captured.gif")
            bigfoot.undraw()
            capturedBigfoot.draw(win)
            txtMsg.undraw()
            bPnt=Point(3,5.5)
            txtMsg = Text(bPnt, "Congrats! Bigfoot is captured!")
            txtMsg.setStyle("bold")
            txtMsg.setTextColor("blue")
            txtMsg.draw(win)
            break
        
        numTry = numTry+1
        tries=(5-numTry)
        score=100-(20*numTry)
        msg=("moves left: %d" %(tries))
        tryMsg.setText(msg)
        scMsg=("Score: %d" %score)
        scoreMsg.setText(scMsg)
        
        #Game is over after 5 tries
        #replace bigfoot image with escaping Bigfoot image 
        if numTry >= 5:
            
            pnt = Point(bigfootGridX+.5,bigfootGridY+.5)
            escapeBigfoot = Image(pnt,"bigfoot-escape.gif")
            bigfoot.undraw()
            escapeBigfoot.draw(win)
            pntMsg = Point(3,5.5 )
            txtMsg.undraw()
            txtMsg = Text(pntMsg, "Bigfoot escaped!")
            txtMsg.setStyle("bold")
            txtMsg.setTextColor("blue")
            txtMsg.draw(win)
            break
       
        gCx,gCy=showClick(win)
        converted_x = int(gCx)
        converted_y = int(gCy)
        
    #close window with next user click           
    click = win.getMouse()
    win.close()
    
main()




        
