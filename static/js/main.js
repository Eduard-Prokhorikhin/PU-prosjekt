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
$(".dropbtn").click(function(event) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
        }
    }
});

// Makes it possible to prevent default on links etc.
document.addEventListener("click", {}, true);

// Calendar
today = new Date();
month = today.getMonth();
year = today.getFullYear();

function resetCalendar() {
    month = today.getMonth();
    year = today.getFullYear();
    updateCalendar();
}

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


let startDate = null;
let startDateElement = null;
let endDate = null;
let endDateElement = null;

function handleCellClick(event) {
    // Hierarchy: requestWrapper > div > table > tbody > tr > td
    if (! event.target.parentElement.parentElement.parentElement.parentElement.parentElement.classList.contains('requestWrapper')) {
        alert("RequestWrapper not found. There is something wrong... This should never happen.");
        return;
    }

    if (event.target.classList.contains('calendarUnavailable') || event.target.classList.contains('calendarOtherMonth')) {return;}

    const clickedDate = new Date(year, month, parseInt(event.target.innerHTML)+1);
    if (!startDate) {
        // If start date hasn't been set, set it to clicked date
        startDate = clickedDate;
        startDateElement = event.target;
        event.target.classList.add('calendarSelectedStart');
        document.getElementById('id_start_date').value = startDate.toISOString().slice(0,10);
    } else if (!endDate) {
        // If end date hasn't been set, set it to clicked date
        if (clickedDate < startDate) {
            return;
        }
        
        endDate = clickedDate;
        endDateElement = event.target;
        event.target.classList.add('calendarSelectedEnd');
        handleSelectedTimespan(startDate, endDate);
    } else {
        // If both start and end dates have been set, reset selection
        startDate = clickedDate;
        startDateElement = event.target;
        endDate = null;
        clearSelectedCells();
        event.target.classList.add('calendarSelectedStart');
        document.getElementById('id_start_date').value = startDate.toISOString().slice(0,10);
    }
}

function clearSelectedCells() {
    // Remove 'calendarSelectedStart' and 'calendarSelectedEnd' classes from all cells
    const cells = document.querySelectorAll('td');
    cells.forEach(cell => {
        cell.classList.remove('calendarSelectedStart', 'calendarSelectedEnd', 'calendarSelectedSpan');
    });
    document.getElementById('id_start_date').value = '';
    document.getElementById('id_end_date').value = '';
}

function handleSelectedTimespan(startDate, endDate) {
    document.getElementById('id_start_date').value = startDate.toISOString().slice(0,10);
    document.getElementById('id_end_date').value = endDate ? endDate.toISOString().slice(0,10) : '';
    if (!endDate) {return;}

    for (day of document.getElementsByClassName('calendarUnavailable')) {
        let dayDate = new Date(year, month, parseInt(day.innerHTML)+1);
        if (startDate <= dayDate && dayDate <= endDate) {
            alert("En eller flere av valgte dager er allerede leid ut. Velg en annen periode.");
            clearSelectedCells();
            return;
        }
    }

    let currentElement = startDateElement;
    if (startDateElement == endDateElement) {return;}
    while (currentElement.nextElementSibling != endDateElement) {
        if (currentElement == currentElement.parentElement.lastElementChild) {
            currentElement = currentElement.parentElement.nextElementSibling.firstElementChild;
        } else {
            currentElement = currentElement.nextElementSibling;
        }
        currentElement.classList.add('calendarSelectedSpan');
    }
}

if (document.getElementsByClassName('requestWrapper').length > 0 && document.querySelector('table')) {
    // Add event listener to calendar to track clicks
    const requestCalendar = document.querySelector('table');
    requestCalendar.addEventListener('click', handleCellClick);
}

// Calendar
today = new Date();
month = today.getMonth();
year = today.getFullYear();

function resetCalendar() {
    month = today.getMonth();
    year = today.getFullYear();
    updateCalendar();
}

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



