/* Set the width of the side navigation to 250px */
let toggle = false;
let nav_width = "80px"

function ToggleNav() {
    if (toggle == false) {
        document.getElementById("mySidenav").style.width = nav_width;
        document.getElementById("icons").style.width = nav_width;
        document.body.style.backgroundColor = "rgba(0,0,0,0.6)";
        document.getElementById("topbar").style.borderColor = "rgba(0,0,0,0.6)";
        document.getElementById("background").style.opacity = "0.2";
        document.getElementById("burger").style.color = "white";
        toggle = true;
    } else {
        document.getElementById("mySidenav").style.width = "0";
        document.getElementById("icons").style.width = "0";
        document.body.style.backgroundColor = "white";
        document.getElementById("topbar").style.borderColor = "rgb(187, 187, 187)";
        document.getElementById("background").style.opacity = "0.8";
        document.getElementById("burger").style.color = "black";
        toggle = false;
    }
}
  

/* Clicking on the cross in the navbar closes it */
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("icons").style.width = "0";
    document.body.style.backgroundColor = "white";
    document.getElementById("topbar").style.borderColor = "rgb(187, 187, 187)";
    document.getElementById("background").style.opacity = "0.8";
    document.getElementById("burger").style.color = "black";
    toggle = false;
}

function bodyClose() {
    if (toggle) {
        document.getElementById("mySidenav").style.width = "0";
        document.getElementById("icons").style.width = "0";
        document.body.style.backgroundColor = "white";
        document.getElementById("topbar").style.borderColor = "rgb(187, 187, 187)";
        document.getElementById("background").style.opacity = "0.8";
        document.getElementById("burger").style.color = "black";
        toggle = false;
    } 
}

