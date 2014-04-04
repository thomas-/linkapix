<?php

session_start();
include("conn.php");

// if the user isn't logged in the system shouldn't let them hit this script
// so we abort
if(!isset($_SESSION['username'])) die("not logged in");

// if a puzzlename is set then we are saving,
if(isset($_POST['puzzlename'])) {
    // so we get the puzzlename and data and escape because SQL injection
    $puzzlename = mysql_real_escape_string($_POST['puzzlename']);
    $puzzledata = mysql_real_escape_string($_POST['puzzledata']);
    $username = mysql_real_escape_string($_SESSION['username']);

    // if that puzzlename exists already then we can't save and must die
    $rs = mysql_query("SELECT * from Puzzle WHERE name = '$puzzlename'");
    $rows = mysql_num_rows($rs);
    if ($rows > 0) die("Puzzle already exists with that name");

    // else however we continue and save the puzzle in the database
    $rs = mysql_query("INSERT INTO Puzzle (name, username, position, data)
        VALUES ('$puzzlename', '$username', 'testImages/unknown.jpg', '$puzzledata')");
    if ($rs) die("OK");
}
