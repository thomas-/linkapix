// JavaScript Document
function validate_form(thisform) {
  document.getElementById("email_suggestion").innerHTML="";
  document.getElementById("password_suggestion").innerHTML="";
  document.getElementById("name_suggestion").innerHTML="";
  
  if (thisform.form_email.value==null || thisform.form_email.value==""){ 	
  	document.getElementById("email_suggestion").innerHTML="* Email must be filled out!";
  	thisform.form_email.focus();
    thisform.form_password.value="";
  	return false;
  }
  else { 
  	var reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
  	if (!reg.test(thisform.form_email.value)) {
    	document.getElementById("email_suggestion").innerHTML="* Not a valid e-mail address!";
    	thisform.form_email.focus();
        thisform.form_password.value="";
  		return false;
    }	
  }

  if (thisform.form_password.value==null || thisform.form_password.value==""){ 
  	document.getElementById("password_suggestion").innerHTML="* Password must be filled out!";
  	thisform.form_password.focus();
    thisform.form_password.value="";
  	return false;
  }
  else {
  	if (thisform.form_password.value.length < 7 || thisform.form_password.value.length > 15) {
    	document.getElementById("password_suggestion").innerHTML="* Password  length must be in the range of [7 , 15]!";
  		thisform.form_password.focus();
        thisform.form_password.value="";
  		return false;
    }
	else {
		var pwdReg = /^[_A-Za-z0-9]+$/;
		if (!pwdReg.test(thisform.form_password.value)) {
			document.getElementById("password_suggestion").innerHTML="* Only digit, letter and underline are allowed!";
  			thisform.form_password.focus();
        	thisform.form_password.value="";
  			return false;	
		}	
	}
  }
  
  if (thisform.form_name.value==null || thisform.form_name.value==""){ 
    document.getElementById("name_suggestion").innerHTML="* Username must be filled out!";
  	thisform.form_name.focus();
    thisform.form_password.value="";
  	return false;
  }
  
}