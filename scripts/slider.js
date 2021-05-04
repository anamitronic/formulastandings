$(document).ready(function(){
    $(".slider").diyslider({
    width: "100px", // width of the slider
    height: "100px", // height of the slider
    display: 1, // number of slides you want it to display at once
    loop: 1 // disable looping on slides
}); // this is all you need!

// use buttons to change slide
$("#go-left").bind("click", function(){
    // Go to the previous slide
    $(".slider").diyslider("move", "back");
});
$("#go-right").bind("click", function(){
    // Go to the previous slide
    $(".slider").diyslider("move", "forth");
});
});