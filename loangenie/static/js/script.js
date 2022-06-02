const body = document.querySelector("body"),
      container = document.querySelector(".container"),
     sidebar = document.querySelector(".sidebar"),
     toggle = document.querySelector(".toggle"),
     modeSwitch = document.querySelector(".toggle-switch"),
     imgSwitch = document.querySelector(".cube-logo"),
     imgSwitch2 = document.querySelector(".rec-logo"),
     button = document.querySelector(".predict"),
     toast =  document.querySelector(".toast"),
     insights = document.querySelector(".insights"),
     message = document.querySelector(".message")
     clsIcon = document.querySelector(".times");

     
     toggle.addEventListener("click", ()=>{
        sidebar.classList.toggle("open");
        container.classList.toggle("open");

     });

     setTimeout(function(){
      message.style.display = "none"
    }, 5000);

