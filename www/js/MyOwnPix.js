// JavaScript Document
function validate_form(thisform) {
  
  if (thisform.login.value==null || thisform.login.value==""){ 	
  	document.getElementById("alert").innerHTML="* Email must be filled out!";
  	thisform.login.focus();
    thisform.password.value="";
  	return false;
  }
  if (thisform.password.value==null || thisform.password.value=="") {
  	document.getElementById("alert").innerHTML="* Password must be filled out!";
  	thisform.password.focus();
    thisform.password.value="";
  	return false;
  }
  if (thisform.password.value < 7) { 
  	document.getElementById("alert").innerHTML="* Length must be more than 6!";
  	thisform.password.focus();
    thisform.password.value="";
  	return false;
  }
 
  var reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
  if (!reg.test(thisform.login.value)) {
   	document.getElementById("alert").innerHTML="* Not a valid e-mail address!";
    thisform.login.focus();
    thisform.password.value="";
  	return false;
  }
  document.getElementById("alert").innerHTML="&nbsp;";
}