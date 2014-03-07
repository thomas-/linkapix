"""Solver for G52GRP Link-Pix Project
	Classes:
		PathContainer() - To be implemented
		Cell( int[] pos ) - Holds individual cell information
		Grid( int xsize, int ysize ) - Cell container/manupulator, main control class
		
	Current functionality:
		Cell range searching procedure
		Basic Grid configuration validity checking
		
	Container 'testInfo' contains sample set of cell positions to allow quick instantiation of a valid Grid
"""

from cellReader import Cell, CsvCellReader, JsonCellReader
from pathContainer import PathContainer, getRelativePos, getAbsolutePos
from math import pi, cos, sin
from random import randint
from constants import *
import sys
'''
def getRelativePos( origin, destination ):
	return [destination[X] - origin[X], destination[Y] - origin[Y]]

def getAbsolutePos( origin, offset ):
	return [origin[X] + offset[X], origin[Y] + offset[Y]]
	

class PathContainer:
	def __init__( self ):
		self.paths =   {1: [ [[0,0]] ],
						2: [ [[0,0],[0,1]] ],
						3: [ [[0,0],[0,1],[0,2]], [[0,0],[0,1],[1,1]] ], #, [[0,0],[0,1],[-1,1]] ],
						4: [ [[0,0],[0,1],[0,2],[0,3]], [[0,0],[0,1],[0,2],[1,2]], [[0,0],[0,1],[1,1],[1,2]], [[0,0],[0,1],[1,1],[1,0]] ],
						5: [ [[0,0],[0,1],[0,2],[0,3],[0,4]], [[0,0],[0,1],[0,2],[0,3],[1,3]], [[0,0],[0,1],[0,2],[1,2],[1,3]], [[0,0],[0,1],[0,2],[1,2],[2,2]], [[0,0],[0,1],[0,2],[1,2],[1,1]], [[0,0],[0,1],[1,1],[1,2],[2,2]], [[0,0],[0,1],[1,1],[2,1],[2,2]], [[0,0],[0,1],[1,1],[2,1],[2,0]] ],
						6: [],
						7: [],
						8: []
						}
						
		self.addMirrors();
	
	def mirror( self, pos, axis=0 ):
		newPos = pos[:]
		newPos[axis] *= -1
		return newPos
	
	def mirrorPath( self, path, axis=0 ):
		return [self.mirror(pos,axis) for pos in path]
	
	def addMirrors( self ):
		for i in range(len(self.paths)):
			pathList = self.paths[i+1]
			
			newPathList = []
			for path in pathList:
				mPath = self.mirrorPath( path )
				
				if mPath == path: newPathList.append( path )
				else: newPathList.extend( [path, mPath] )
			
			self.paths[i+1] = newPathList
	
	def rotate( self, pos, angle ):
		return [ int(round(pos[X]*cos( angle ) - pos[Y]*sin( angle ))), int(round(pos[X]*sin( angle ) + pos[Y]*cos( angle ))) ]
		
	def rotatePath( self, path, angle=pi/2 ):
		return [ self.rotate( pos, angle ) for pos in path ]
		
	def getRotations( self, path ):
		return [ self.rotatePath( path, (pi/2)*i ) for i in range(4) ]
		
	def reversePath( self, path ):
		tempPath = path[:]
		tempPath.reverse()
		return [getRelativePos(tempPath[0],pos) for pos in tempPath]
'''
pc = PathContainer()
#mp = MapReader()

