<html>
<head>
<title>LINK-A-PIX</title>
<meta http-equiv="Content-Style-Type" content="text/css">
<link rel="shortcut icon" type="image/x-icon" href="images/puzzle.ico" media="screen" />
<LINK HREF="style.css" TYPE="text/css" REL="stylesheet">
<link href="css/Signup.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="js/Signup.js"></script>
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
          <table width="700" height="785"  border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td height="199" align="left" valign="top"><table width="700" height="199"  border="0" cellpadding="0" cellspacing="0">
                <tr align="left" valign="top">
                  <td width="495">
                  <div>
                  <a href="index.html"><img src="images/top_1.png" width="462" height="105"></a>
                  </div></td>
                  <td><table width="198" border="0" cellspacing="0" cellpadding="0" >
                   <tr align="left" valign="top">
                      <td width="41"><img src="images/main_2.jpg" width="39" height="182" border="0"></td>
                      <td width="40"><img src="images/about_2.jpg" width="38" height="182" border="0"></td>
                      <td width="39"><img src="images/portfolio_2.jpg" width="37" height="182" border="0"></td>
                      <td width="40"><img src="images/services_2.jpg" width="38" height="182" border="0"></td>
                      <td><img src="images/contacts_2.jpg" width="38" height="182" border="0"></td>
                    </tr>
                  </table></td>
                </tr>
              </table>
              </td>
            </tr>
            <tr>
              <td height="586" align="left" valign="top" background="images/back_4.jpg" style="border-top:12px solid #ffffff;background-repeat:no-repeat; background-position:bottom right; background-repeat:no-repeat">

<!-- Sign up form  -->
<div id="content">
	<h1>Welcome to LINK-A-PIX</h1>
    
    <div class="sign-up-form">
	<div class="article">
    <form method="post" onSubmit="return validate_form(this)">
        <div class="item">
            <label>Email</label>
            <input name="form_email" type="text" maxlength="60" tabindex="1" value="" />
        </div>
        <div>
            <div id="email_suggestion"  class="suggestion"></div>
        </div>
        <div class="item">
            <label>Password</label>
            <input name="form_password" type="password" tabindex="2" maxlength="20"/>
        </div>
        <div>
            <div id="password_suggestion"  class="suggestion"></div>
        </div>
        <div class="item">
        	<label>Username</label>
          	<input name="form_name" type="text" maxlength="15" tabindex="3" value=""/>
        </div>
        <div>
            <div id="name_suggestion"  class="suggestion"></div>
        </div>
        <div>
            <span class="tips">First impressions are lasting impressions !</span>
        </div>
        <div>
            <br />
            <input type="submit" value="Sign Up" class="submitButton" tabindex="4" name="submit" />
        </div>
    </form>
	</div>
    
	<div class="aside">            
	<p class="pl">&gt;&nbsp; Already have an account ?&nbsp;<a rel="nofollow" href="MyOwnPix.php">&nbsp;Login&nbsp;</a></p>
	</div>
	</div>
</div>            
             </td>
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

<?php 
if (isset($_POST['submit'])) {
	$valid = true;
	include("conn.php");
	$email = $_POST['form_email'];
	$password = $_POST['form_password'];
	$username = $_POST['form_name'];
	
	// check whether email and name are repeated
	$checkEmail = mysql_query("SELECT * FROM Users WHERE email = '$email'");
	$sum = mysql_num_rows($checkEmail);
	if ($sum >= 1) {
		$valid = false;
		echo "<script type='text/javascript'>
	document.getElementById('email_suggestion').innerHTML='* Email already exists !';
	</script>";
	}
	
	$checkName = mysql_query("SELECT * FROM Users WHERE username = '$username'");
	$sum = mysql_num_rows($checkName);
	if ($sum >= 1) {
		$valid=false;
		echo "<script type='text/javascript'>
	document.getElementById('name_suggestion').innerHTML='* Username already exists !';
	</script>";
	}
	
	if ($valid) {
		mysql_query("INSERT INTO Users(email,password,username) VALUES ('$email','$password','$username')");
		mysql_close();
		unset($_POST);
		echo "<script type='text/javascript'>
		alert('Welcome , $username');
		</script>";
	}
	else {
		mysql_close();
		unset($_POST);
	}
}
?>
</body>
</html>
