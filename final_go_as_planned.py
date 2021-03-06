import numpy

##path = numpy.array([
##    [-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0],
##    [-01.0,000.0,999.0,-01.0,-01.0,-01.0,-01.0,999.0,-01.0,-01.0],
##    [-01.0,-01.0,999.0,999.0,-01.0,-01.0,999.0,-01.0,999.0,-01.0],
##    [-01.0,-01.0,-01.0,999.0,999.0,999.0,-01.0,-01.0,999.0,-01.0],
##    [-01.0,-01.0,-01.0,999.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0],
##    [-01.0,-01.0,-01.0,999.0,999.0,-01.0,-01.0,999.0,999.0,-01.0],
##    [-01.0,-01.0,-01.0,-01.0,999.0,999.0,-01.0,999.0,-01.0,-01.0],#end
##    [-01.0,-01.0,-01.0,-01.0,-01.0,999.0,-01.0,-01.0,999.0,-01.0],
##    [-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,999.0,999.0,999.0,-01.0],
##    [-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0]
##    ])
path = numpy.array([
    [-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0],
    [-01.0,000.0,999.0,-01.0,999.0,999.0,-01.0,-01.0,-01.0,-01.0],
    [-01.0,-01.0,999.0,-01.0,-01.0,-01.0,-01.0,999.0,999.0,-01.0],
    [-01.0,-01.0,-01.0,999.0,999.0,999.0,999.0,-01.0,999.0,-01.0],
    [-01.0,-01.0,-01.0,999.0,-01.0,-01.0,-01.0,-01.0,999.0,-01.0],
    [-01.0,-01.0,-01.0,999.0,999.0,-01.0,-01.0,999.0,999.0,-01.0],
    [-01.0,-01.0,-01.0,-01.0,999.0,999.0,-01.0,999.0,-01.0,-01.0],#end
    [-01.0,-01.0,-01.0,-01.0,-01.0,999.0,-01.0,-01.0,999.0,-01.0],
    [-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,999.0,999.0,999.0,-01.0],
    [-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0,-01.0]
    ])
pathpath = numpy.array([
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

global wind
wind = [('r',5.0,10.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,10.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,10.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,10.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,10.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,10.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0),('d',9.0,1.0),('l',3.0,4.0),('u',1.0,5.0),('r',1.0,6.0),('r',5.0,3.0),('u',1.0,6.0),('d',5.0,2.0)]    #direction,speed,time
global windTime
global windCount
windTime = 0
windCount = 0





def weights():
    global windTime
    global windCount
    global lMove
    global rMove
    global uMove
    global dMove
    time = windTime
    count = windCount
    windTime = windTime+1
    windDetails = wind[windCount]
    #print windCount
    direction = windDetails[0]
    magnitude = windDetails[1]
    if direction == 'r':
        lMove = 10 - magnitude*0.2
        rMove = 10 + magnitude*0.3
        uMove = 10 + magnitude*0.05
        dMove = 10 + magnitude*0.05
    elif direction == 'l':
        lMove = 10 + magnitude*0.3
        rMove = 10 - magnitude*0.2
        uMove = 10 + magnitude*0.05
        dMove = 10 + magnitude*0.05
    elif direction == 'u':
        lMove = 10 + magnitude*0.05
        rMove = 10 + magnitude*0.05
        uMove = 10 + magnitude*0.3
        dMove = 10 - magnitude*0.2
    elif direction == 'd':
        lMove = 10 + magnitude*0.05
        rMove = 10 + magnitude*0.05
        uMove = 10 - magnitude*0.2
        dMove = 10 + magnitude*0.3
    if windTime == wind[windCount][2]:
        windCount = windCount + 1
        windTime = 0
        


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
    weights()
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
    for k in range (0,9):
        for i in range (0,9):
            for j in range (0,9):
                neighbours((i,j))

itteration()
print path
finalPath = path
for i in range (0,9):
    for j in range (0,9):
        if finalPath[i][j] != -01.0:
            finalPath[i][j] = 1.0
finalPath[1][1] = 0.0
