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
  if (thisform.password.value.length < 7) { 
  	document.getElementById("alert").innerHTML="* Length must be more than 6!";
	thisform.password.focus();
    thisform.password.value="";
  	return false;
  }
  var emailReg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
  if (!emailReg.test(thisform.login.value)) {
   	document.getElementById("alert").innerHTML="* Not a valid e-mail address!";
	thisform.login.focus();
    thisform.password.value="";
  	return false;
  }
  var pwdReg = /^[_A-Za-z0-9]+$/;
  if (!pwdReg.test(thisform.password.value)) {
	document.getElementById("alert").innerHTML="* Only digit, letter, _ are allowed!";
  	thisform.password.focus();
    thisform.password.value="";
  	return false;	
  }	
}