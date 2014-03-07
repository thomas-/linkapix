from math import sin, cos, pi, ceil

X = 0
Y = 1

def mirror( pos, axis=0 ):
    newPos = pos[:]
    newPos[axis] *= -1
    return newPos
    
def mirrorPath( path, axis=0 ):
    return [mirror(pos,axis) for pos in path]

def rotate( pos, angle ):
    return [ int(round(pos[X]*cos( angle ) - pos[Y]*sin( angle ))), int(round(pos[X]*sin( angle ) + pos[Y]*cos( angle ))) ]
    
def rotatePath( path, angle=pi/2 ):
    return [ rotate( pos, angle ) for pos in path ]
    
def getRotations( path ):
    return [ rotatePath( path, (pi/2)*i ) for i in range(4) ]

def getRelativePos( origin, destination ):
    return [destination[X] - origin[X], destination[Y] - origin[Y]]

def reversePath( path ):
    tempPath = path[:]
    tempPath.reverse()
    return [getRelativePos(tempPath[0],pos) for pos in tempPath]
    
    
def getPathExtensions( path ):
    exts = []
    for i in range(-1,2):
        for j in range(-1,2):
            if abs(i) + abs(j) == 1:
                newPath = path[:]
                newPos = [ newPath[-1][X] + i, newPath[-1][Y] + j ]
                if newPos not in newPath and newPos[X] >= 0 and newPos[Y] >= 0:
                    newPath.append( newPos )
                    exts.append( newPath )

    return exts

def remDups( plist ):
    dots = 0
    progress = 0
    normalizedPathWorth = 100/float(len(plist))
    uq = []
    while plist:
        while dots < ceil(progress):
            dots += 1
            print ".",
            
        
        pp = plist.pop()
        if pp not in uq: uq.append( pp )
        

        progress += normalizedPathWorth
        
    print ""
    return [pt.pattern for pt in uq]
    
    
    
def getUniquePaths( length ):
    print "Starting.."
    p = genPaths( length )
    print "Paths generated. Extracting patterns.."
    pl = getPatternList( p )
    print "Patterns extracted. Removing duplicates.."
    nodups = remDups( pl )
    print "Duplicates removed, operation complete"
    return nodups
    
def printPath( path ):
    size = len(path)
    for j in range(size):
        for i in range(size):
            if [i,j] in path: print 'X',
            else: print ' ',
        print ''
    print ''
    
                
def genPaths( length ):
    pathList = [ [[0,0]] ]
    while( len( pathList[0] ) < length ):
        newPathList = []
        for path in pathList:
            newPaths = getPathExtensions( path )
            newPathList.extend( newPaths )
        
        pathList = newPathList
    return pathList
    
def getPatternList( paths ):
    unique = []
    patterns = [Pattern( path ) for path in paths]
    return patterns
'''
    p = patterns.pop()
    if p not in unique: unique.append( p )
    return [pt.pattern for pt in unique]
'''
    
    
class Pattern:
    def __init__( self, pattern ):
        self.pattern = pattern
        
    def __eq__( self, other ):
        matchPattern = other.pattern[:]
        rot = getRotations( matchPattern )
        mrot = getRotations( mirrorPath( matchPattern ))
        
        pt = self.pattern
        rpt = reversePath( pt )
        
        if pt in rot or pt in mrot or rpt in rot or rpt in mrot: return True
        return False
        '''
        if self.pattern in getRotations( matchPattern ): return True
        if self.pattern in getRotations( mirrorPath( matchPattern )): return True
        
        return False
        '''
        
    def __ne__( self, other ):
        return not self.__eq__( other )
        
        
