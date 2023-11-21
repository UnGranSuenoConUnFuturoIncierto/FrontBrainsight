// /********************* light-dark js ************************/
// //

// var bodyElem = document.documentElement;

// // layout mode
// if (bodyElem.hasAttribute("data-bs-theme") && bodyElem.getAttribute("data-bs-theme") == "light") {
//     sessionStorage.setItem("data-layout-mode", "light");
// } else if (bodyElem.getAttribute("data-bs-theme") == "dark") {
//     sessionStorage.setItem("data-layout-mode", "dark");
// }

// if (sessionStorage.getItem("data-layout-mode") == null) {
//     bodyElem.setAttribute("data-bs-theme", "light");
// } else if (sessionStorage.getItem("data-layout-mode")) {
//     bodyElem.setAttribute("data-bs-theme", sessionStorage.getItem("data-layout-mode"));
// }

// var lightDarkBtn = document.getElementById('light-dark-mode');
// if (lightDarkBtn) {
//     lightDarkBtn.addEventListener('click', function (event) {
//         if (bodyElem.hasAttribute("data-bs-theme") && bodyElem.getAttribute("data-bs-theme") == "dark") {
//             bodyElem.setAttribute('data-bs-theme', 'light');
//             sessionStorage.setItem("data-layout-mode", "light");
//         } else {
//             bodyElem.setAttribute('data-bs-theme', 'dark');
//             sessionStorage.setItem("data-layout-mode", "dark");
//         }
//     });
// }