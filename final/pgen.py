"""
	generate.py (RENAME)
	~~~~~~~~~

	Solver for G52GRP Link-A-Pix Project
	
	This module implements the puzzle generation functionality for a given image bitmap.
	The program takes 3 arguments on the command line, and outputs a valid puzzle to a
	temp file (of name and type specified in constants.py) in the specified puzzle directory.
	
	Command line interface:
		$ python generate.py [PUZZLE_WIDTH] [PUZZLE_HEIGHT] [PUZZLE_NAME] [PUZZLE_DIFFICULTY (4-10)]
		(PUZZLE_NAME is a type-specified name of a file located in the directory specified in constants.py)
		
	:Mandla Moyo, 2014.
"""


from math import pi, cos, sin
from random import randint, choice
from pattern import getRelativePos, getAbsolutePos, getRotations, getRelativePath, getEuclidianDistance, addMirrors
from constants import *
from grid import Grid
from cellReader import Cell
from copy import deepcopy
import sys

# Remove redundancy..



class GenerateGrid( Grid ):
	def __init__( self, x, y, limit ):
		Grid.__init__( self, x, y, limit )
		#self.symbols = {(0,0):' '}
		self.pids = 1
		self.runs = 0
		self.build()
		
	def build( self ):
		self.grid = [[ INIT_VALUE for c in range( self.dimensions[X] )] for r in range( self.dimensions[Y] )]
	
	def getAllCells( self ):
		cells = []
		for j in range(len(self.grid)):
			for i in range(len(self.grid[j])):
				c = self.grid[j][i]
				cells.append(c)
				
		return cells
		
	def getCellList( self ):
		cells = []
		for j in range(len(self.grid)):
			for i in range(len(self.grid[j])):
				c = self.grid[j][i]
				cells.append( Cell( [c[X],c[Y]] ))
				cells[-1].setInfo( c[PID], c[VALUE], c[TYPE], colour = c[COLOUR] )
				if c[TYPE] != END: cells[-1].setInfo( c[PID], 0, EMPTY )
		return cells
	
	def setCellInfo( self, cellInfo ):
		for info in cellInfo:
			self.grid[info[Y]][info[X]] = [info[X],info[Y],info[VALUE],info[TYPE],self.pids, self.pids, info[COLOUR]]
			self.pids += 1


	def getNeighbors( self, pos ):
		neighbors = []
		
		for y in range(-1,2):
			for x in range(-1,2):
				p = [pos[X] + x, pos[Y] + y]
				if( self.isValidPos( p )) and abs(x) != abs(y):
					neighbors.append( self.grid[p[Y]][p[X]] )
		
		return neighbors
	
	def getEndNodes( self, value=-1 ):
		nodes = []
		for y in range(len(self.grid)):
			for x in range(len(self.grid[y])):
				n = self.grid[y][x]
				if n[TYPE] == END and (value == -1 or n[VALUE] == value):
					nodes.append( n )
					
		return nodes
		
	def getRandomPair( self, value=-1 ):
		nodes = filter( lambda x: x[VALUE] < self.limit, self.getEndNodes( value ))
		if len( nodes ) < 2: return 1
		
		first = choice(nodes)
		neighbors = filter( lambda x: 0 < x[VALUE] + first[VALUE] <= self.limit and x[TYPE] == END and x[COLOUR] == first[COLOUR], self.getNeighbors(first[:2]))
		if len( neighbors ) == 0: return -1
		
		second = choice(neighbors)

		return [first,second]
		
	def getConnectedNeighbors( self, pos, pid ):
		return filter( lambda x: x[PID] == pid, self.getNeighbors( pos ))
		
	
	def getConnected( self, node, value, oldId, newId ):
		# Start with PATH nodes, then move onto END nodes, to ensure correct traversal order (nodes with fewest neighbours go first)
		neighbors = sorted( self.getNeighbors(node[:2]), key=lambda x: (-x[TYPE], len(self.getConnectedNeighbors(x[:2],oldId))))
		
		node[VALUE],node[PID] = value, newId
		for neighbor in neighbors:
			# A connected neighbour exists, current node is a path node
			if neighbor[PID] == oldId: 
				node[TYPE] = PATH
				return self.getConnected( neighbor, value, oldId, newId )
		
		return node

	def merge( self, value=-1, showStep=False ):
		pair = self.getRandomPair( value )
		attempts = 5
		while type(pair) is int or pair[0][PID] == pair[1][PID]:
			if (type(pair) is int and pair > 0) or attempts == 0: return False
			pair = self.getRandomPair( value )
			attempts -= 1
			
		newValue = pair[0][VALUE] + pair[1][VALUE] # new value
		newId = self.pids
		self.pids += 1
		
		# perform error check with new value
		
		ends = []
		temp = deepcopy( self.grid )
		fail = False
		
		for n in pair:
			oldId = n[PID]
			ends.append( self.getConnected( n, newValue, oldId, newId ))
		
		allPaths = self.getConnections( ends[0], ends[1] )
		if self.getReachable( ends[0] ) and self.getReachable( ends[1] ): fail = True
		
		if not fail:
			for path in allPaths:
				for p in path:
					if self.grid[ends[0][Y]+p[Y]][ends[0][X]+p[X]][TYPE] == EMPTY:
						fail = True

		
		#check if ends can both connect to more than one other node.
		#if so, undo
		#for e in ends:
		if fail:
			#print "generation error\n\n"
			#self.printGrid()
			self.grid = temp
			#self.printGrid()
			self.runs += randint(0,1)
			return [ends,-1]
				
		return ends
		
	def runMerges( self, n, showAll=False ):
		#temp = deepcopy( self.grid ) FOR DEBUGGING ONLY!
		
		endList = []
		for i in range(n): endList.append( self.merge( showStep=showAll ))
		#if not showAll: self.printGrid()
		return True
		
	def getRuns( self, x, y, lim ):
		return int( (x*y)/((LIMIT_CONSTANT/lim)*10) )
		
	def isReachable( self, p1, p2 ):
		"""bool isReachable( int[] p1, int[] p2 )
			returns True if p1 reachable from p2 and visa versa
		"""

		res = abs( p1[X]-p2[X] ) + abs( p1[Y] - p2[Y] )
		v = p1[VALUE]

		return res < v and res%2 != v%2
		
	def getReachable( self, cell ):
		cells = self.getAllCells()
		valid = [c for c in cells if c[TYPE] == END and c[VALUE] == cell[VALUE] and c[PID] != cell[PID] and c[COLOUR] == cell[COLOUR] and self.isReachable( cell, c )]
		return filter( lambda c : len(self.getConnections( cell, c )) > 0, valid )
		
	def printGrid( self, showAll=False ):
		for r in range( len( self.grid )):
			for c in range( len( self.grid[r] )):
				if not showAll and self.grid[r][c][TYPE] != END: print ' ',
				else:
					try: print self.symbols[tuple(self.grid[r][c][2:4])],
					except: print self.grid[r][c][VALUE],
			print ''
		print '\n\n'
		
	def printGrids( self, first, second ):
		self.grid = first
		self.printGrid()
		self.printGrid(True)
		self.grid = second
		self.printGrid()
		self.printGrid(True)
		
	def multiMerge( self, xsize, ysize, limit ):
		self.runs = self.getRuns( xsize, ysize, limit )
		inc = self.runs/10
		if self.runs > 100: inc = self.runs/100
		cur = 0
		print self.runs, xsize*ysize
		#for i in range( runs ):
		while self.runs > 0:
			self.runs -= 1
			cur += 1
			if cur > inc: 
				print ".",
				sys.stdout.flush()
				cur = 0
				
			if not self.runMerges( 1 ): break
		
	#TO ADAPT FOR VALIDITY TESTING
	def getConnections( self, startCell, endCell ):
		# Error checking (should be unnecessary, only keep for testing..)
		if startCell[VALUE] != endCell[VALUE]: return []
		if startCell[TYPE] == PATH or endCell[TYPE] == PATH: return []
		if not self.isReachable( startCell, endCell ): return []
		
		startPos = [startCell[X],startCell[Y]]
		endPos = [endCell[X],endCell[Y]]
		value = startCell[VALUE]
		distance = getEuclidianDistance( startPos, endPos )
		paths = addMirrors( self.pathList.paths[value][distance] )
		valid = []
		
		for p in paths:
			plist = getRotations( p )
			
			# check whether to rotate p for proper orientation (start at start cell)..
			for rp in plist:
				if rp[-1] == getRelativePos( startPos, endPos ) or rp[-1] == getRelativePos( endPos, startPos ):
					p = rp if rp[-1] == getRelativePos( startPos, endPos ) else getRelativePath( rp )
					
					isValid = True
					for pos in p:
						apos = getAbsolutePos( startPos, pos )
						if not (0 <= apos[X] < self.dimensions[X] and 0 <= apos[Y] < self.dimensions[Y]):
							isValid = False
							break
							
						cell = self.grid[apos[Y]][apos[X]]
						
						# if a cell in the specified path is not either empty, or a part of the defined path, it is invalid
						if cell[TYPE] != EMPTY and cell[PID] != startCell[PID] and 0 < p.index( pos ) < len(p)-1 :
							isValid = False
							break
						
					if isValid and p not in valid: valid.append( p )
						
		return valid
		

xsize, ysize, filename, limit = int(sys.argv[XSIZE]), int(sys.argv[YSIZE]), sys.argv[FILENAME], int(sys.argv[LIMIT])

g = GenerateGrid( xsize, ysize, limit ) # python pgen.py x y name limit
fname, ftype = filename.split('.')
g.importGrid( fname, ftype )
g.multiMerge( xsize, ysize, limit )
g.exportGrid( fname, ftype )
