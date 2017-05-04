$(document).ready( function() {

    $("#about-btn").click( function(event) {
        alert("the button using JQuery!");
    });
    $("#about-btn").click( function(event) {
	msgstr = $("#msg").html()
        msgstr = msgstr + "o"
        $("#msg").html(msgstr)
    });
    $("p").hover( function() {
            $(this).css('color', 'red');
    },
    function() {
            $(this).css('color', 'black');
    });
});

$(document).ready( function() {
    $('#about-btn').click(function() {
        changeRating(+1, $(this).attr('data-id')); // id - того, что лайкаем
    });
    $('.rating-minus').click(function() {
        changeRating(-1, $(this).attr('data-id')); // id - того, что лайкаем
    });
});

function changeRating(delta, thread_id) {
    $.post('/change_rating/', 
        {
	    'thread_id': thread_id,
            'delta': delta
        }, function(data) { //обработка ответа сервера, заменяем кол-во лайков
               $('.rating-value[data-id=" ' + thread_id + ' "]').text(data.new_rating);
               //$.('.rating-value[data-id="thread_id"]').text(data.new_rating);
        }
    )
}
