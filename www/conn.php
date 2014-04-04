<?php 
	$mysql_host =   	"localhost";
	$mysql_database = "linkapix";
	$mysql_user = "linkapix";
	$mysql_password = "braveheart";
	$conn = mysql_connect($mysql_host,$mysql_user,$mysql_password);
	if (!$conn) {
		die("Database Connection Error!");				// exception
	}
	mysql_select_db($mysql_database,$conn);
?>
