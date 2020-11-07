var slideIndex, slides, dots;
function initGallery() {
    slideIndex = 0;
    slides=document.getElementsByClassName("imageHolder");
    slides[slideIndex].style.opacity=1;

    dots=[];
    var dotsContainer=document.getElementById("dotsContainer");

    for(var i=0; i<slides.length; i++) {
        var dot=document.createElement("span");
        dot.classList.add("dots");
        dot.setAttribute("onClick", "moveSlide("+i+")");
        dotsContainer.append(dot);
        dots.push(dot);
    }
    dots[slideIndex].classList.add("active");
}
initGallery();

function plusSlides(n) {
    moveSlide(slideIndex + n);
}

function moveSlide(n) {
    var i, current, next;
    var moveSlideAnimClass={
        forCurrent:"",
        forNext:""
    }
    if(n>slideIndex) {
        if (n>=slides.length) {n=0}
        moveSlideAnimClass.forCurrent="moveLeftCurrentSlide";
        moveSlideAnimClass.forNext="moveLeftNextSlide";
    } else if (n<slideIndex) {
        if (n<0) {n=slides.length-1}
        moveSlideAnimClass.forCurrent="moveRightCurrentSlide";
        moveSlideAnimClass.forNext="moveRightNextSlide";
    }
    if (n!=slideIndex) {
        next=slides[n];
        current=slides[slideIndex];
        for (i=0; i<slides.length; i++) {
            slides[i].className="imageHolder";
            slides[i].style.opacity=0;
            dots[i].classList.remove("active");
        }
        current.classList.add(moveSlideAnimClass.forCurrent);
        next.classList.add(moveSlideAnimClass.forNext);
        dots[n].classList.add("active");
        slideIndex=n;
    }
}
var timer=null;
function setTimer() {
    timer=setInterval (function () {
        plusSlides(1);
    }, 3000)
}
setTimer();

function playPauseSlides() {
    var playPauseBtn=document.getElementById("playPauseBtn");
    if (timer==null) {
        setTimer();
        playPauseBtn.style.backgroundPositionY="0px";
    } else {
        clearInterval(timer);
        timer=null;
        playPauseBtn.style.backgroundPositionY="-33px";
    }
}