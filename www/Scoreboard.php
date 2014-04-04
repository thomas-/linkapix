<?php
// if doesn't log in or log off , jump to main puzzle store 
session_start(); 
	if (!isset($_SESSION['username'])) {
		echo "<script type='text/javascript'>
		window.location.href ='MyOwnPix.php'
		</script>";  
	}
	if (isset($_POST['logoff'])) {
		session_unset();
		echo "<script type='text/javascript'>
			window.location.href ='MyOwnPix.php'
			</script>";	
	}
?>
<html>
<head>
<title>LINK-A-PIX</title>
<meta http-equiv="Content-Style-Type" content="text/css">
<link rel="shortcut icon" type="image/x-icon" href="images/puzzle.ico" media="screen" />
<link href="css/Scoreboard.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="js/Popup.js"></script>
</head>
<body>
<!-- deal with changing password -->
<?php 
if (isset($_POST['changePassword'])) {
	echo "<script>
		document.body.onload = topDiv();
	</script>";	
	$old = $_POST['oldPassword'];
	$new = $_POST['newPassword'];
	$newRetype = $_POST['newPasswordRetype'];
	
	if ($old=="" || $new=="" || $newRetype=="") {
		unset( $_POST['oldPassword']);
		unset( $_POST['newPassword']);
		unset( $_POST['newPasswordRetype']);
	}
	else if (strlen($new) < 7) {
		unset( $_POST['oldPassword']);
		unset( $_POST['newPassword']);
		unset( $_POST['newPasswordRetype']);
		echo "<script>
		document.getElementById('alert').innerHTML='* Password Length Less Than 7!';
		</script>";	
	}
	else if ($new != $newRetype) {
		unset( $_POST['oldPassword']);
		unset( $_POST['newPassword']);
		unset( $_POST['newPasswordRetype']);
		echo "<script>
		document.getElementById('alert').innerHTML='* Passwords do not match!';
		</script>";	
	}
	else {
		include("conn.php");
		$rs = mysql_query("select password from Users where username = '{$_SESSION['username']}'");
		$result = mysql_fetch_row($rs);
	
		if ($old == $result[0]) {
			mysql_query("update Users set password = '{$new}' where username = '{$_SESSION['username']}'");
			mysql_close();
			echo "<script>
			document.getElementById('alert').innerHTML='* Password is Changed';
			</script>";	
		}
		else {
			mysql_close();
			echo "<script>
			document.getElementById('alert').innerHTML='* Old Password Is Incorrect !';
			</script>";	
		}
		unset( $_POST['oldPassword']);
		unset( $_POST['newPassword']);
		unset( $_POST['newPasswordRetype']);
	}	
}
?>
<!-- header -->
<table width="100%" height="100%"  border="0" cellpadding="0" cellspacing="0" background="images/rep_1.jpg">
  <tr>
    <td>&nbsp;</td>
    <td width="700" align="left" valign="top">
    <div style="padding-left:0px; padding-top:39px">
      <table width="700" height="800" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td align="left" valign="top" bgcolor="#FFFFFF" style="border:1px solid #C5C5C5 ">
          <table width="700"  border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td height="199" align="left" valign="top"><table width="700" height="199"  border="0" cellpadding="0" cellspacing="0">
                <tr align="left" valign="top">
                  <td width="495">
                  <div>
                  <a href="index.html"><img src="images/top_1.png" width="462" height="105"></a>
                  </div>
                  </td>
                  <td><table width="198" border="0" cellspacing="0" cellpadding="0" >
                    <tr align="left" valign="top">
                      <td width="41"><a href="#"><img src="images/main_2.jpg" width="39" height="182" border="0"></a></td>
                      <td width="40"><a href="#"><img src="images/about_2.jpg" width="38" height="182" border="0"></a></td>
                      <td width="39"><a href="#"><img src="images/portfolio_2.jpg" width="37" height="182" border="0"></a></td>
                      <td width="40"><a href="#"><img src="images/services_2.jpg" width="38" height="182" border="0"></a></td>
                      <td><a href="#"><img src="images/contacts_2.jpg" width="38" height="182" border="0"></a></td>
                    </tr>
                  </table></td>
                </tr>
              </table>
              <hr style="margin-top:16px;" />
              </td>
            </tr>
            <tr>
              <td height="556" align="left" valign="top" background="images/back_4.jpg" style="border-top:12px solid #ffffff;background-repeat:no-repeat; background-position:bottom right ; background-repeat:no-repeat">
              <table width="700" height="556"border="0" cellspacing="0" cellpadding="0">
                <tr align="left" valign="top">
                  <td width="438" height="100%" background="images/rep_2.jpg" style="background-position:top right; background-repeat:repeat-y ">
                  <div style="font-size:36px; margin-left:5px; color: #F30;">History Scores</div>
                  <div>
	<table border="0" cellspacing="0" cellpadding="0">
    <tr align="center">

