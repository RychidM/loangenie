const pwShowHide = document.querySelectorAll(".showHidePw"),
      nameField = document.querySelectorAll(".name"),
      pwFields = document.querySelectorAll(".passwordCC"),
      spinner = document.querySelector(".buttn"),
      submit_text = document.querySelector(".button-text");

var getStarted = document.getElementById('getStartedBtn');
var logggin = document.getElementById('loggBtn');
const formSub = document.getElementById('formRe');
const subBtn = document.getElementById('buttn');

        // let date = new Date();
        //     let year = date.getFullYear();
        //     document.getElementById('currYr').innerHTML = year;

pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", ()=>{
        pwFields.forEach(pwField =>{
            if (pwField.type === "password") {
                pwField.type = "text"

                pwShowHide.forEach(icon =>{
                    icon.classList.replace("uil-eye-slash", "uil-eye");
                })
            }else{
                pwField.type = "password";

                pwShowHide.forEach(icon =>{
                    icon.classList.replace("uil-eye", "uil-eye-slash");
                })
            }
        })
    })
});



formSub.addEventListener('submit', ()=>{
    // subBtn.style.pointerEvents = "none";
    submit_text.style.visibility = 'hidden';
    spinner.classList.add('button-loader');
});




// closeBtn.addEventListener('click', closeForms)
// closesBtn.addEventListener('click', closeForms2)
// getStarted.addEventListener('click', popupLogin);
// logggin.addEventListener('click', popupLogin2);

// function popupLogin(){
//     popsup.style.visibility = 'visible';
    
//     // popsup.style.pointer-events = 'none'
// }
// function popupLogin2(){
//     popsup.style.visibility = 'visible'
// }
// function closeForms(){
//     popsup.style.visibility = 'hidden'
//     mainContainer.classList.remove("active")
// }
// function closeForms2(){
//     popsup.style.display = 'none'
// }


