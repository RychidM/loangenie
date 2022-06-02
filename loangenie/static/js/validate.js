const form = document.getElementById('signUpForm'),
      username = document.getElementById('userName'),
      email = document.getElementById('emailID'),
      org = document.getElementById('org'),
      password = document.getElementById('password'),
      conPass = document.getElementById('conPass');

form.addEventListener('submit', (e) =>{
  e.preventDefault();

  checkInputs();
});

function checkInputs() {
  const usernameValue = username.value.trim()
  const emailValue = email.value.trim()
  const orgValue = org.value.trim()
  const passwordValue = password.value.trim()
  const conPassValue = conPass.value.trim()

  if (userNameValue === "") {
    setErrorFor(username, "Please fill form")
    
  }else{
    serSuccessFor(username)
  }
}

function setErrorFor(input, message){
  const formControl = input.parentElement;
  const small = formControl.querySelector('small');

  small.innerHtml = message;

  formControl.className = 'input-field error'
}

function setSuccessFor(input) {
  const formControl = input.parentElement;
  formControl.className = 'input-field success'
  
}