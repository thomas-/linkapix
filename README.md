g52grp
======

Repository for G52GRP group project (gp13-jaa)

Contents
========

The most notable and in production:

* /www contains production website code and is written in PHP
* /final contains the puzzle generator & solver and is written in Python

However *we still have early development prototypes* in the repo, which can
probably be *disregarded*:

* /linkapix contains the first prototype written in nodejs
* /ImageTest contains the prototype image analyser written in JavaScript

www
---

All the files that are web-visible live in here, it's where all the content for
the website lives and the scripts that power it. Notable files:

* `/www/js/linkapix-colour.js` contains the game logic and the code that makes
  the puzzles playable
* `/www/js/upload.js` contains the image analyser that converts an image into
  information for the server to handle
* `/www/js/generate.php` is the endpoint for handling the analysed images and
  returning puzzles
* `/www/js/MyOwnPix.php` is the main list of puzzles and login screen

final
-----

Puzzle generation/AI code that doesn't need to be public visible. Notable
files:

* `/final/generator.py` is the script that generates a puzzle from an array of
  data about an image
* `/final/solver.py` is the script that creates a solution from a generated
  puzzle

