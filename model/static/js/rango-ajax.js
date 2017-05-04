$(document).ready( function() {
    $('#about-btn').click(function(ev) {
	ev.preventDefault(); // metod
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

/*
$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('127.0.0.1:8000/', {club_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
})


$(document).ready(function() {
    $('#mregister').live('click', function() {
        $('#register_form').ajaxSubmit({
            success: function(data, statusText, xhr, $form) {
                // Удаляем ошибки если были
                $form.find('.error').remove();
                if (data['result'] == 'success') {
                    // Делаем что-то полезное
                }
                else if (data['result'] == 'error') {
                    // Показываем ошибки
                    $form.replaceWith(data['response']);
                }
            },
            dataType: 'json'
        });
    });
})

*/

