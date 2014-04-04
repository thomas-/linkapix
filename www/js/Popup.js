// JavaScript Document
function topDiv(){ 
	var elem=document.createElement("div"); 
	elem.className="top-div"; 
	// create form tag
	var form = document.createElement("form");
	form.method="post";
	
	var oldPassword = document.createElement("label");
	oldPassword.innerHTML="Old Password";
	oldPassword.className="passwordLabel";
	var oldPasswordInput = document.createElement("input");
	oldPasswordInput.type = "password";	
	oldPasswordInput.className="passwordInput";
	oldPasswordInput.name = "oldPassword";
	oldPasswordInput.value="";
	oldPasswordInput.tabIndex="1";
	var clear1 = document.createElement("div");
	clear1.className="clear";
	
	var newPassword = document.createElement("label");
	newPassword.innerHTML="New Password";
	newPassword.className="passwordLabel";
	var newPasswordInput = document.createElement("input");
	newPasswordInput.type = "password";
	newPasswordInput.className="passwordInput";
	newPasswordInput.name = "newPassword";
	newPasswordInput.value="";
	newPasswordInput.tabIndex="2";
	var clear2 = document.createElement("div");
	clear2.className="clear";
	
	var newPasswordRetype = document.createElement("label");
	newPasswordRetype.innerHTML="Retype New";
	newPasswordRetype.className="passwordLabel";
	var newPasswordRetypeInput = document.createElement("input");
	newPasswordRetypeInput.type = "password";
	newPasswordRetypeInput.className="passwordInput";
	newPasswordRetypeInput.name = "newPasswordRetype";
	newPasswordRetypeInput.value="";
	newPasswordRetypeInput.tabIndex="3";
	var warnning = document.createElement("div");
	warnning.id="alert";
	
	var changePassword = document.createElement("input");
	changePassword.type="submit";
	changePassword.className="submitButton";
	changePassword.value="Change Password";
	changePassword.name="changePassword";
	changePassword.tabIndex="4";
	
	form.appendChild(oldPassword);
	form.appendChild(oldPasswordInput);
	form.appendChild(clear1);
	form.appendChild(newPassword);
	form.appendChild(newPasswordInput);
	form.appendChild(clear2);
	form.appendChild(newPasswordRetype);
	form.appendChild(newPasswordRetypeInput);
	form.appendChild(warnning);
	form.appendChild(changePassword);
	
	elem.appendChild(form);
	//=========create close DIV 
	var closeDiv=document.createElement("div"); 
	closeDiv.innerHTML=" Close "; 
	closeDiv.onclick=function(){ 
		document.body.removeChild(elem); 
		document.body.removeChild(alpha); 
	} 
	closeDiv.style.position="absolute"; 
	closeDiv.style.right="8px"; 
	closeDiv.style.top="4px"; 
	closeDiv.style.fontSize="12px"; 
	closeDiv.style.color="red"; 
	closeDiv.style.border="1px solid #333"; 
	closeDiv.style.backgroundColor="#eee"; 
	closeDiv.style.cursor="hand"; 
	elem.appendChild(closeDiv); 
	//=========append the top DIV to body 
	document.body.appendChild(elem); 
	var alpha = alphaDiv(elem); 
} 

function alphaDiv(el){ 
	var elem=document.createElement("div"); 
	elem.className="alphaDiv"; 
	elem.onclick=function(e){ 
		document.body.removeChild(elem); 
		document.body.removeChild(el); 
	} 
	document.body.appendChild(elem); 
	return elem; 
}