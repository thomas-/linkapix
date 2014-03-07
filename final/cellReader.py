from fileReader import CsvReader, JsonReader
from constants import X, Y, EMPTY, END
#import sys

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
	
	def getId( self ):
		return self.cid
		
	def getValue( self ):
		return self.value
		
	def getType( self ):
		return self.cType
	
	def getPosition( self ):
		return self.pos

	def getInfo( self ):
		return [self.pos[X], self.pos[Y], self.value, self.cType, self.startId, self.endId]
	
	def setInfo( self, cid, value, type, pos=None, sid=None, eid=None ):
		self.cid = cid
		self.value = value
		self.cType = type
		self.pos = pos or self.pos
		self.startId = sid or self.startId
		self.endId = eid or self.endId
		
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

class CellReader():
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
	def __init__( self, dimensions, directory="puzzles/" ):
		CellReader.__init__( self, dimensions, CsvReader( directory ))
		
	def getCellInfo( self, data ):
		cellInfo = []
		
		for j in range(len( data )):
			for i in range( len( data[j] )):
				if data[j][i]: cellInfo.append( [i, j, data[j][i], 1, None, None] )
				
		return cellInfo
		
		
class JsonCellReader( CellReader ):
	def __init__( self, dimensions, directory="puzzles/" ):
		CellReader.__init__( self, dimensions, JsonReader( directory ))
		
	def getCellInfo( self, data ):
		cellInfo = []
		for row in range( len( data )):
			for col in range( len( data[row] )):
				xPos = col #i%self.dimensions[X]
				yPos = row #i/self.dimensions[Y]
				value = data[row][col]["number"]
				type = data[row][col]["type"] if "type" in data[row][col] else END
				startId = None
				endId = None
				if value: cellInfo.append( [xPos, yPos, value, type, startId, endId] )
		return cellInfo
		
	def writeGrid( self, name, cellList, full=False ):
		data = []
		row = []

		for i in range(len(cellList)):
			cell = cellList[i]
			v = cell.getValue()
			col = 0 if v else 255
			cellInfo = {"number": v, "color": {"r": col, "g": col, "b": col}}
			
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
	
