const pwShowHidee = document.querySelectorAll(".showHideePw"),
      pwFields = document.querySelectorAll(".passwordCCC");

pwShowHidee.forEach(eyeIconn => {
    eyeIconn.addEventListener("click", ()=>{
        pwFields.forEach(pwField =>{
            if (pwField.type === "password") {
                pwField.type = "text"

                pwShowHidee.forEach(icon =>{
                    icon.classList.replace("uil-eye-slash", "uil-eye");
                })
            }else{
                pwField.type = "password";

                pwShowHidee.forEach(icon =>{
                    icon.classList.replace("uil-eye", "uil-eye-slash");
                })
            }
        })
    })
});