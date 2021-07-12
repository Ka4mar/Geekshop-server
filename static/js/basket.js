window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function (){
        let t_href = event.target;
        // ctrl+f5 restart and cookie clean

        $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
            success: function (data){
                $('.basket_list').html(data.result);
            }
        });

        event.preventDefault();
    })
}