"""
	fileReader.py
	~~~~~~~~~

	This module implements a basic file I/O, creating a standard interface
	for either json or csv files.

	:Mandla Moyo, 2014.
"""

import json
import csv
import os


class FileReader():
	"""The base FileReader class simply controls directory
	management and error handling
	"""
	def __init__( self, directory ):
		if not os.path.isdir( directory ): raise IOError( "Directory '" + directory + "' does not exist" )
		self.directory = directory
		self.fileType = None
		
	def changeDirectory( self, newDirectory ):
		if not os.path.isdir( newDirectory ): raise IOError( "Directory '" + newDirectory + "' does not exist" )
		self.directory = newDirectory
		
	def readFile( self, name ):
		return None
		
	def writeFile( self, name ):
		pass
		
		
class CsvReader( FileReader ):
	"""CSVReader simply reads from or writes to a specified csv file, without
	any particular formatting or alteration of the handled data.
	"""
	def __init__( self, directory ):
		FileReader.__init__( self, directory )
		self.fileType = ".csv"
		
	def readFile( self, name ):
		data = []
		filepath = self.directory + name + self.fileType
		if not os.path.isfile( filepath ): raise IOError( "File '" + filepath + "' does not exist" )
					
		with open( filepath, 'rb' ) as f:
			reader = csv.reader(f)
			for row in reader:
				data.append([int(value) for value in row])
									
		return data

	def writeFile( self, name, data ):
		"""Takes a filename, and a 2d array containing the rows
		of data to be written.
		"""
		filepath = self.directory + name + self.fileType
		with open( filepath, 'w') as outfile:
			writer = csv.writer( outfile )
			writer.writerows( data )
		
		
class JsonReader( FileReader ):
	"""JsonReader simply reads from or writes to a specified json file, without
	any particular formatting or alteration of the handled data.
	"""
	def __init__( self, directory ):
		FileReader.__init__( self, directory )
		self.fileType = ".json"
		
	def readFile( self, name ):
		filepath = self.directory + name + self.fileType
		if not os.path.isfile( filepath ): raise IOError( "File '" + filepath + "' does not exist" )
		
		json_data = open( filepath )
		data = json.load( json_data )
		json_data.close()
		return data
		
	def writeFile( self, name, data ):
		"""Takes a filename, and a 2d array containing the rows
		of data to be written.
		"""
		filepath = self.directory + name + self.fileType
		with open( filepath, 'w' ) as outfile:
			json.dump( data, outfile )
		
		
		
'''		
class CsvReader( MapReader ):
	def getCellInfo( self ):
		cellInfo = []
		
		for j in range(len(self.template)):
			for i in range(len(self.template[j])):
				if self.template[j][i]: cellInfo.append( [i,j,self.template[j][i],1,None,None] )
				
		return cellInfo
	
	def readMap( self ):
		data = []
		filepath = 'csv/' + name + '.csv'
		if not os.path.isfile( filepath ): raise IOError
					
		with open( filepath, 'rb' ) as f:
			reader = csv.reader(f)
			for row in reader:
				data.append([int(value) for value in row])
									
		return data
		
	
	
class JsonReader( MapReader ):
	def getCellInfo( self ):
		cellInfo = []
		for i in range(len(data)):
			xPos = i%self.dimensions[X]
			yPos = i/self.dimensions[Y]
			value = data[i]["number"]
			type = 1
			startId = None
			endId = None
			if value: cellInfo.append( [xPos, yPos, value, type, startId, endId] )

		return cellInfo
		
	def readMap( self, name ):
		filepath = 'json/' + name + '.json'
		if not os.path.isfile( filepath ): return False
		
		json_data=open( name )
		data = json.load(json_data)
		json_data.close()
		return data
	
	def writeMap( self ):
		data = []
		for cell in self.cellList:
			v = cell.getValue()
			col = 0 if v else 255
			cellInfo = {"number": v, "color": {"r": col, "g": col, "b": col}}
			data.append( cellInfo )
			
		with open( 'solverOutput.txt', 'w' ) as outfile:
			json.dump( data, outfile )
		

	def getCellInfo( self ):
		cellInfo = []
		
		for j in range(len(self.template)):
			for i in range(len(self.template[j])):
				if self.template[j][i]: cellInfo.append( [i,j,self.template[j][i],1,None,None] )
				
		return cellInfo
	
	def read( self, name, fileType ):
		
		
		
	def loadTemplate( self, name ):
		template = []
		templatepathname = 'templates/' + name + '.csv'
		if not os.path.isfile( templatepathname ): return False
					
		with open(templatepathname,'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				template.append([int(value) for value in row])
									
		self.template = template
		
	def exportAsJson( self ):
		data = []
		for cell in self.cellList:
			v = cell.getValue()
			col = 0 if v else 255
			cellInfo = {"number": v, "color": {"r": col, "g": col, "b": col}}
			data.append( cellInfo )
			
		with open( 'solverOutput.txt', 'w' ) as outfile:
			json.dump( data, outfile )
		
	def importGrid( self, name="solverOutput.txt", type="json" ):
		"""Imports files either in 'json' or 'csv' format"""
		if type == "json":
			json_data=open( name )
			data = json.load(json_data)
			json_data.close()
		
			cellInfo = []
			for i in range(len(data)):
				x = i%self.dimensions[X]
				y = i/self.dimensions[Y]
				value = data[i]["number"]
				type = 1
				startId = None
				endId = None
				if value: cellInfo.append( [x, y, value, type, startId, endId] )

			self.setCellInfo( cellInfo )
			
		elif type == "
'''
		