<!-- load puzzle information -->
<?php
   	include("conn.php");
	
	$sql = mysql_query("select * from Scores where Puzzle.name = Scores.name AND username ='{$_SESSION['username']}'");
	
    $pagesize = 9; 
    $sum = mysql_num_rows($sql); 
    $count = ceil($sum/$pagesize);
    $lastPage = $count;
    $init = 1;
    $page_len = 3;
    $max_p = $count;    
    if(empty($_GET["page"]) || $_GET["page"]<0){
        $page = 1;
    }else{
        $page = $_GET["page"];
    }
    $off = ($page-1)*$pagesize; 
		
	$content = mysql_query("select Puzzle.name,position,scores from Puzzle,Scores where Puzzle.name = Scores.name AND Scores.username ='{$_SESSION['username']}' limit $off,$pagesize");

	for ($i=0;$i<9;$i++) {
		if ($result = mysql_fetch_array($content)) {
			if ($i!=0 && $i%3==0) {
				echo "</tr><tr align='center'>";	
			}
?>	

<td width="146" height="166" style="overflow:hidden">
<div style="height:130px; width:146px;margin-bottom:5px;"><img height="130" width="140" src="<?php echo $result[1]?>" alt="thumbnail"/></div>
<?php echo $result[2] ?></td>	

<?php				
		}
		else {
			if ($i==0) {
				echo "<p align='center'>Sorry . No Result !</p>";
				break;	
			}
			if ($i!=0 && $i%3==0) {
				echo "</tr><tr>";	
			}
			echo "<td width='136' height='166'>&nbsp;</td>";	
		}
	}

    $page_len = ($page_len%2)?$page_len:$page_len+1;
    $pageoffset = ($page_len-1)/2;
	$url = $_SERVER['REQUEST_URI'];
	$url = parse_url($uri);
	$url = $url[path];
    if($page!=1){
        $key.="<span><a href=\"".$url."?page=1"."\">First</a></span>&nbsp;&nbsp;";
        $key.="<span><a href=\"".$url."?page=".($page-1)."\">Previous</a></span>&nbsp;";
    }else{
        $key.="<span>First</span>&nbsp;&nbsp;";
        $key.="<span>Previous</span>&nbsp;";
    }
    if($lastPage>$page_len){
        if($page<=$pageoffset){
            $init=1;
            $max_p = $page_len;
        }else{
            if($page+$pageoffset>=$lastPage+1){
                $init = $lastPage - $page_len+1;
            }else{
                $init = $page-$pageoffset;
                $max_p = $page + $pageoffset;
            }
        }
    }
    for($i=$init;$i<=$max_p;$i++){
        if($i==$page){
            $key.="&nbsp;[&nbsp;".$i."&nbsp;]&nbsp;";    

        }
		else{
            $key.="&nbsp;<a href=\"".$url."?page=".$i."\">$i</a>&nbsp;";
        }
    }
    if($page < $lastPage){
        $key.="&nbsp;<span><a href=\"".$url."?page=".($page+1)."\">Next</a></span>&nbsp;";
        $key.="&nbsp;<span><a href=\"".$url."?page=".$lastPage."\">Last</a></span>&nbsp;";
    }else{
        $key.="&nbsp;<span>Next</span>&nbsp;";
        $key.="&nbsp;<span>Last</span>&nbsp;";
    }
	$key .= "&nbsp;Page ".$page." / ".$count;
	if ($count==0) {
		$key ="";	
	}
	mysql_close();
?>

</tr>
</table>
</div>

<div align="center" style="padding-top:5px"><?php echo $key; ?></div>
</td>
<td width="262" height="100%">

<!-- User System -->
<div style=" background:url(images/window.png) no-repeat;height:130px">
<br />
<br />
<p align="center" style="margin-top:0px">
Pick A Puzzle<br/>
Load A Puzzle<br />
Play A Puzzle<br />
Log In to Find More !<br />
</p>
</div>
<div class="form">

<h1 style="margin-left:10px">Welcome</h1>
<p align="center"><?php echo $_SESSION['username'] ?></p>
<div style="height:200px;margin:0 20%">
<table width="100%" height="200px">
	<tr>
		<td align="center">
			<a href="GeneralPuzzles.php"><img src="images/SystemPuzzles.png" alt="general" title="General Puzzles" align="top" ></a>			
		</td>
        <td align="center">
        	<a href="PrivatePuzzles.php"><img src="images/MyOwnPuzzle.png" alt="MyOwnPuzzle"  title="Private Puzzles" align="top" ></a>
        </td>
	</tr>
    <tr>
    	<td align="center">
        	<a href="UserUploadedPuzzles.php"><img src="images/UserUploadedPuzzles.png" alt="UserUploadedPuzzles" title="Uploaded Puzzles"  align="top" ></a>
        </td>
        <td align="center">
        	<a href="#" onClick="topDiv();return false"><img src="images/lock.png" alt="password" title="Change Password" align="top" ></a>    
        </td>
    </tr>
    <tr>
        <td align="center" colspan="2">
        	<form method="post">
<input type="submit" alt="logoff" name="logoff" id="logoff" value="" title="Log Off" />
</form>
        </td>
    </tr>
</table>
</div>
</div>
                  </td>
                </tr>
              </table></td>
            </tr>
          </table></td>
        </tr>
      </table>
    </div>      </td>
    <td>&nbsp;</td>
  </tr>
  <tr>
    <td height="100%">&nbsp;</td>
    <td width="558" height="100%" align="center" valign="top"><div style="padding-left:153px; padding-top:20px"></div></td>
    <td height="100%">&nbsp;</td>
  </tr>
</table>
</body>
</html>
