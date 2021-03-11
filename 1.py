import numpy

path = numpy.array([
    [-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0],
    [-01.0,000.0,999.0,-01.0,-01.0,-01.0,-01.0,999.0,-01.0,-01.0],
    [-01.0,-01.0,999.0,999.0,-01.0,-01.0,999.0,-01.0,999.0,-01.0],
    [-01.0,-01.0,-01.0,999.0,999.0,999.0,-01.0,-01.0,999.0,-01.0],
    [-01.0,-01.0,-01.0,999.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0],
    [-01.0,-01.0,-01.0,999.0,999.0,-01.0,-01.0,999.0,999.0,-01.0],
    [-01.0,-01.0,-01.0,-01.0,999.0,999.0,-01.0,999.0,-01.0,-01.0],#end
    [-01.0,-01.0,-01.0,-01.0,-01.0,999.0,-01.0,-01.0,999.0,-01.0],
    [-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,999.0,999.0,999.0,-01.0],
    [-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0]
    ])


global lMove
global rMove
global uMove
global dMove



def weights():
    lMove = 1.0
    rMove = 1.0
    uMove = 1.0
    dMove = 1.0


def move(current,neighbour):
    l=0.0   #direction of movement is left
    r=0.0
    u=0.0
    d=0.0
    #print "current :   ", current
    #print " neighbour :   ", neighbour
    x = current[0] - neighbour[0]
    y = current[1] - neighbour[1]
    #print x,"    ",y
    if x < 0:
        d = x*(-1.0)
    else:
        u = x
    if y < 0:
        r = y*(-1.0)
    else:
        l = y
    updateCost = path[neighbour[0],neighbour[1]]+(((lMove*l) **2 + (uMove*u) **2 + (rMove*r) **2 + (dMove*d) **2) ** 0.5)
    #print updateCost
    if path[current[0],current[1]] > updateCost:
            path[current[0],current[1]] = updateCost


def neighbours(current):
    possibleLink = numpy.array([(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)])
    #print "possibleLink:  ",possibleLink
    for i in range (0,8):
        possibleLink[i][0] = possibleLink[i][0] + current[0]    #downward in path(y direction)
        possibleLink[i][1] = possibleLink[i][1] + current[1]    #sideward in path(x direction)
    #print "possibleLink:  ",possibleLink
    for i in range (0,8):
        if path[possibleLink[i][0],possibleLink[i][1]] != -01.0:
            #print path[possibleLink[i][0],possibleLink[i][1]]
            #print possibleLink[i][0]
            #print possibleLink[i][1]
            move(current,possibleLink[i])
            #print 2

def itteration():
    for i in range (0,9):
        for j in range (0,9):
            neighbours((i,j))



itteration()
print path
