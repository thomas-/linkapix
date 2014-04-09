<?php
// start session and load relevant puzzle 
session_start();
	if (!empty($_GET['puzzleId'])) {
		$hasPuzzle = 1;
		include("conn.php");
        $puzzleId = mysql_real_escape_string($_GET['puzzleId']);
		$rs = mysql_query("SELECT * FROM Puzzle WHERE id = '$puzzleId'");
		$result = mysql_fetch_assoc($rs);
		$puzzledata = $result['data']; 
        $solutiondata = $result['solution'];
		mysql_close();
	}
	else {
		$hasPuzzle=0;	
	}
?>
<html>
<head>
<title>LINK-A-PIX</title>
<meta http-equiv="Content-Style-Type" content="text/css">
<link rel="shortcut icon" type="image/x-icon" href="images/puzzle.ico" media="screen" />
<LINK HREF="style.css" TYPE="text/css" REL="stylesheet">
<link href="css/GamePlay.css" rel="stylesheet" type="text/css" />
<link href="css/linkapix-colour.css" rel="stylesheet" type="text/css" />
<link href="css/bootstrap.min.css" rel="stylesheet" type="text/css" />
</head>
<body>
<!-- header -->
<table width="100%" height="100%"  border="0" cellpadding="0" cellspacing="0" background="images/rep_1.jpg">
  <tr>
    <td>&nbsp;</td>
    <td width="950" align="left" valign="top">
    <div style="padding-left:0px; padding-top:39px">
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
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
                      <td width="49"><img src="images/main_2.jpg" width="47" height="182" border="0"></td>
                      <td width="48"><img src="images/about_2.jpg" width="46" height="182" border="0"></td>
                      <td width="46"><img src="images/portfolio_2.jpg" width="44" height="182" border="0"></td>
                      <td width="46"><img src="images/services_2.jpg" width="44" height="182" border="0"></td>
                      <td><img src="images/contacts_2.jpg" width="44" height="182" border="0"></td>
                    </tr>
                  </table></td>
                </tr>
              </table>
              </td>
            </tr>
            <tr>
            
              <td height="1042" align="left" valign="top" background="images/back_4.jpg" style="border-top:12px solid #ffffff;background-repeat:no-repeat; background-position:bottom right; background-repeat:no-repeat">
<!-- Conetent --><!-- Game Window -->
<table width="100%" cellspacing="0" cellpadding="0">
  <tr>
    <td align="center">
		<div align="left" style="margin-left:10px"><a href="PICK-A-PIX.html" class="buttonEffect"><img src="images/back.png" alt="back"></a></div>
    	<div id="gameDisplayb">
            <div class="centered linkapix" >
            </div>
        </div>
        <div>
        
        
        
<!-- Game Buttons -->
        <table id="gameButtons" width="301" border="0" cellspacing="20" cellpadding="0" align="center">
  <tr>
    <td align="center">
    <a <?php if ($hasPuzzle==1) echo "href='GamePlay.php?puzzleId={$_GET['puzzleId']}'"; ?> class="buttonEffect restart_game"><img src="images/restart.png" width="32" height="32" alt="Restart" title="Restart"></a>
    </td>
    <td align="center">
    <a class="buttonEffect clear_incorrect"><img src="images/check_links.png" width="32" height="32" alt="Clear Incorrect Links" title="Clear Incorrect Links"></a>
    </td>
    <td align="center">
    <a class="buttonEffect show_solution"><img src="images/solution.png" width="32" height="32" alt="Show Solution" title="Show Solution"></a>
    </td>
    <td align="center">
    <a href="<?php if ($hasPuzzle==1) echo "Score_rank.php?puzzleId={$_GET['puzzleId']}" ?>" class="buttonEffect"><img src="images/highscore.png" width="32" height="32" alt="High Scores" title="View High Scores"></a>
    </td>
  </tr>
		</table>
        </div>
    </td>
  </tr>
  <tr>
<!-- Functional Buttons -->
    <td align="center">
    <div class="functionButtons">
    	<div class="btn-load load_puzzle" style="width:160px; height:45px;">
    		<img src="images/load-disabled.jpg" alt="load" title="Go to 'Play A Pix' to upload your favourite" />
        </div>
       		<img src="images/save-disabled.jpg" alt="save" title="Go to 'Play A Pix' to save your favourite" style="float:left;margin-left:160px;" />
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



<script src="js/jquery.js"></script>
<script src="js/linkapix-colour.js"></script>

  <script>
    destroy_puzzle();
    var puzzle = string_to_puzzle('<?=$puzzledata?>');
    build_puzzle(puzzle);
    var solution = string_to_puzzle('<?=$solutiondata?>');
    register_game_events();
  </script>

</body>
</html>
