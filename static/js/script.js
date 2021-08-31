$(document).ready(function () {
    $(".sidenav").sidenav();
    $(".collapsible").collapsible();
    $('.tabs').tabs();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('.datepicker').datepicker();
    $('select').formSelect();
    $('.tooltipped').tooltip();
});


function displayError(message) {
    Swal.Fire({
        title: 'Error!',
        text:`${message}`,
        icon: 'error',
        confirmButtonText: 'ok',
    });
}