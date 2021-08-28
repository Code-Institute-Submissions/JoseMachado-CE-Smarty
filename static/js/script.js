$(document).ready(function () {
    $(".sidenav").sidenav();
    $(".collapsible").collapsible();
    $('.tabs').tabs();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('.datepicker').datepicker();
    $('select').formSelect();
    $('.tooltipped').tooltip();
});



$(function () {
    Profile.load();
});

Profile = {
    load: function () {
        this.links();
        this.social();
        this.accordion();
    },
    links: function () {
        $('a[href="#"]').click(function (e) {
            e.preventDefault();
        });
    },
    social: function () {
        $('.accordion .about-me .photo .photo-overlay .plus').click(function () {
            $('.social-link').toggleClass('active');
            $('.about-me').toggleClass('blur');
        });
        $('.social-link').click(function () {
            $(this).toggleClass('active');
            $('.about-me').toggleClass('blur');
        });
    },
    accordion: function () {
        var subMenus = $('.accordion .sub-nav').hide();
        $('.accordion > a').each(function () {
            if ($(this).hasClass('active')) {
                $(this).next().slideDown(100);
            }
        });
        $('.accordion > a').click(function () {
            $this = $(this);
            $target = $this.next();
            $this.siblings('a').removeAttr('class');
            $this.addClass('active');
            if (!$target.hasClass('active')) {
                subMenus.removeClass('active').slideUp(100);
                $target.addClass('active').slideDown(100);
            }
            return false;
        });
    }
}



function displayError(message) {
    Swal.Fire({
        title: 'Error!',
        text:`${message}`,
        icon: 'error',
        confirmButtonText: 'ok',
    });
}