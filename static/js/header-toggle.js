let searchButton = document.getElementById("search-icon");
let navButton = document.getElementById("navbar-icon");
let links = document.getElementById("links");
let searchBox = document.getElementById("searchbox");


$(searchButton).click(function() {
    if ($(links).hasClass("show")) {
        $(navButton).click();
    }
});

$(navButton).click(function() {
    if ($(searchBox).hasClass("show")) {
        $(searchButton).click();
    }
});
