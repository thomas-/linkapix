<?php 
session_start();
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
<table width="100%" height="100%"  border="0" cellpadding="0" cellspacing="0" background="images/rep_1.jpg">
  <tr>
    <td>&nbsp;</td>
    <td width="950" align="left" valign="top">
    <div style="padding-left:0px; padding-top:39px">
      <table width="100%" height="800" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <td align="left" valign="top" bgcolor="#FFFFFF" style="border:1px solid #C5C5C5 ">
          <table  border="0" cellspacing="0" cellpadding="0">
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
<table width="100%" cellspacing="0" cellpadding="0">
  <tr>
    <td align="center">
    	<div align="left" style="margin-left:10px"><a href="PICK-A-PIX.html" class="buttonEffect"><img src="images/back.png" alt="back"></a></div>
        <div id="sizetoolbar">
            <p>		
    		<label for="width">Width:</label> 
            <input type="number" name="width" id="width" value="5">
    		<label for="height" style="margin-left:30px">Height:</label> 
            <input type="number" name="height" id="height" value="5">
            <br />
            <label for="difficulty">Difficulty:</label>
            <select name="difficulty" id="difficulty">
            <option value="5">Easy</option>
            <option value="7">Medium</option>
            <option value="10">Difficult</option>
            </select>
            </p>
            <p class="uploader"></p>
        </div>
    	<div id="gameDisplayb">
      <div class="progress progress-striped active" style="display: none;">
  <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 10%; transition:none;">
  </div>
</div>
                <div class="centered linkapix"></div>
        </div>
        <div>
   
        <table id="gameButtons" width="301" border="0" cellspacing="20" cellpadding="0" align="center">
  <tr>
    <td align="center">
    <a class="buttonEffect"><img src="images/restart.png" width="32" height="32" alt="Restart" title="Restart"></a>
    </td>
    <td align="center">
    <a class="show_upload_solution buttonEffect"><img src="images/solution.png" width="32" height="32" alt="Show Solution" title="Show Solution"></a>
    </td>
    <td align="center">
<?php 
	if (isset($_SESSION['username'])) {
?>
    <a href="PrivatePuzzles.php" class="buttonEffect"><img src="images/highscore.png" width="32" height="32" alt="My Own Puzzles" title="View 'My Own Puzzles'"></a>
<?php 
	}
	else {
?>
	<img src="images/highscore-disabled.png" width="32" height="32" alt="My Own Puzzles" title="Log in to view private puzzles">
<?php 
	}
?>
    </td>
  </tr>
		</table>
        </div>
    </td>
  </tr>
  <tr>
    <td align="center">
    <div class="functionButtons"> 
    <form action="uploadImg.php" method="post" target="uploadImg" enctype="multipart/form-data" id="userFile">
    	<div class="btn-load" style="width:160px; height:45px;">
    		<a class="btn-file buttonEffect">
           
            <input class="joint upld" type="file" name="uploadedFile" id="imgInp" /><img src="images/load-btn.jpg" alt="load" title="Load" />
            
            </a>
        </div>
<?php 
if (isset($_SESSION['username'])) {
?>
        <a class="btn-save buttonEffect" id="savebutton"><img src="images/save-btn.jpg" alt="save" title="Save"/></a>
<?php 
}
else {
?>
	<img src="images/save-disabled.jpg" alt="save" title="Log in to save" style="float:left;margin-left:160px;"/>
<?php	
}
?>
	</form>
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
<script src="js/upload.js"></script>

<iframe name="uploadImg" src="" style="display:none"></iframe>
</body>
</html>
