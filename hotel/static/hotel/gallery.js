var current = document.querySelector("#current");
var imgs = document.querySelectorAll(".imgs img");
var opacity = 0.4

imgs.forEach(img => 
    img.addEventListener('click', imgClick));


function imgClick(e) {
    // reset the opacity on picture prevy
    imgs.forEach(img => (img.style.opacity = 1));
    // click on the image to make it main photo
    current.src = e.target.src;
    // grey-out the grid image which main-photo
    e.target.style.opacity = opacity;
}