'''		
class Cell:
	def __init__( self, pos ):
		self.cid = hash( tuple( pos ))
		self.startId = None
		self.endId = None
		self.pos = pos
		self.value = 0
		self.cType = EMPTY
		
	def setValue( self, value ):
		self.value = value
		
	def setType( self, t ):
		self.cType = t
	
	def setPathIds( self, start, end ):
		self.startId = start
		self.endId = end
	
	def addInRange( self, cells ):
		self.inRange.extend( cells )
	
	def getValue( self ):
		return self.value
		
	def getType( self ):
		return self.cType
	
	def getPosition( self ):
		return self.pos

	def getInfo( self ):
		return [self.pos[X], self.pos[Y], self.value, self.cType, self.startId, self.endId]
	
	def setInfo( self, cid, pos, value, type, sid=None, eid=None ):
		self.cid = cid
		self.startId = sid
		self.endId = eid
		self.pos = pos
		self.value = value
		self.cType = type
	
	def getNeighbors( self ):
		neighbors = []
		for i in range(-1,2):
			for j in range(-1,2):
				nPos = [self.pos[X] + i, self.pos[Y] + j]
				if nPos != self.pos and abs(i) != abs(j):
					neighbors.append( nPos )
		
		return neighbors

	def reset( self ):
		self.value = 0
		self.cType = EMPTY
'''

