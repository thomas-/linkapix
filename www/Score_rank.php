<html>
<head>
<title>LINK-A-PIX</title>
<meta http-equiv="Content-Style-Type" content="text/css">
<link rel="shortcut icon" type="image/x-icon" href="images/puzzle.ico" media="screen" />
<LINK HREF="style.css" TYPE="text/css" REL="stylesheet">
<link href="style.css" rel="stylesheet" type="text/css" />
</head>
<body>

<!-- header -->
<table width="100%" height="100%" border="0" cellpadding="0" cellspacing="0" background="images/rep_1.jpg">
  <tr>
    <td></td>
    <td width="700" align="center" valign="top">
    <div style="padding-left:0px; padding-top:39px">
      <table width="700" height="800" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td align="left" valign="top" bgcolor="#FFFFFF" style="border:1px solid #C5C5C5 ">
          <table width="700" height="785"  border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td height="199" colspan="2" align="left" valign="top"><table width="700" height="199"  border="0" cellpadding="0" cellspacing="0">
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
              <hr />
              </td>
            </tr>
            <tr>
              <td width="664" align="left" valign="top" background="images/back_4.jpg" style="border-top:12px solid #ffffff; background-repeat:no-repeat; background-position:bottom right; background-repeat:no-repeat; font-family: Arial, Helvetica, sans-serif; font-size: 24px; color: #F30;">
                <div style="font-size:50px; margin-left:20px; color: #F30;">Top 10</div>
                
               <div style="margin-top:20px">

<!-- Score rank -->
<table align="center" width="560px" style='font-family: Arial, Helvetica, sans-serif; font-size: 18px; color: #099;' cellpadding="8" cellspacing="0">
	<tr align="center">
		<th>Rank</th>
		<th>User</th>
		<th>Time</th>
	</tr>
<?php		
	include("conn.php");
					
	$puzzleID = $_GET['puzzle'];
	$rs = mysql_query("SELECT username, scores FROM Scores WHERE name = '$puzzleID' ORDER BY scores ASC");
					
for($i = 1; $i <= 10; $i++){
	echo "<tr align='center'>"; 
	switch ($i){
		case 1:
			echo "<td>" . "<img src='images/rank1.png'>" . "</td>";
			break;
		case 2:
			echo "<td>" . "<img src='images/rank2.png'>" . "</td>";
			break;
			case 3:
			echo "<td>" . "<img src='images/rank3.png'>" . "</td>";
			break;	
		default:
			echo "<td>" . $i . "</td>";
			break;
	}
	if($row = mysql_fetch_array($rs)){
		echo "<td>" . $row[0] . "</td>";
		echo "<td>" . $row[1] . "</td>";
	} 
	else {
		echo "<td>" . "N/A" . "</td>";
		echo "<td>" . "--:--:--" . "</td>";
	}
}
		mysql_close();
		echo "</tr>";
?> 
</table>
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
</body>
</html>
