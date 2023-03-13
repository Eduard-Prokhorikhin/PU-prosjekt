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

document.getElementById("headerInputField").addEventListener("keypress", event => {
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

// Makes it possible to prevent default on links etc.
document.addEventListener("click", {}, true);

// Calendar
today = new Date();
month = today.getMonth();
year = today.getFullYear();

function updateCalendar(monthChange=0) {
    if (monthChange == -1) {
        if (month == 0) {
            month = 11;
            year -= 1;
        } else {
            month -= 1;
        }
    } else if (monthChange == 1) {
        if (month == 11) {
            month = 0;
            year += 1;
        } else {
            month += 1;
        }
    }

    document.getElementById("calendarMonth").innerHTML = new Date(year, month).toLocaleString('default', { month: 'long' });
    document.getElementById("calendarYear").innerHTML = year;

    calendar = document.getElementById("postCalendar");

    content = "<thead><th>Man</th><th>Tirs</th><th>Ons</th><th>Tors</th><th>Fre</th><th>Lør</th><th>Søn</th></thead><tbody><tr>";

    numberOfDays = new Date(year, month+1, 0).getDate();
    firstDay = new Date(year, month, 0).getDay();

    content += firstDay > 0 ? "<td class='calendarOtherMonth' colspan='" + firstDay + "'></td>" : "";

    for (let i = 1; i < numberOfDays+1; i++) {
        td = document.createElement("td");
        if (rentedDays.includes(new Date(year, month, i+1).toISOString().slice(0,10))) {
            td.classList.add('calendarUnavailable');
        }
        if (i == today.getDate() && year == today.getFullYear() && month == today.getMonth()) {
            td.classList.add('calendarToday');
        }
        td.innerHTML = i;
        content += td.outerHTML;
        if (new Date(year, month, i).getDay() == 0) {
            content += "</tr><tr>";
        }
    }

    rest = 7-(numberOfDays+firstDay)%7
    content += rest < 7 ? "<td class='calendarOtherMonth' colspan='" + rest + "'></td>" : "";

    content += "</tr></tbody>";

    document.getElementById("postCalendar").innerHTML = content;
}
