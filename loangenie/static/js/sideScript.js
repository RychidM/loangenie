const burger = document.querySelector(".burger-menu"),
      sidebarr = document.querySelector(".sidebar"),
      body = document.getElementsByTagName('main')[0],
      right = document.querySelector(".right"),
      icons = document.querySelectorAll(".iconss");

burger.addEventListener('click', ()=>{
    sidebarr.classList.toggle('open');
    body.classList.toggle('open');
    right.classList.toggle('open');
   

    icons.forEach(icon =>{
        icon.classList.toggle("uil-times");
    })
});
