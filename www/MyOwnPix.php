<?php 
// if doesn't log in , jump to main puzzle store
// deal with login
session_start();
if (isset($_SESSION['username'])) {
		echo "<script type='text/javascript'>
		window.location.href ='GeneralPuzzles.php'
		</script>";  
	}
if (isset($_POST['submit'])) {
	include("conn.php");
	$email = $_POST['login'];
	$password = $_POST['password'];
	
	$rs = mysql_query("SELECT * FROM Users WHERE email = '$email' AND  password = '$password'");
	$sum = mysql_num_rows($rs);
	
	if ($sum >= 1 ) {
		$rs = mysql_query("SELECT username FROM Users WHERE email = '$email'");
		$result = mysql_fetch_row($rs);
		$name = $result[0]; 
		mysql_close();
		
		// successful
		$_SESSION['username'] = $name;
		echo "<script type='text/javascript'>
		window.location.href ='GeneralPuzzles.php'
		</script>";  
	}
}
?>
<html>
<head>
<title>LINK-A-PIX</title>
<meta http-equiv="Content-Style-Type" content="text/css">
<link rel="shortcut icon" type="image/x-icon" href="images/puzzle.ico" media="screen" />
<link href="css/MyOwnPix.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="js/MyOwnPix.js"></script>
</head>
<body>

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
                  <div style="margin:50px 0 0 0" align="center">
<form method="get" name="search">
<table border="0" cellpadding="0" cellspacing="0" class="tab_search">
<tr>
<td>
<input type="text" name="q" title="Search" class="searchinput" id="searchinput" onKeyDown="if (event.keyCode==13) {}" onBlur="if(this.value=='')value='- Search -';" onFocus="if(this.value=='- Search -')value='';" value="- Search -" size="10" style="width:250px;height:30px"/>
</td>
<td>
<input type="image" class="searchaction" onClick="if(document.forms['search'].searchinput.value=='- Search -')document.forms['search'].searchinput.value='';" src="images/submit.jpg"  hspace="2" border="0"/>

</td>
</tr>
</table>
</form>
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
              <hr />
              </td>
            </tr>
            <tr>
              <td height="556" align="left" valign="top" background="images/back_4.jpg" style="border-top:12px solid #ffffff;background-repeat:no-repeat; background-position:bottom right ; background-repeat:no-repeat">
              <table width="700" height="556"border="0" cellspacing="0" cellpadding="0">
                <tr align="left" valign="top">
                  <td width="438" height="100%" background="images/rep_2.jpg" style="background-position:top right; background-repeat:repeat-y ">
                  <div style="font-size:36px; margin-left:5px">General Puzzles</div>
                  <div>
	<table border="0" cellspacing="0" cellpadding="0">
    <tr align="center">
	
<!-- Load Puzzle information -->
<?php
   	include("conn.php");
	if(empty($_GET["q"])){
		$sql = mysql_query("select * from Puzzle where username ='admin'");
	}
	else {
		$search = trim($_GET["q"]);
		$sql = mysql_query("select * from Puzzle where name like '%$search%' AND username ='admin'");
	}
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
	
	if(empty($_GET["q"])){
		$content = mysql_query("select name,position from Puzzle where username ='admin' limit $off,$pagesize");
	}
	else {
		$content = mysql_query("select name,position from Puzzle where name like '%$search%' AND username ='admin' limit $off,$pagesize");
	}
    
	for ($i=0;$i<9;$i++) {
		if ($result = mysql_fetch_array($content)) {
			if ($i!=0 && $i%3==0) {
				echo "</tr><tr align='center'>";	
			}
?>	

<td width="146" height="166" style="overflow:hidden">
<div style="height:130px; width:146px; margin-bottom:5px;"><a href="GamePlay.php?puzzle=<?php echo $result[0] ?>"><img height="130" width="140" src="<?php echo $result[1]?>" alt="thumbnail"/></a></div>
<?php echo $result[0] ?></td>	

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

<!-- User System -->
<td width="262" height="100%">
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
<div id="login-form">
<form method="post" name="login_form" onSubmit="return validate_form(this)" style="padding-top:70px">
	<label for="login">Email</label>
	<input type="text" name="login" id="login"/>
	<div class="clear"></div>
		
	<label for="password">Password</label>
	<input type="password" name="password" id="password"/>
	<div class="clear"></div>
    <div id="alert">&nbsp;</div>

	<input type="submit" class="submitButton" name="submit" value="Log in"/>	
    <br />
    <br />
    <a href="Signup.php" target="_blank" style="margin-left:20%; margin-right:16%">Don't have an account?</a>
</form>
</div> 
<?php 
if (isset($_POST['submit'])) {
	if ($sum == 0) {
		mysql_close();
		unset($_POST['login']);
		unset($_POST['password']);
		
		// invalid user or password
		echo "<script type='text/javascript'>	document.getElementById('alert').innerHTML='* Invalid Email or Password!';
</script>";
	}
}
?>
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
