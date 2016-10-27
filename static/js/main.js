$(document).ready(function() {
	// hide descriptions
    $('.more').hide();
    
    // show/hide on click
    $('a.trigger').click(function() {
        $(this).nextAll('.more').slideToggle('fast');
        $(this).css("outline", 0);
        if ($(this).find('h2 i').hasClass('fa-chevron-down')) {
            $(this).find('h2 i').removeClass('fa-chevron-down').addClass('fa-chevron-up');
        } else {
            $(this).find('h2 i').removeClass('fa-chevron-up').addClass('fa-chevron-down');
        }
        return false;
    });

    // expand all
    $('a#expand_all').click(function() {
        $('.more').show();
        $('a.trigger').find('h2 i').removeClass('fa-chevron-down').addClass('fa-chevron-up');
        return false;
    });

    // hide all
    $('a#hide_all').click(function() {
        $('.more').hide();
        $('a.trigger').find('h2 i').removeClass('fa-chevron-up').addClass('fa-chevron-down');
        return false;
    });
});