<?php

session_start();
include("conn.php");

if(!isset($_SESSION['username'])) die("not logged in");

if(isset($_POST['puzzlename'])) {
    $puzzlename = mysql_real_escape_string($_POST['puzzlename']);
    $puzzledata = mysql_real_escape_string($_POST['puzzledata']);
    $username = $_SESSION['username'];
    $rs = mysql_query("SELECT * from Puzzle WHERE name = '$puzzlename'");
    $rows = mysql_num_rows($rs);
    if ($rows > 0) die("Puzzle already exists with that name");
    $rs = mysql_query("INSERT INTO Puzzle (name, username, position, data)
        VALUES ('$puzzlename', '$username', 'testImages/unknown.jpg', '$puzzledata')");
    error_log(mysql_error());
    if ($rs) die("OK");
}
