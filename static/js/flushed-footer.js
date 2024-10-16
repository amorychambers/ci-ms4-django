/**
 * Code snippet taken from StackOverflow user Cory, linked in README
 * This script ensures the footer remains at the bottom of the page on all screensizes, without having it be sticky and overlaying the content
 */

function setFooterStyle() {
    var docHeight = $(window).height();
    var footerHeight = $('#footer').outerHeight();
    var footerTop = $('#footer').position().top + footerHeight;
    if (footerTop < docHeight) {
        $('#footer').css('margin-top', (docHeight - footerTop) + 'px');
    } else {
        $('#footer').css('margin-top', '');
    }
    $('#footer').removeClass('invisible');
}
$(document).ready(function() {
    setFooterStyle();
    window.onresize = setFooterStyle;
});