import swal from 'sweetalert';


$(document).ready(function() {
    $('.sidenav').sidenav();
})

function displayError(message) {
    swal.fire({
        title: 'Error!',
        text: `${message}`,
        icon: 'error',
        confirmButtonText: 'Ok',
    });
}