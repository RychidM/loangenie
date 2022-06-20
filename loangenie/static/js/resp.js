const hamburger = document.querySelector(".hamburger"),
      burger_menu = document.querySelector(".burger-menu"),
      burger_close = document.querySelector(".hamburger-close");



hamburger.addEventListener("click", ()=>{
    burger_menu.style.top = '0';
    hamburger.style.display = 'none';
    burger_close.style.display = 'block';
});

burger_close.addEventListener("click", ()=>{
    hamburger.style.display = 'block';
    burger_menu.style.top = '-450px';
    burger_close.style.display = 'none';
});