class Grid:
	"""Cell container:
		__init__( x, y )		-> Initializes Grid of x by y empty Cells
		void reset()			-> Clear current Cell values of Grid
		void printGrid()		-> Print current Grid configuration
		void getInfo()			-> Print current Grid's Cell information
		void setCells( cellInfo )	-> Set specified Cells to provided values
			cellInfo format: [[x,y,value,type],...]
		
		int numEndCells()		-> Returns the number of 'endpoint' Cells in the Grid
		int numConnected()		-> Returns the number of connected 'endpoint' Cells
		int getConnectedness()	-> Returns the percentage of 'endpoint' Cells that are connected
		
		Cell getCellAt( pos )		-> Returns the Cell at given grid coordinates
		void connect( pos1, pos2, path )	-> Connects the given position with a given path
		bool isReachable( origin, target )	-> Determines whether a target position is within the range of the cell at the origin position
		bool checkValid()			->returns false if board configuration violates any basic principles of complete-ability
		void showRange( pos )		-> Print the range of the Cell at the given position
		
		Cell[] getCellType( cellType )		-> Returns a list of all cells of type 'cellType'
		Cell[] getReachable( pos )	-> Returns a list of all cells that are reachable from the Cell at the given position, that also share the same value
	"""
		
	def __init__( self, xsize=10, ysize=10, cellInfo=None ):
		self.dimensions = [xsize,ysize]
		self.grid = []
		self.cellList = []
		self.readers = { "csv": CsvCellReader( self.dimensions ), "json": JsonCellReader( self.dimensions ) }
		self.pathList = pc 
		
		for j in range(ysize):
			cells = []
			for i in range(xsize):
				cell = Cell( [i,j] )
				cells.append(cell)
				self.cellList.append(cell)
			self.grid.append( cells )
	
		if cellInfo: self.setCellInfo( cellInfo )
	
	def importGrid( self, name, fileType ):
		data = self.readers[fileType].readGrid( name )
		self.setCellInfo( data )
		
	def exportGrid( self, name, fileType ):
		self.readers[fileType].writeGrid( name, self.cellList )
	
	'''	
	def exportAsJson( self ):
		data = []
		for cell in self.cellList:
			v = cell.getValue()
			col = 0 if v else 255
			cellInfo = {"number": v, "color": {"r": col, "g": col, "b": col}}
			data.append( cellInfo )
			
		with open( 'solverOutput.txt', 'w' ) as outfile:
			json.dump( data, outfile )
		
	def getGrid( self, name ):
		self.mapReader.loadTemplate( name )
		self.setCellInfo( self.mapReader.getCellInfo() )
	'''
	def reset( self ):
		for row in self.grid:
			for cell in row:
				cell.reset()

	def setCellInfo( self, cellInfo ): # cellInfo: [[xpos,ypos,value,type,startId,endId],...]
		for info in filter( lambda x: x[TYPE] == END, cellInfo ):
			#print info
			cell = self.grid[ info[Y] ][ info[X] ]
			cell.setValue( info[VALUE] )
			cell.setType( info[TYPE] )
			cell.setPathIds( info[START_ID], info[END_ID] )
			
	def getCellInfo( self ):
		return [cell.getInfo() for cell in self.cellList]	
			
	def printGrid( self, rnge=False ):
		for j in range(len(self.grid)):
			for i in range(len(self.grid[j])):
				cell = self.grid[j][i]
				if cell.getType() == END: print cell.getValue(),
				elif cell.getType() == PATH: print cell.getValue(),#'*',
				elif rnge and self.isReachable( rnge, [i,j] ): print 'X',
				else: print ' ',
			print ''
		print ''
	
	def getInfo( self ):
		for j in range(len(self.grid)):
			for i in range(len(self.grid[j])):
				cell = self.grid[j][i]
				if cell.getType() != EMPTY:
					print "[%(x)d, %(y)d]:\tValue -> %(v)d, Type -> %(t)d" % {'x': i, 'y': j, 'v': cell.getValue(), 't': cell.getType()}
	
	def getCellAt( self, pos ):
		return self.grid[pos[Y]][pos[X]]
	
	def outOfBounds( self, pos ):
		if not 0 <= pos[X] < self.dimensions[X]: return True
		if not 0 <= pos[Y] < self.dimensions[Y]: return True
		return False
	
	def isReachable( self, p1, p2 ):
		"""bool isReachable( int[] p1, int[] p2 )
			returns True if p1 reachable from p2 and visa versa
		"""

		res = abs( p1[0]-p2[0] ) + abs( p1[Y] - p2[Y] )
		v = self.getCellAt( p1 ).getValue()

		return res < v and res%2 != v%2
	
	def checkValid( self ):
		"""bool checkValid()
			returns false if board configuration violates any basic principles of complete-ability
		"""
		
		endCells = self.getCellType( END )
		
		# Even number of endpoints?
		if len( endCells ) % 2 != 0: return False
		
		# All endpoints have other reachable endpoints of equal value?
		for cell in endCells:
			if len( getReachable( cell.pos )) == 0: return False
		
		return True
	
	def showRange( self, pos ):
		"""void showRange( int[] pos )
			prints the range of the Cell at the given position
		"""
		
		self.printGrid( pos )
		
	def getReachable( self, pos ):
		"""Cell[] getReachable( int[] pos )
			Returns a list of all cells that are reachable from the Cell at the given position, that also share the same value
		"""
		
		cell = self.getCellAt( pos )
		valid = [c for c in self.getCellType( END ) if c.getValue() == cell.getValue() and c.cid != cell.cid and self.isReachable( pos, c.getPosition() )]
		return filter( lambda c : len(self.getConnections( pos, c.getPosition() )) > 0, valid )
		
	def getCellType( self, cType ):
		return [c for c in self.cellList if c.getType() == cType]
		
	def numConnected( self ):
		sids = [c.startId for c in self.getCellType( PATH )]
		eids = [c.endId for c in self.getCellType( PATH )]
		return len( set( sids + eids ))
		
	def numEndCells( self ):
		return len( self.getCellType( END )) + self.numConnected()
		
	def getConnectedness( self ):
		return self.numConnected()/float( numEndCells() )
		
	def getConnections( self, startPos, endPos ):
		startCell = self.getCellAt( startPos )
		endCell = self.getCellAt( endPos )
		
		if startCell.getValue() != endCell.getValue(): return []
		if startCell.getType() == PATH or endCell.getType() == PATH: return []
		if not self.isReachable( startPos, endPos ): return []
		
		value = startCell.getValue()
		paths = self.pathList.paths[value]
		valid = []
		for p in paths:
			plist = self.pathList.getRotations( p )
			for rp in plist:
				if rp[-1] == getRelativePos( startPos, endPos ) or rp[-1] == getRelativePos( endPos, startPos ):
					p = rp if rp[-1] == getRelativePos( startPos, endPos ) else self.pathList.reversePath( rp )
					isValid = True
					for pos in p:
						aPos = getAbsolutePos( startPos, pos )
						if self.outOfBounds( aPos ) or self.getCellAt( aPos ).getType() != EMPTY and  0 < p.index( pos ) < len(p)-1 :
							isValid = False
							break
						
					if isValid and p not in valid: valid.append( p )
						
		return valid
	
	def innerConnect( self, startPos, endPos, path ):
		startCell = self.getCellAt( startPos )
		endCell = self.getCellAt( endPos )
	
		for pos in path:
			cell = self.getCellAt( getAbsolutePos( startPos, pos ))
			cell.setType( PATH )
			cell.setValue( startCell.getValue() )
			cell.startId = startCell.cid
			cell.endId = endCell.cid
			
	def connect( self, startPos, endPos, path ):
		oldGrid = self.getCellInfo()
		self.innerConnect( startPos, endPos, path )
		newGrid = self.getCellInfo()
		self.setCellInfo( oldGrid )
		return Grid( self.dimensions[X], self.dimensions[Y], newGrid )
	
	'''
	def getReachIndex( self ):
		di = {}
		cells = self.getCellType( END )
		for cell in cells:
			k = len( self.getReachable( cell.getPosition() ))
			if di.has_key( k ): di[k].append( cell.getPosition() )
			else: di[k] = [ cell.getPosition() ]
			
		return di
	'''
	
	def getSimple( self ):
		# cells with only one possible connecting cell (minus reciprocals
		#return [c.getPosition() for c in filter( lambda cell: len( self.getReachable( cell.getPosition() )) == 1, self.cellList )]
		cells = filter( lambda cell: len( self.getReachable( cell.getPosition() )) == 1, self.cellList )
	
		uniqueCells = []#filter( lambda cell: self.getReachable( cell.getPosition() )[0] not in cells, cells )
		for c in cells: uniqueCells.append( c ) if self.getReachable( c.getPosition() )[0] not in uniqueCells else None
		
		# cells with only one possible connecting path
		validCells = filter( lambda cell: len( self.getConnections( cell.getPosition(), self.getReachable( cell.getPosition() )[0].getPosition() )) == 1, uniqueCells )
		
		return [c.getPosition() for c in validCells]
		
	def solveSimple( self ):
		simple = self.getSimple()
		
		while simple:
			for pos in simple:
				if self.getCellAt( pos ).getType() != END or not self.getReachable( pos ): continue
				target = self.getReachable( pos )[0].getPosition()
				conns = self.getConnections( pos, target )
				#print len(conns)
				self.innerConnect( pos, target, conns[0] )
			simple = self.getSimple()
	
	'''		
		reachIndex = self.getReachIndex()
		while reachIndex.has_key(1):
			for pos in reachIndex[1]:
				if self.getCellAt( pos ).getType != END: continue
				target = self.getReachable( pos )[0].getPosition()
				self.innerConnect( pos, target, self.getConnections( pos, target )[0] )
			reachIndex = self.getReachIndex()
	'''
