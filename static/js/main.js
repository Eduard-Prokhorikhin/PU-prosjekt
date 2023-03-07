// Clickable divs in header
$(".headerElement").click(function() {
    window.location = $(this).find("a").attr("href"); 
    return false;
});

// Clickable posts
$(".single_post").click(clickablePost);

function clickablePost(event) {
    event.stopPropagation();
    window.location = $(this).find("a").last().attr("href");
    return false;
}

// Prevent default on links
$("a").click(function(event) {
    event.preventDefault();
    window.location = $(this).attr("href");
    return false;
});

// Accordion effect for profile page
var acc = document.getElementsByClassName("accordion");

for (let i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        var panel = this.nextElementSibling;
        if (panel.style.display === "none") {
            this.getElementsByTagName("span")[0].innerHTML = "▲";
            panel.style.display = "grid";
        } else {
            this.getElementsByTagName("span")[0].innerHTML = "▼";
            panel.style.display = "none";
        }
    });
}


// Dark Mode
let darkMode = false;
const darkModeButton = document.getElementById("darkmode_button");

const lightcolors = {
    '--primary-color': '#ffcd80',
    '--secondary-color': '#ff9900',
    '--tertiery-color': '#efefef',
    '--bg-color1': '#efefef',
    '--bg-color2': '#fff',
    '--text-color1': '#fff',
    '--text-color2': '#000'
};

const darkcolors = {
    '--primary-color': '#ff9900',
    '--secondary-color': '#ffcd80',
    '--tertiery-color': '#1a1a1a',
    '--bg-color1': '#111',
    '--bg-color2': '#222',
    '--text-color1': '#000',
    '--text-color2': '#fff'
};

function enableDarkMode(bool) {
    if (bool) {
        localStorage.setItem("isDarkMode", "1");
        darkModeButton.classList.remove("fa-sun");
        darkModeButton.classList.add("fa-moon");
        for (let color in lightcolors) {
            document.documentElement.style.setProperty(color, lightcolors[color]);
        }
    } else {
        localStorage.setItem("isDarkMode", "0");
        darkModeButton.classList.remove("fa-moon");
        darkModeButton.classList.add("fa-sun");
        for (let color in darkcolors) {
            document.documentElement.style.setProperty(color, darkcolors[color]);
        }
    }
}

function toggleDarkMode() {
    darkMode = !darkMode;
    enableDarkMode(darkMode);
}

// Initialize darkmode setting
darkMode = localStorage.getItem("isDarkMode") == "1" ? true : false;
enableDarkMode(darkMode);

/* Disabled for now
document.getElementById("headerInputField").addEventListener("keypress", event => {
    if (event.key == "d") {
        toggleDarkMode();
    }
});
*/
// End Dark Mode



// Filter dropdown
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function dropdownFilter() {
    document.getElementById("myDropdown").classList.toggle("show");
}
  
// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
        if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

// Makes it possible to prevent default on links etc.
document.addEventListener("click", {}, true);
