from cellReader import Cell, CsvCellReader, JsonCellReader
from pathContainer import PathContainer, getRelativePos, getAbsolutePos
from math import pi, cos, sin
from random import randint, choice
from constants import *
from copy import deepcopy
import sys

PID = 4
LIMIT = 8

class Grid( object ):
	def __init__( self, x, y, rand=False ):
		self.x = x
		self.y = y
		self.dimensions = [x,y]
		
		self.pathList = PathContainer()
		self.grid = []
		self.symbols = {(0,0):0,(1,1):1,(1,2):"*"}
		self.initValue = [0,0,0,EMPTY,0]
		self.unknown = ' '
		self.pids = 1
		
		self.readers = { "csv": CsvCellReader( self.dimensions ), "json": JsonCellReader( self.dimensions ) }
		self.reset( rand )
		
	def build( self, x, y ):
		return [[ self.initValue for c in range( x )] for r in range( y )]
		
	def randomBuild( self, x, y ):
		return [[ randint( 0, len( self.symbols )-1 ) for c in range( x )] for r in range( y )]
		
	def reset( self, rand=False ):
		if rand: self.grid = self.randomBuild( self.x, self.y )
		else: self.grid = self.build( self.x, self.y )
	
	def getCellList( self ):
		cells = []
		for j in range(len(self.grid)):
			for i in range(len(self.grid[j])):
				c = self.grid[j][i]
				cells.append( Cell( [c[X],c[Y]] ))
				cells[-1].setInfo( c[PID], c[VALUE], c[TYPE] )
				if c[TYPE] != END: cells[-1].setInfo( c[PID], 0, EMPTY )
		return cells
	
	def exportGrid( self, name, fileType ):
		self.readers[fileType].writeGrid( name, self.getCellList(), True )
	
	def importGrid( self, name, fileType ):
		data = self.readers[fileType].readGrid( name )
		self.setCellInfo( data )
	
	def setCellInfo( self, cellInfo ): # cellInfo: [[xpos,ypos,value,type,startId,endId],...]
		for info in cellInfo:
			self.grid[info[Y]][info[X]] = [info[X],info[Y],info[VALUE],info[TYPE],self.pids]
			self.pids += 1
			#print info
		#print ""
			
	def printGrid( self, showAll=False ):
		for r in range( len( self.grid )):
			for c in range( len( self.grid[r] )):
				if not showAll and self.grid[r][c][TYPE] != END: print ' ',
				else:
					try: print self.symbols[tuple(self.grid[r][c][2:4])],
					except: print self.grid[r][c][VALUE],
			print ''
		print ''
	
	def getNeighbors( self, pos ):
		neighbors = []
		
		for y in range(-1,2):
			for x in range(-1,2):
				p = [pos[X] + x, pos[Y] + y]
				if( self.isValid( p )) and abs(x) != abs(y):
					neighbors.append( self.grid[p[Y]][p[X]] )
		
		return neighbors
		
	def isValid( self, pos ):
		maxBounds = [self.x,self.y]
		for i in range(len(pos)):
			if( pos[i] < 0 or pos[i] >= maxBounds[i] ): return False
			
		return True

	def getEndNodes( self, value=-1 ):
		nodes = []
		for y in range(len(self.grid)):
			for x in range(len(self.grid[y])):
				n = self.grid[y][x]
				if n[TYPE] == END and (value == -1 or n[VALUE] == value):
					nodes.append( n )
					
		return nodes
		
	def getRandomPair( self, value=-1, limit=9999 ):
		nodes = filter( lambda x: x[VALUE] < limit, self.getEndNodes( value ))
		if len( nodes ) < 2: return 1
		
		first = choice(nodes)
		neighbors = filter( lambda x: 0 < x[VALUE] + first[VALUE] < limit and x[TYPE] == END, self.getNeighbors(first[:2]))
		if len( neighbors ) == 0: return -1
		
		second = choice(neighbors)
		
		'''
		self.grid[first[Y]][first[X]][TYPE] = 2
		self.grid[second[Y]][second[X]][TYPE] = 2
		g.printGrid()
		self.grid[first[Y]][first[X]][TYPE] = 1
		self.grid[second[Y]][second[X]][TYPE] = 1
		'''

		return [first,second]
		
	def getConnectedNeighbors( self, pos, pid ):
		return filter( lambda x: x[PID] == pid, self.getNeighbors( pos ))
		
	
	def getConnected( self, node, value, oldId, newId ):
		neighbors = sorted( self.getNeighbors(node[:2]), key=lambda x: (-x[TYPE], len(self.getConnectedNeighbors(x[:2],oldId)))) #start with PATH nodes, then move onto END nodes, to ensure correct traversal order (nodes with fewest neighbors go first)
		#print node, value, oldId, newId, neighbors
		
		node[VALUE],node[PID] = value, newId
		for neighbor in neighbors:
			if neighbor[PID] == oldId: # a connected neighbor exists, current node is a path node
				node[TYPE] = PATH
				return self.getConnected( neighbor, value, oldId, newId )
		
		return node

	def merge( self, value=-1, limit=LIMIT, showStep=False ):
		pair = self.getRandomPair( value, limit )
		attempts = 5
		while type(pair) is int or pair[0][PID] == pair[1][PID]:
			if (type(pair) is int and pair > 0) or attempts == 0: return False
			pair = self.getRandomPair( value, limit )
			attempts -= 1
			
		newValue = pair[0][VALUE] + pair[1][VALUE]
		newId = self.pids
		self.pids += 1
		
		ends = []
		temp = deepcopy( self.grid )
		
		for n in pair:
			oldId = n[PID]
			ends.append( self.getConnected( n, newValue, oldId, newId ))
		
		for path in self.getConnections( ends[0], ends[1] ):
			for p in path:
				if self.grid[ends[0][Y]+p[Y]][ends[0][X]+p[X]][TYPE] == EMPTY:
					self.grid = temp
					return [ends,-1]
				
		#if showStep: self.printGrid()
		return ends
		
	def runMerges( self, n, showAll=False ):
		#if not showAll: self.printGrid()
		temp = deepcopy( self.grid ) # FOR DEBUGGING ONLY!
		
		endList = []
		for i in range(n): endList.append( self.merge( showStep=showAll ))
		
		#if not showAll: self.printGrid()
		
		'''
		# FOR DEBUGGING #
		for i in endList: 
			if i: 
				if i[1] == -1:
					print "INVALID CONNECTION!"
					i = i[0]
					
				print "Ends: ", i
				print "Paths: (L", i[0][VALUE], ")"
				for c in self.getConnections( i[0], i[1] ):
					print "\t", c, " - ",
					for p in c:
						print (["EMPTY","END","PATH"][self.grid[i[0][Y]+p[Y]][i[0][X]+p[X]][TYPE]],self.grid[i[0][Y]+p[Y]][i[0][X]+p[X]][VALUE]),
					print ""
					
				if i[0][TYPE] != 1 or i[1][TYPE] != 1: 
					current = deepcopy( self.grid )
					self.printGrids( temp, current )
					self.grid = temp
					#return False
			else: print ".",
		print ""
		# FOR DEBUGGING #
		'''
		return True
		
	def isReachable( self, p1, p2 ):
		"""bool isReachable( int[] p1, int[] p2 )
			returns True if p1 reachable from p2 and visa versa
		"""

		res = abs( p1[X]-p2[X] ) + abs( p1[Y] - p2[Y] )
		v = p1[VALUE]

		return res < v and res%2 != v%2
		
	def printGrids( self, first, second ):
		self.grid = first
		self.printGrid()
		self.printGrid(True)
		self.grid = second
		self.printGrid()
		self.printGrid(True)
		
	def multiMerge( self, n ):
		for i in range(n):
			#print "Run ", i
			if not self.runMerges(1): break
		#self.printGrid()
		
	#TO ADAPT FOR VALIDITY TESTING
	def getConnections( self, startCell, endCell ):
		# Error checking (should be unnecessary, only keep for testing..)
		if startCell[VALUE] != endCell[VALUE]: return []
		if startCell[TYPE] == PATH or endCell[TYPE] == PATH: return []
		if not self.isReachable( startCell, endCell ): return [] #isReachable()
		
		startPos = [startCell[X],startCell[Y]]
		endPos = [endCell[X],endCell[Y]]
		value = startCell[VALUE]
		paths = self.pathList.paths[value]
		valid = []
		
		for p in paths:
			plist = self.pathList.getRotations( p )
			
			# check whether to rotate p for proper orientation (start at start cell)..
			for rp in plist:
				if rp[-1] == getRelativePos( startPos, endPos ) or rp[-1] == getRelativePos( endPos, startPos ):
					p = rp if rp[-1] == getRelativePos( startPos, endPos ) else self.pathList.reversePath( rp )
					
					isValid = True
					for pos in p:
						#print "pos: ", pos, " - StartPos: ", startPos
						apos = getAbsolutePos( startPos, pos )
						if not (0 <= apos[X] < self.x and 0 <= apos[Y] < self.y):
							isValid = False
							break
							
						cell = self.grid[apos[Y]][apos[X]]
						
						# if a cell in the specified path is not either empty, or a part of the defined path, it is invalid
						if cell[TYPE] != EMPTY and cell[PID] != startCell[PID] and 0 < p.index( pos ) < len(p)-1 :
							isValid = False
							break
						
					if isValid and p not in valid: valid.append( p )
						
		return valid
	
def reset():
	g = Grid(10,10)
	g.importGrid("gentest","csv")
	return g
''' 
xsize = int( raw_input( "Enter grid width: " ))
ysize = int( raw_input( "Enter grid height: " ))
fname = raw_input( "Enter grid filename: " )
ftype = raw_input( "Enter grid filetype (csv/json): " )
'''

g = Grid( int(sys.argv[XSIZE]), int(sys.argv[YSIZE]) )
fname, ftype = sys.argv[FILENAME].split('.')
#g = Grid( xsize, ysize )
g.importGrid( fname, ftype )
g.multiMerge(100)
g.exportGrid( "temp", "json" )
#g.exportGrid( fname + "_gen", "json" )
#print "Generated file saved as '" + fname + "_gen.json'"

#g = Grid(10,10)
#g.importGrid("gentest","csv")
#print g.getRandomPair()
#g.printGrid()
#raw_input("Press Enter to Quit..")
#print "Use g.multiMerge(n) to generate puzzle.."