'''
xsize = int( raw_input( "Enter grid width: " ))
ysize = int( raw_input( "Enter grid height: " ))
fname = raw_input( "Enter grid filename: " )
ftype = raw_input( "Enter grid filetype (csv/json): " )

g = Grid( xsize, ysize )
g.importGrid( fname, ftype )
g.solveSimple()
g.exportGrid( fname + "_sol", "json" )
print "Generated file saved as '" + fname + "_sol.json'"
'''
#sysargv = ["none","10","10","test.json"]
g = Grid( int(sys.argv[XSIZE]), int(sys.argv[YSIZE]) )
fname, ftype = sys.argv[FILENAME].split('.')
#g = Grid( xsize, ysize )
g.importGrid( fname, ftype )
g.solveSimple()
g.exportGrid( "temp", "json" )

#testInfo = [[2,2,5,END],[3,5,5,END],[7,3,4,END],[7,6,4,END],[5,5,2,END],[5,6,2,END],[4,8,2,END],[5,8,2,END]]

#print "Use '__doc__' or 'filename.__doc__' command for usage information"
#g = Grid()
#g.importGrid( "test", "csv" )
#g.solveSimple()

#g.printGrid()
#g.getInfo()
#g.showRange( [4,8] )
#raw_input("Press Enter to Quit..")
