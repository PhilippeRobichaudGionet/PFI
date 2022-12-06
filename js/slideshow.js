var slideIndex = 0
var slides = document.querySelectorAll(".slideshow img")
for (let slide of slides) slide.classList.add("slide", "fading")
slideshow()
function slideshow() {
    for (let slide of slides) slide.style.display = "none"
    slideIndex++
    if (slideIndex > slides.length) slideIndex = 1
    slides[slideIndex - 1].style.display = "block"
    setTimeout(slideshow, 8000)
}