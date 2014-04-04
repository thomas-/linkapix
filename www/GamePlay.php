<?php 
session_start();
include("conn.php");
	if (empty($_GET['puzzle'])) {
		$hasPuzzle = 0;	
    }
	else {
        $hasPuzzle = 1;
        $puzzle = mysql_real_escape_string($_GET['puzzle']);
		$rs = mysql_query("SELECT * FROM Puzzle WHERE name = '$puzzle'");
		$result = mysql_fetch_assoc($rs);
		$puzzledata = $result['data']; 
		mysql_close();
	}
?>
<html>
<head>
<title>LINK-A-PIX</title>
<meta http-equiv="Content-Style-Type" content="text/css">
<link rel="shortcut icon" type="image/x-icon" href="images/puzzle.ico" media="screen" />
<link href="css/GamePlay.css" rel="stylesheet" type="text/css" />
<link href="css/linkapix-colour.css" rel="stylesheet" type="text/css" />
<link href="css/bootstrap.min.css" rel="stylesheet" type="text/css" />
</head>
<body>
<table width="100%" height="100%"  border="0" cellpadding="0" cellspacing="0" background="images/rep_1.jpg">
  <tr>
    <td>&nbsp;</td>
    <td width="950" align="left" valign="top">
    <div style="padding-left:0px; padding-top:39px">
      <table width="100%" height="800" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td align="left" valign="top" bgcolor="#FFFFFF" style="border:1px solid #C5C5C5 ">
          <table height="785"  border="0" cellspacing="0" cellpadding="0">
            <tr>
              <td height="199" align="left" valign="top"><table width="100%" height="199"  border="0" cellpadding="0" cellspacing="0">
                <tr align="left" valign="top">
                  <td width="717">
                  <div>
                  <a href="index.html"><img src="images/top_1.png" width="626" height="147"></a>
                  </div></td>
                  <td width="231"><table width="198" border="0" cellspacing="0" cellpadding="0" >
                    <tr align="left" valign="top">
                      <td width="49"><a href="#"><img src="images/main_2.jpg" width="47" height="182" border="0"></a></td>
                      <td width="48"><a href="#"><img src="images/about_2.jpg" width="46" height="182" border="0"></a></td>
                      <td width="46"><a href="#"><img src="images/portfolio_2.jpg" width="44" height="182" border="0"></a></td>
                      <td width="46"><a href="#"><img src="images/services_2.jpg" width="44" height="182" border="0"></a></td>
                      <td><a href="#"><img src="images/contacts_2.jpg" width="44" height="182" border="0"></a></td>
                    </tr>
                  </table></td>
                </tr>
              </table>
              </td>
            </tr>
            <tr>
            <!--        CONTENT!!!!!!!Here you can change height!!!       -->
              <td height="1000" align="left" valign="top" background="images/back_4.jpg" style="border-top:12px solid #ffffff;background-repeat:no-repeat; background-position:bottom right; background-repeat:no-repeat">
<table width="100%" cellspacing="0" cellpadding="0">
  <tr>
    <td align="center">
    	<div id="sizetoolbar"> 		
    		<label for="width">Width:</label> 
            <input type="number" name="width" id="width" value="30">
    		<label for="height" style="margin-left:30px">Height:</label> 
    		<input type="number" name="height" id="height" value="30">
        </div>
    	<div id="gameDisplayb">
            <div class="centered linkapix">
            </div>
        </div>
        <div>
        
        
        
        
        <table id="gameButtons" width="301" border="0" cellspacing="20" cellpadding="0" align="center">
  <tr>
    <td>
    <a href="#"><img src="images/restart.png" width="32" height="32" alt="Restart" title="Restart"></a>
    </td>
    <td>
    <a href="#"><img src="images/solution.png" width="32" height="32" alt="Show Solution" title="Show Solution"></a>
    </td>
    <td>
    <a href="<?php if ($hasPuzzle==1) echo "Score_rank.php?puzzle={$_GET['puzzle']}" ?>"><img src="images/highscore.png" width="32" height="32" alt="High Scores" title="View High Scores"></a>
    </td>
    <td><a href="#" onClick="newWindow()"><img src="images/new-window.png" width="32" height="32" alt="New Window" title="Open New Window"></a>
    </td>
  </tr>
		</table>
        </div>
    </td>
  </tr>
  <tr>
    <td align="center">
    <div class="functionButtons">
    	<div class="btn-load" style="width:160px; height:45px;">
    		<a class="btn-file"><input type="file" /></a>
        </div>
        <a href="#" class="btn-save"><img src="images/save-btn.jpg" alt="save" title="Save" /></a>
    </div>
    </td>
  </tr>
</table>
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



<?php var_dump($puzzledata); ?>

<script src="js/jquery.js"></script>
<script src="js/linkapix-colour.js"></script>

  <script>
    destroy_puzzle();
    puzzle = string_to_puzzle('<?=$puzzledata?>');
    build_puzzle(puzzle);
  </script>

</body>
</html>
