<?php session_start();

// if the user isn't logged in the system shouldn't let them hit this script
// so we abort
if(!isset($_SESSION['username'])) die("not logged in");

include("conn.php");

// if a puzzlename is set then we are saving,
if(isset($_POST['puzzlename'])) {
	
    // so we get the puzzlename and data and escape because SQL injection
    $puzzlename = mysql_real_escape_string($_POST['puzzlename']);
    $puzzledata = mysql_real_escape_string($_POST['puzzledata']);
    $solution = mysql_real_escape_string($_POST['solution']);
    $username = mysql_real_escape_string($_SESSION['username']);
	
    // we save the puzzle in the database
	$rs = mysql_query("INSERT INTO Puzzle (name, username, position, data, solution) VALUES ('$puzzlename', '$username', 'unknown.jpg', '$puzzledata', '$solution')");
	$lastId = mysql_insert_id();
	$_SESSION['lastId'] = $lastId;
	
	unset($_POST['puzzlename']);
	if ($rs) die("OK");
}

?>
