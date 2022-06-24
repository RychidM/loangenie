const hamburger = document.querySelector(".hamburger"),
      burger_menu = document.querySelector(".burger-menu"),
      icns = document.querySelectorAll(".icns"),
      burger_close = document.querySelector(".hamburger-close");


hamburger.addEventListener('click', ()=>{
    burger_menu.classList.toggle('tog');

    icns.forEach(icon =>{
        icon.classList.toggle("uil-times");
    })
});      



// hamburger.addEventListener("click", ()=>{
//     burger_menu.classList.toggle("tog");
//     // burger_menu.style.top = '0';
//     hamburger.style.display = 'none';
//     // burger_close.style.display = 'block';
// });

// burger_close.addEventListener("click", ()=>{
//     burger_close.classList.toggle('togg');
//     burger_menu.classList.remove('tog');
//     // hamburger.style.display = 'block';
//     // burger_menu.style.top = '-450px';
//     // burger_close.style.display = 'none';
// });
