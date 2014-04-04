"""
	grid.py
	~~~~~~~~~

	This module describes the core interface for a basic Grid object.
	
	The grid is the main data structure used to manipulate cells in order both to generate and solve Link-a-Pix puzzles. The parent Grid class implements various utility, cell handling, and file handling operations, allowing generating and solving functionality to be separated into particular child classes.
	
	:Mandla Moyo, 2014.
"""

from pattern import getRotations, getRelativePos, getAbsolutePos, getRelativePath, getEuclidianDistance, addMirrors
from cellReader import Cell, CsvCellReader, JsonCellReader
from pathContainer import PathContainer 
from constants import *

class Grid( object ): # object? only for pgen at the mo..
	""" The Grid class is used to contain and manipulate puzzle data as
	specified by particular Cell configurations.
	"""
	def __init__( self, x, y, limit=MAX_LIMIT ):
		#self.pids = 1
		self.grid = []
		self.cellList = []
		self.dimensions = [x,y]
		self.pathList = PathContainer( limit )
		self.readers = { CSV: CsvCellReader( self.dimensions ), JSON: JsonCellReader( self.dimensions ) }
		self.limit = limit
		#self.build()
	
	""" INITIALIZATION
	"""
	def build( self ):
		for j in range( self.dimensions[Y] ):
			cells = []
			for i in range( self.dimensions[X] ):
				cell = Cell( [i,j] )
				cells.append(cell)
				self.cellList.append(cell)
			self.grid.append( cells )
			
	

		
	""" UTILITY FUNCTIONS
	"""
	def isValidPos( self, pos ):
		for i in range(len(pos)):
			if( pos[i] < 0 or pos[i] >= self.dimensions[i] ): return False
			
		return True
	
	def isReachable( self, p1, p2 ):
		"""Returns True if p1 reachable from p2 and visa versa.
		"""
		res = abs( p1[0]-p2[0] ) + abs( p1[Y] - p2[Y] )
		v = self.getCellAt( p1 ).getValue()

		return res < v and res%2 != v%2
		
		
	""" CELL HANDLING FUNCTIONS
	"""
	def getCellAt( self, pos ):
		return self.grid[pos[Y]][pos[X]]
	
	def getCellList( self ):
		return self.cellList
		
	def setCellInfo( self, cellInfo ):
		pass
		
	def getCellInfo( self ):
		return [cell.getInfo() for cell in self.getCellList()]
	
	def getCellType( self, cellType, value=-1 ):
		"""Returns all the cells of a particular type.
			Cell Types:
				END		- The cell is an endpoint, and is visible in the initial puzzle state.
				PATH	- The cell contains a value, but is a part of a path connecting two endpoints.
				EMPTY	- The cell contains no data, and represents a blank space in the puzzle.
		"""
				
		return [c for c in self.cellList if c.getType() == cellType and (value == -1 or c.getValue() == value)]
	
	def getReachable( self, pos ):
		"""Returns a list of all cells that are reachable from the Cell at the given position, that also share the same value and colour.
		"""
		cell = self.getCellAt( pos )
		valid = [c for c in self.getCellType( END ) if c.getValue() == cell.getValue() and c.getId() != cell.getId() and c.getPosition() != cell.getPosition() and c.colour == cell.colour and self.isReachable( pos, c.getPosition() )]
		#print "==="
		#print cell.getId(), cell.getPosition()
		#for v in valid: print v.getId(), v.getPosition()
		#print '---'
		return filter( lambda c : len(self.getConnections( pos, c.getPosition() )) > 0, valid )
		
	def getConnections( self, startPos, endPos ): #, isGenerator=False ):
		"""Returns the set of valid connection patterns for a given pair of endpoints.
		"""
		# Get the cells at the specified positions.
		startCell = self.getCellAt( startPos )
		endCell = self.getCellAt( endPos )
		
		# There are no valid connections if the two cells are:
		#	1) Not of equal value,
		if startCell.getValue() != endCell.getValue(): return []
		
		#	2) Not both end cells,
		if startCell.getType() == PATH or endCell.getType() == PATH: return []
		
		#	3) Not reachable from one another.
		if not self.isReachable( startPos, endPos ): return []

		valid = []
		value = startCell.getValue()
		
		# Get the possible paths for the specified value.
		#print "Ids: ", startCell.getId(), endCell.getId()
		distance = getEuclidianDistance( startCell.getPosition(), endCell.getPosition() )
		#print "Value: ", value, " -- Distance: ", distance
		paths = addMirrors( self.pathList.paths[value][distance] )
		
		# Test whether each path is a valid connector of the two points:
		#  For each of the possible paths,
		for p in paths:
		
			# All the possible rotations are expanded, and for each one,
			plist = getRotations( p )
			for rp in plist:
			
				# The alignment of the rotation is checked (it's endpoints correspond to the positions of the specified points).
				if rp[-1] == getRelativePos( startPos, endPos ) or rp[-1] == getRelativePos( endPos, startPos ):
				
					# If the starting position of the rotation is not the specified start position, the rotation is reversed.
					p = rp if rp[-1] == getRelativePos( startPos, endPos ) else getRelativePath( rp )
					isValid = True
					
					# Each of the positions in the path being tested is checked for any properties that render it invalid:
					for pos in p:
						aPos = getAbsolutePos( startPos, pos )
						
						# The position must be in bounds, and either empty (not a path point or end point in another path), or
						#  one of the initially specified end points.
						if not self.isValidPos( aPos ) or (self.getCellAt( aPos ).getType() != EMPTY and self.getCellAt( aPos ).getId() != startCell.getId() and 0 < p.index( pos ) < len(p)-1):
							isValid = False
							break
						
					if isValid and p not in valid: valid.append( p )
						
		return valid
		
	""" FILE I/O HANDLING
	"""
	def importGrid( self, name, fileType ):
		"""Reads in cell data from the specified file, and uses it to update Grid cells
				Read data format: [[xpos, ypos, value, type, startId, endId, colourCode],..]
		"""
		data = self.readers[fileType].readGrid( name )
		self.setCellInfo( data )
		
	def exportGrid( self, name, fileType ):
		"""Takes the current set of stored cells, and passes them to the specified reader
		to be written to a given file.
		"""
		self.readers[fileType].writeGrid( name, self.getCellList() ) #,True)
	
	

####################################
# testSolve.py



####################################
# pgen.py

