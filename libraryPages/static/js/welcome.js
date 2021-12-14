var loginButton = document.getElementById('login')
var signUpButton = document.getElementById('SignUp')
var signUpButton2 = document.getElementById('special-button')
var myDiv = document.getElementById('main-div')
var logDiv = document.getElementById('login-div')
var signUpDiv = document.getElementById('signup-div')


loginButton.onclick = function(e) {
    myDiv.classList.add("animate__bounceOut")
    loginButton.style.display = "none";
    signUpButton.style.display = "none";
    myDiv.style.display = 'none'
    logDiv.style.display = 'flex';
    logDiv.classList.add("animate__bounceIn")
    logDiv.classList.add('auth')
}


signUpButton.onclick = function(){
    myDiv.classList.add("animate__bounceOut")
    loginButton.style.display = "none";
    signUpButton.style.display = "none";
    myDiv.style.display = 'none'
    signUpDiv.style.display = 'flex';
    signUpDiv.classList.add('animate__bounceIn')
    signUpDiv.classList.add('auth')
}

signUpButton2.onclick = function(){
    logDiv.classList.add("animate__bounceOut")
    logDiv.style.display = 'none';
    signUpDiv.style.display = 'flex';
    signUpDiv.classList.add('animate__bounceIn')
    signUpDiv.classList.add('auth')
}

//------------ Sign Up form validation ----------------
var signForm = document.getElementById('signup-form')
var form2 = document.getElementById('form2')
var signName = document.getElementById('signup-name')
var signPassword = document.getElementById('signup-password')
var signConfirmPassword = document.getElementById('signup-confirm-password')
var signEmail = document.getElementById('signup-email')
var signPhone = document.getElementById('signup-phone')
var signCollege = document.getElementById('signup-college')
var signID = document.getElementById('signup-id')

signForm.onclick = function(e){
    
    if(signName.value == '' || signName.value == null){
        var error = document.createElement('p')
        e.preventDefault()
        error.innerHTML += 'This field is required'
        error.style.margin = 0;
        signName.insertAdjacentElement('beforebegin',error)
    }

    if(signPassword.value != signConfirmPassword.value){
        var error = document.createElement('p')
        e.preventDefault()
        error.innerHTML += 'Password Do not match'
        error.style.margin = 0;
        signConfirmPassword.insertAdjacentElement('beforebegin',error)
    }

    
    if(signPassword.value == '' ||signPassword.value == null){
        var error = document.createElement('p')
        e.preventDefault()
        error.innerHTML += 'This field is required'
        error.style.margin = 0;
        signPassword.insertAdjacentElement('beforebegin',error)
    }

    
    if(signConfirmPassword.value == '' || signConfirmPassword.value == null){
        var error = document.createElement('p')
        e.preventDefault()
        error.innerHTML += 'This field is required'
        error.style.margin = 0;
        signConfirmPassword.insertAdjacentElement('beforebegin',error)
    }

    if(signEmail.value == '' || signEmail.value == null){
        var error = document.createElement('p')
        e.preventDefault()
        error.innerHTML += 'This field is required'
        error.style.margin = 0;
        signEmail.insertAdjacentElement('beforebegin',error)
    }

    if(signPhone.value == '' || signPhone.value == null){
        var error = document.createElement('p')
        e.preventDefault()
        error.innerHTML += 'This field is required'
        error.style.margin = 0;
        signPhone.insertAdjacentElement('beforebegin',error)
    }

    if(signID.value == '' || signID.value == null){
        var error = document.createElement('p')
        e.preventDefault()
        error.innerHTML += 'This field is required'
        error.style.margin = 0;
        signID.insertAdjacentElement('beforebegin',error)
    }

    if(signCollege.value == '' || signCollege.value == null){
        var error = document.createElement('p')
        e.preventDefault()
        error.innerHTML += 'This field is required'
        error.style.margin = 0;
        signCollege.insertAdjacentElement('beforebegin',error)
    }

}


//------------ Login Validation ------------------

var loginForm = document.getElementById('login-form')
var form1 = document.getElementById('form1')
var loginEmail = document.getElementById('login-email')
var loginPassword = document.getElementById('login-password')

loginForm.onclick = function(e){
    
    if(loginEmail.value == '' || loginEmail.value == null){
        var error = document.createElement('p')
        e.preventDefault()
        error.innerHTML += 'This field is required'
        error.style.margin = 0;
        loginEmail.insertAdjacentElement('beforebegin',error)
    }

    if(loginPassword.value == '' || loginPassword == null){
        var error = document.createElement('p')
        e.preventDefault()
        error.innerHTML += 'This field is required'
        error.style.margin = 0;
        loginPassword.insertAdjacentElement('beforebegin',error)
    }
}