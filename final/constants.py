"""
	constants.py
	~~~~~~~~~

	This module contains the constants and settings that are
	used throughout the project.

	:Mandla Moyo, 2014.
"""

X = 0
Y = 1
VALUE = 2
TYPE = 3
START_ID = 4
END_ID = 5
COLOUR = 6

LIMIT = 4
MAX_LIMIT = 10
PID = 4

EMPTY = 0
END = 1
PATH = 2

XSIZE = 1
YSIZE = 2
FILENAME = 3

BLACK = hash( (0,0,0) )
WHITE = hash( (255,255,255) )
RED = hash( (255,0,0) )
GREEN = hash( (0,255,0) )
BLUE = hash( (0,0,255) )
YELLOW = hash( (255,255,0) )

CSV = "csv"
JSON = "json"

PUZZLE_DIRECTORY = "puzzles/"

OUTPUT_FILENAME_GENERATOR = "temp"
OUTPUT_FILENAME_SOLVER = "tempsolved"

OUTPUT_FILETYPE_GENERATOR = CSV
OUTPUT_FILETYPE_SOLVER = CSV

INIT_VALUE = [0,0,0,EMPTY,0,0,WHITE]
UNKNOWN = ' '