function handleCellClick(event) {
    // Hierarchy: requestWrapper > div > table > tbody > tr > td
    if (! event.target.parentElement.parentElement.parentElement.parentElement.parentElement.classList.contains('requestWrapper')) {
        alert("RequestWrapper not found. There is something wrong... This should never happen.");
        return;
    }

    if (event.target.classList.contains('calendarUnavailable') || event.target.classList.contains('calendarOtherMonth')) {return;}

    const clickedDate = new Date(year, month, parseInt(event.target.innerHTML)+1);
    if (!startDate) {
        // If start date hasn't been set, set it to clicked date
        startDate = clickedDate;
        startDateElement = event.target;
        event.target.classList.add('calendarSelectedStart');
        document.getElementById('id_start_date').value = startDate.toISOString().slice(0,10);
    } else if (!endDate) {
        // If end date hasn't been set, set it to clicked date
        if (clickedDate < startDate) {
            return;
        }
        
        endDate = clickedDate;
        endDateElement = event.target;
        event.target.classList.add('calendarSelectedEnd');
        handleSelectedTimespan(startDate, endDate);
    } else {
        // If both start and end dates have been set, reset selection
        startDate = clickedDate;
        startDateElement = event.target;
        endDate = null;
        clearSelectedCells();
        event.target.classList.add('calendarSelectedStart');
        document.getElementById('id_start_date').value = startDate.toISOString().slice(0,10);
    }
}

function clearSelectedCells() {
    // Remove 'calendarSelectedStart' and 'calendarSelectedEnd' classes from all cells
    const cells = document.querySelectorAll('td');
    cells.forEach(cell => {
        cell.classList.remove('calendarSelectedStart', 'calendarSelectedEnd', 'calendarSelectedSpan');
    });
    document.getElementById('id_start_date').value = '';
    document.getElementById('id_end_date').value = '';
}

function handleSelectedTimespan(startDate, endDate) {
    document.getElementById('id_start_date').value = startDate.toISOString().slice(0,10);
    document.getElementById('id_end_date').value = endDate ? endDate.toISOString().slice(0,10) : '';
    if (!endDate) {return;}

    for (day of document.getElementsByClassName('calendarUnavailable')) {
        let dayDate = new Date(year, month, parseInt(day.innerHTML)+1);
        if (startDate <= dayDate && dayDate <= endDate) {
            alert("En eller flere av valgte dager er allerede leid ut. Velg en annen periode.");
            clearSelectedCells();
            return;
        }
    }

    let currentElement = startDateElement;
    if (startDateElement == endDateElement) {return;}
    while (currentElement.nextElementSibling != endDateElement) {
        if (currentElement == currentElement.parentElement.lastElementChild) {
            currentElement = currentElement.parentElement.nextElementSibling.firstElementChild;
        } else {
            currentElement = currentElement.nextElementSibling;
        }
        currentElement.classList.add('calendarSelectedSpan');
    }
}

if (document.getElementsByClassName('requestWrapper').length > 0 && document.querySelector('table')) {
    // Add event listener to calendar to track clicks
    const requestCalendar = document.querySelector('table');
    requestCalendar.addEventListener('click', handleCellClick);
}

//Category dropdown
var checkList = document.getElementById('dropdown-content');
checkList.getElementsByClassName('anchor')[0].onclick = function(evt) {
  if (checkList.classList.contains('visible'))
    checkList.classList.remove('visible');
  else
    checkList.classList.add('visible');
}

//Filter. THis is inspired by, but not fully copied from https://www.w3schools.com/howto/howto_js_portfolio_filter.asp 
filterSelection("all") // Execute the function and show all columns
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("single_post");
  if (c == "all") c = "";
  // Add the "show" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected
  for (i = 0; i < x.length; i++) {
    addClass(x[i], "hide");
    if (x[i].className.indexOf(c) > -1) removeClass(x[i], "hide");
  }
}

// Show filtered elements
function addClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// Hide elements that are not selected
function removeClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

// Add active class to the current button (highlight it)
var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function(){
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}