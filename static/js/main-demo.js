$(function() {

    $('.theme-options').addClass('active');

    $('.theme-options .toggle-btn').on('click', function() {
        $('.theme-options').toggleClass('active');
    });
    $('#anim-type').on('change', function() {
        $html = $('html');
        var animNum = $(this).val();
        if(animNum >= 0 &&  animNum <= 36 ) {
            if( animNum == 0 ) {
                $html.data('random-animation', true);
            } else {
                $('html').data('animation', parseInt(animNum, 10));
                $html.data('random-animation', false);
            }
        }
    });

    $('.theme-color li a').on('click', function(e) {
        var style_link = $(this).attr('href');
        $('link.site-color').attr('href', style_link);

        e.preventDefault();
    });
});

$(window).on('load', function(){
    var options = [], i;
    for( i = 1; i < 37 ; i++ )
    {
        options.push('<option value="' + i + '">' + i + '</option>');
    }

    setTimeout(function() {
        $('.theme-options').removeClass('active');
    },3000);


    $('#anim-type').append(options);
});
