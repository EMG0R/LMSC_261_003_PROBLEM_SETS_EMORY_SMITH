#establishes function

def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    
#background
    fill(193, 154, 107)
    rect(0, 0, 320, 150)
    
#white keys    
    fill(250)
    rect(40, 90, 20, 60)
    rect(60, 90, 20, 60)
    rect(80, 90, 20, 60)
    rect(100, 90, 20, 60)
    rect(120, 90, 20, 60)
    rect(140, 90, 20, 60)
    rect(160, 90, 20, 60)
    rect(180, 90, 20, 60)
    rect(200, 90, 20, 60)
    rect(220, 90, 20, 60)
    rect(240, 90, 20, 60)
    rect(260, 90, 20, 60)
    rect(280, 90, 20, 60)
    rect(300, 90, 20, 60)
    
#wk outline    
    fill(0)
    rect(40, 90, 1, 60)
    rect(60, 90, 1, 60)
    rect(80, 90, 1, 60)
    rect(100, 90, 1, 60)
    rect(120, 90, 1, 60)
    rect(140, 90, 1, 60)
    rect(160, 90, 1, 60)
    rect(180, 90, 1, 60)
    rect(200, 90, 1, 60)
    rect(220, 90, 1, 60)
    rect(240, 90, 1, 60)
    rect(260, 90, 1, 60)
    rect(280, 90, 1, 60)
    rect(300, 90, 1, 60)
    rect(40, 90, 280, 1)
    
#black keys
    fill(0)
    rect(50, 90, 20, 30)
    rect(70, 90, 20, 30)
    rect(90, 90, 20, 30)
    rect(110, 90, 20, 30)
    rect(130, 90, 20, 30)
    rect(150, 90, 20, 30)
    rect(170, 90, 20, 30)
    rect(190, 90, 20, 30)
    rect(210, 90, 20, 30)
    rect(230, 90, 20, 30)
    rect(250, 90, 20, 30)
    rect(270, 90, 20, 30)
    rect(290, 90, 20, 30)
    
#bk outline
    fill(250)
    rect(50, 90, 1, 30)
    rect(70, 90, 1, 30)
    rect(90, 90, 1, 30)
    rect(110, 90, 1, 30)
    rect(130, 90, 1, 30)
    rect(150, 90, 1, 30)
    rect(170, 90, 1, 30)
    rect(190, 90, 1, 30)
    rect(210, 90, 1, 30)
    rect(230, 90, 1, 30)
    rect(250, 90, 1, 30)
    rect(270, 90, 1, 30)
    rect(290, 90, 1, 30)

#switches
    fill(250)
    rect(10, 105, 5, 30)
    rect(25, 105, 5, 30)
    
#knobs
    fill(0)
    circle(20, 25, 15)
    circle(20, 65, 15)
    circle(50, 25, 15)
    circle(50, 65, 15)
    circle(80, 25, 15)
    circle(80, 65, 15)
    circle(110, 25, 15)
    circle(110, 65, 15)
    circle(140, 25, 15)
    circle(140, 65, 15)
    circle(170, 25, 15)
    circle(170, 65, 15)
    circle(200, 25, 15)
    circle(200, 65, 15)
    circle(230, 25, 15)
    circle(230, 65, 15)
    circle(260, 25, 15)
    circle(260, 65, 15)
    circle(290, 25, 15)
    circle(290, 65, 15)
    pop()

#establishes basic stuff
def setup():
    size(400,400)
    noStroke()

#draws 4 synths at half scale
def draw():
    drawObject(0 ,0 , 0.5)
    drawObject(190 ,0 , 0.5)
    drawObject(0 ,100 , 0.5)
    drawObject(190 ,100 , 0.5)
