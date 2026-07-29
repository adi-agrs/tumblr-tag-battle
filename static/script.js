
const coords = { x: 0, y: 0 };
const circles = document.querySelectorAll(".circle");
const cursor = document.querySelector(".cursor");

let isHolding = false;
let circleSize = 90;
const maxSize = 200;
const baseSize = 90;
let growSpeed = 5; // Adjust this value to control the growth speed
let circleOffset = 40;
let offsetGrowth = 2; // Adjust this value to control the offset growth speed

circles.forEach(function (circle, index) {
circle.x = 0;
circle.y = 0;
circle.style.backgroundColor = "white";
});

window.addEventListener("mousemove", function (e) {
coords.x = e.clientX;
coords.y = e.clientY;
});

function animateCircles() {
let x = coords.x;
let y = coords.y;

cursor.style.top = x;
cursor.style.left = y;

circles.forEach(function (circle, index) {
    circle.style.left = x - circleOffset + "px";
    circle.style.top = y - circleOffset + "px";
    circle.style.scale = (circles.length - index) / circles.length;
    circle.x = x;
    circle.y = y;

    const nextCircle = circles[index + 1] || circles[0];
    x += (nextCircle.x - x) * 0.3;
    y += (nextCircle.y - y) * 0.3;
});

requestAnimationFrame(animateCircles);
}

animateCircles();

window.addEventListener("scroll", function() {
    const scrollY = window.scrollY;
    document.querySelector(".bg").style.backgroundPosition = `0px ${scrollY * 3}px`;
});


window.addEventListener("mousedown", function() {
    isHolding = true;
});

window.addEventListener("mouseup", function() {
    isHolding = false;
});

function animateSize() {
    if (isHolding && circleSize < maxSize) {
        circleSize += growSpeed; //grow speed
        circleOffset += offsetGrowth; // Increase the offset when holding
    } else if (!isHolding && circleSize > baseSize) {
        circleSize -= growSpeed; //shrink speed
        circleOffset -= offsetGrowth; // Decrease the offset when not holding
    }

    circles.forEach(function (circle) {
        circle.style.width = circleSize + "px";
        circle.style.height = circleSize + "px";
        circle.style.borderRadius = circleSize + "px";
    });

    requestAnimationFrame(animateSize);
}

animateSize();

const form = document.querySelector("form");
const waveLeft = document.querySelector(".wave-left");
const waveRight = document.querySelector(".wave-right");

if (form) {
    form.addEventListener("submit", function(e) {
        e.preventDefault();
        
        waveLeft.style.width = "50vw";
        waveRight.style.width = "50vw";
        
        setTimeout(function() {
            document.querySelector(".content").classList.add("hidden");
            document.querySelector(".wave-left").style.width = "0";
            document.querySelector(".wave-right").style.width = "0";
            document.getElementById("loading-screen").style.display = "flex";
            form.submit(); // Now submit the form after the animation
        }, 900);

    });
}

const a = document.querySelector("a");

if (a) {
    a.addEventListener("click", function(e) {
        e.preventDefault();

        waveLeft.style.width = "50vw";
        waveRight.style.width = "50vw";

        setTimeout(function() {
            document.querySelector(".content").classList.add("hidden");
            document.querySelector(".wave-left").style.width = "0";
            document.querySelector(".wave-right").style.width = "0";
            window.location.href = a.href;
        }, 900);
    });
}
