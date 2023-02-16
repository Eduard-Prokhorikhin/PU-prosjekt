// Clickable divs in header
$(".headerElement").click(function() {
    window.location = $(this).find("a").attr("href"); 
    return false;
});

// Clickable posts
$(".single_post").click(function() {
    window.location = $(this).find("a").attr("href"); 
    return false;
});

// Return to home page


// Dark Mode
let darkMode = false;

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

function toggleDarkMode() {
    if (darkMode) {
        for (let color in lightcolors) {
            document.documentElement.style.setProperty(color, lightcolors[color]);
        }
    } else {
        for (let color in darkcolors) {
            document.documentElement.style.setProperty(color, darkcolors[color]);
        }
    }
    darkMode = !darkMode;
}

document.addEventListener("keypress", event => {
    if (event.key == "d") {
        toggleDarkMode();
    }
});
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