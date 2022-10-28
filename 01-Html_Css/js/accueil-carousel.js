// Carousel
var slide = new Array("images/carousel/carousel.jpeg", "images/carousel/python-logo.jpg", "images/animaux/cheval.jpg");
// TODO: All carousel Images must have same size
let currentSlide = 0;
document.querySelector("#slide").src = slide[currentSlide];
function changeSlideWithButton(sens) {
    currentSlide += sens;
    if (currentSlide < 0) {currentSlide = slide.length - 1;}
    if (currentSlide > slide.length - 1){currentSlide = 0;}
    document.querySelector("#slide").src = slide[currentSlide];
}
// setInterval("changeSlideWithButton(1)", 3000);
