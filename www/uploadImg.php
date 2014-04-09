<?php session_start();
		$imgFile = $_FILES["uploadedFile"];
		$type = $_FILES["uploadedFile"]["type"];
		$size = $_FILES["uploadedFile"]["size"];
		$imgName = $_FILES["uploadedFile"]["name"];
		$temp_name = $_FILES["uploadedFile"]["tmp_name"];
		
		// random function
		function randomNum($length) {   
        	$hash = 'CR-';   
        	$chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz';   
        	$max = strlen($chars) - 1;   
        	mt_srand((double)microtime() * 1000000);   
            	for($i = 0; $i < $length; $i++) {   
                	$hash .= $chars[mt_rand(0, $max)];   
            	}   
        	return $hash;   
    	}
		
		// rename file
		$filename=explode(".",$imgName);   
        do {   
            $filename[0]= randomNum(10);
            $name=implode(".",$filename);      
            $uploadfile='./upload/'.$name;
        } 
		while(file_exists($uploadfile));
		
		move_uploaded_file($temp_name,$uploadfile);
		
		include("conn.php");
		$lastID = $_SESSION['lastId'];
		unset($_SESSION['lastId']);
		$rs = mysql_query("Update Puzzle Set position = '{$uploadfile}' where username = '{$_SESSION['username']}' AND id = '{$lastID}' ");
		mysql_close();
?>