/* Template Name: Qexal - Responsive Bootstrap 5 Landing Page Template
   Author: Themesbrand
   Version: 1.0.0
   Created: Jan 2019
   File Description: Main js file
*/

!function(e){"use strict";e("#side-menu").metisMenu(),e("#vertical-menu-btn").on("click",function(t){t.preventDefault(),e("body").toggleClass("sidebar-enable"),992<=e(window).width()?e("body").toggleClass("vertical-collpsed"):e("body").removeClass("vertical-collpsed")}),e("#sidebar-menu a").each(function(){var t=window.location.href.split(/[?#]/)[0];this.href==t&&(e(this).addClass("active"),e(this).parent().addClass("mm-active"),e(this).parent().parent().addClass("mm-show"),e(this).parent().parent().prev().addClass("mm-active"),e(this).parent().parent().parent().addClass("mm-active"),e(this).parent().parent().parent().parent().addClass("mm-show"),e(this).parent().parent().parent().parent().parent().addClass("mm-active"))}),e(".navbar-nav a").each(function(){var t=window.location.href.split(/[?#]/)[0];this.href==t&&(e(this).addClass("active"),e(this).parent().addClass("active"),e(this).parent().parent().addClass("active"),e(this).parent().parent().parent().parent().addClass("active"),e(this).parent().parent().parent().parent().parent().addClass("active"),e(this).parent().parent().parent().parent().parent().parent().addClass("active"),e(this).parent().parent().parent().parent().parent().parent().parent().addClass("active"))}),e(".right-bar-toggle").on("click",function(t){e("body").toggleClass("right-bar-enabled")}),e(document).on("click","body",function(t){0<e(t.target).closest(".right-bar-toggle, .right-bar").length||e("body").removeClass("right-bar-enabled")}),e(".dropdown-menu a.dropdown-toggle").on("click",function(t){return e(this).next().hasClass("show")||e(this).parents(".dropdown-menu").first().find(".show").removeClass("show"),e(this).next(".dropdown-menu").toggleClass("show"),!1}),e(function(){e('[data-toggle="tooltip"]').tooltip()}),e(function(){e('[data-toggle="popover"]').popover()}),Waves.init()}(jQuery);var bodyElem=document.documentElement,lightDarkBtn=(bodyElem.hasAttribute("data-bs-theme")&&"light"==bodyElem.getAttribute("data-bs-theme")?sessionStorage.setItem("data-layout-mode","light"):"dark"==bodyElem.getAttribute("data-bs-theme")&&sessionStorage.setItem("data-layout-mode","dark"),null==sessionStorage.getItem("data-layout-mode")?bodyElem.setAttribute("data-bs-theme","light"):sessionStorage.getItem("data-layout-mode")&&bodyElem.setAttribute("data-bs-theme",sessionStorage.getItem("data-layout-mode")),document.getElementById("light-dark-mode"));lightDarkBtn&&lightDarkBtn.addEventListener("click",function(t){bodyElem.hasAttribute("data-bs-theme")&&"dark"==bodyElem.getAttribute("data-bs-theme")?(bodyElem.setAttribute("data-bs-theme","light"),sessionStorage.setItem("data-layout-mode","light")):(bodyElem.setAttribute("data-bs-theme","dark"),sessionStorage.setItem("data-layout-mode","dark"))});

//  Window scroll sticky class add
function windowScroll() {
    const navbar = document.getElementById("navbar");
    if (
        document.body.scrollTop >= 50 ||
        document.documentElement.scrollTop >= 50
    ) {
        navbar.classList.add("nav-sticky");
    } else {
        navbar.classList.remove("nav-sticky");
    }
}

window.addEventListener('scroll', (ev) => {
    ev.preventDefault();
    windowScroll();
})


// Smooth scroll 
var scroll = new SmoothScroll('#navbar-navlist a', {
    speed: 500
});


// Contact Form
function validateForm() {
    var name = document.forms["myForm"]["name"].value;
    var email = document.forms["myForm"]["email"].value;
    var subject = document.forms["myForm"]["subject"].value;
    var comments = document.forms["myForm"]["comments"].value;
    document.getElementById("error-msg").style.opacity = 0;
    document.getElementById('error-msg').innerHTML = "";
    if (name == "" || name == null) {
        document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning error_message'>*Please enter a Name*</div>";
        fadeIn();
        return false;
    }
    if (email == "" || email == null) {
        document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning error_message'>*Please enter a Email*</div>";
        fadeIn();
        return false;
    }
    if (subject == "" || subject == null) {
        document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning error_message'>*Please enter a Subject*</div>";
        fadeIn();
        return false;
    }
    if (comments == "" || comments == null) {
        document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning error_message'>*Please enter a Comments*</div>";
        fadeIn();
        return false;
    }

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("simple-msg").innerHTML = this.responseText;
            document.forms["myForm"]["name"].value = "";
            document.forms["myForm"]["email"].value = "";
            document.forms["myForm"]["subject"].value = "";
            document.forms["myForm"]["comments"].value = "";
        }
    };
    xhttp.open("POST", "php/contact.php", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("name=" + name + "&email=" + email + "&subject=" + subject + "&comments=" + comments);
    return false;
}

function fadeIn() {
    var fade = document.getElementById("error-msg");
    var opacity = 0;
    var intervalID = setInterval(function () {
        if (opacity < 1) {
            opacity = opacity + 0.5
            fade.style.opacity = opacity;
        } else {
            clearInterval(intervalID);
        }
    }, 200);
}

// feather icon

feather.replace();


// Preloader

window.onload = function loader() { 
    setTimeout(() => {
        document.getElementById('preloader').style.visibility = 'hidden';
        document.getElementById('preloader').style.opacity = '0';
    }, 350);
} 

// Swicher
function toggleSwitcher() {
    var i = document.getElementById('style-switcher');
    if (i.style.left === "-189px") {
        i.style.left = "-0px";
    } else {
        i.style.left = "-189px";
    }
};

function setColor(theme) {
    document.getElementById('color-opt').href = './css/colors/' + theme + '.css';
    toggleSwitcher(false);
};



//
/********************* light-dark js ************************/
//
const btn = document.getElementById("mode");
btn.addEventListener("click", (e) => {
    let theme = localStorage.getItem("theme");
    if (theme == "light" || theme == "") {
        document.body.setAttribute("data-bs-theme", "dark");
        localStorage.setItem("theme", "dark");
    } else {
        document.body.removeAttribute("data-bs-theme");
        localStorage.setItem("theme", "light");
    }
});