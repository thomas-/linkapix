"""
	cellReader.py
	~~~~~~~~~

	This module describes the data structure used to represent each
	link-a-pix puzzle cell, and then implements classes which read
	and write cell arrangements to and from either csv or json files.

	:Mandla Moyo, 2014.
"""

from fileReader import CsvReader, JsonReader
from constants import *

# Map for writing cell colour's to json file
COLOUR_MAP = { WHITE: [255,255,255], 
			   BLACK: [0,0,0],
			   RED: [255,0,0],
			   GREEN: [0,255,0],
			   BLUE: [0,0,255],
			   YELLOW: [255,255,0] }

# Map for reading cell colour info from csv file
CSV_COLS = { 1:BLACK, 2:RED, 3:GREEN, 4:BLUE, 5:YELLOW, 6:BLACK, 7:BLACK, 8:BLACK, 9:BLACK }
			   
class Cell:
	"""The Cell class describes the core link-a-pix data-type: a grid cell.
	It specifies a position, colour, value, and various identifying attributes
	that allow cells of different type (empty, path, endpoint), or connection
	group to be distinguished form each other.
	"""
	def __init__( self, pos ):
		self.cid = hash( tuple( pos ))
		self.startId = None
		self.endId = None
		self.colour = WHITE
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
	
	def setColour( self, colour ):
		self.colour = colour
	
	def addInRange( self, cells ):
		self.inRange.extend( cells )
	
	def getId( self ):
		return self.cid
		
	def getValue( self ):
		return self.value
		
	def getType( self ):
		return self.cType
	
	def getPosition( self ):
		return self.pos

	def getInfo( self ):
		return [self.pos[X], self.pos[Y], self.value, self.cType, self.startId, self.endId, self.colour]
	
	def setInfo( self, cid, value, type, pos=None, sid=None, eid=None, colour=WHITE ):
		self.cid = cid
		self.value = value
		self.cType = type
		self.pos = pos or self.pos
		self.startId = sid or self.startId
		self.endId = eid or self.endId
		self.colour = colour
		
	def getNeighbors( self ):
		"""Returns the eight (or less if on boundary) neighbouring cells
		of any specified cell.
		"""
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

class CellReader():
	"""The CellReader class is an abstract class that describes the interface
	of the json and csv I/O cell reading classes, using the fileReaders specified
	in 'fileReader.py'
	"""
	def __init__( self, dimensions, reader ):
		self.dimensions = dimensions
		self.reader = reader
		
	def getCellInfo( self, data ):
		return None
		
	def readGrid( self, name ):
		data = self.reader.readFile( name )
		return self.getCellInfo( data )	
		
	def writeGrid( self, name, data ):
		pass
	

class CsvCellReader( CellReader ):
	def __init__( self, dimensions, directory=PUZZLE_DIRECTORY ):
		CellReader.__init__( self, dimensions, CsvReader( directory ))
		
	def getCellInfo( self, data ):
		"""Takes a csv data array, and converts the data into a format that
		can be parsed by the Grid container for later use.
			in	<- [[1,1,0,..,1,1],..]
			out -> [[xpos, ypos, value, type, startId, endId, colourCode],..]
		"""
		cellInfo = []
		
		for j in range(len( data )):
			for i in range( len( data[j] )):
				if data[j][i]:
					cellInfo.append( [i, j, data[j][i], 1, None, None, CSV_COLS[data[j][i]]] )
					
		return cellInfo
		
	def writeGrid( self, name, cellList, full=False ):
		"""Writes to (or overwrites) a specified csv file with data corresponding
		to a given list of cell data objects.
		"""
		data = []
		row = []

		for i in range(len(cellList)):
			cell = cellList[i]
			v = cell.getValue()
				
			if i%self.dimensions[X] == self.dimensions[X]-1:
				row.append( v )
				data.append(row)
				row = []
			else:
				row.append( v )
				
		self.reader.writeFile( name, data )
		
		
class JsonCellReader( CellReader ):
	def __init__( self, dimensions, directory=PUZZLE_DIRECTORY ):
		CellReader.__init__( self, dimensions, JsonReader( directory ))
		
	def getCellInfo( self, data ):
		"""Takes a json data list of dictionaries, and converts the data
		into a format that can be parsed by the Grid container for later use.
			in	<- [[{"number": v, "color": {"r": r, "g": g, "b": b}},..]..]
			out -> [[xpos, ypos, value, type, startId, endId, colourCode],..]
		"""
		cellInfo = []
		for row in range( len( data )):
			for col in range( len( data[row] )):
				xPos = col #i%self.dimensions[X]
				yPos = row #i/self.dimensions[Y]
				value = data[row][col]["number"]
				type = data[row][col]["type"] if "type" in data[row][col] else END
				startId = None
				endId = None
				
				c = data[row][col]["color"]
				colour = hash( (c["r"], c["g"], c["b"]) )
				
				if value: cellInfo.append( [xPos, yPos, value, type, startId, endId, colour] )
		return cellInfo
		
	def writeGrid( self, name, cellList, full=False ):
		"""Writes to (or overwrites) a specified csv file with data corresponding
		to a given list of cell data objects.
			json output format: { "number": _, "color": {"r": _, "g": _, "b": _ }}
		"""
		data = []
		row = []

		for i in range(len(cellList)):
			cell = cellList[i]
			v = cell.getValue()
			#col = 0 if v else 255
			r, g, b = COLOUR_MAP[cell.colour]
			cellInfo = {"number": v, "color": {"r": r, "g": g, "b": b}}
			
			if full:
				cellInfo["type"] = cell.getType()
				cellInfo["id"] = cell.getId()

			if i%self.dimensions[X] == self.dimensions[X]-1:
				row.append( cellInfo )
				data.append(row)
				row = []
			else:
				row.append( cellInfo )
				
		self.reader.writeFile( name, data )
	
""" UNUSED
class Converter:
	def __init__( self, dimensions ):
		self.dimensions = dimensions
		self.csvReader = CsvCellReader( dimensions )
		self.jsonReader = JsonCellReader( dimensions )
		
	def reset( dimensions ):
		self.dimensions = dimensions
		self.csvReader = CsvCellReader( dimensions )
		self.jsonReader = JsonCellReader( dimensions )
		
	def getCellList( self, cellInfo ):
		cellDi = {}
		for j in range( self.dimensions[Y] ):
			for i in range( self.dimensions[X] ):
				cellDi[(i,j)] = Cell( [i,j] )
				cellDi[(i,j)].setInfo( 0, 0, EMPTY )
				
		for info in cellInfo:
			cellDi[(info[X],info[Y])].setInfo( 0, info[VALUE], info[TYPE] )

		return cellDi.values()
		
	def jsonToCsv( self, fname ):
		cellList = self.getCellList( self.jsonReader.readGrid( fname ))
		self.csvReader.writeGrid( fname, cellList )
	
	def csvToJson( self, fname ):
		cellList = self.getCellList( self.csvReader.readGrid( fname ))
		self.jsonReader.writeGrid( fname, cellList )
"""
