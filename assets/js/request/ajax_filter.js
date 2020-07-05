
function ajax_filter(page=1){
    let $form = $('#filterRequest');
    let serializer = $form.serialize();
    if (serializer !== ''){
        serializer += '&'
    }
    serializer += 'page=' + page;
    $.ajax({
        'url': $form.attr('action'),
        'method': $form.attr('method'),
        'data': serializer,
        success: function (response) {
            $('.requests').html(response.requests).append(response.paginator);
        },
        error: function (errors) {
            console.log(errors.responseText);
        }
    })
}

$('.requests').on('click', '.page-link', function (event) {
    let $page = $(event.target);
    if (!$page.hasClass('active')){
        ajax_filter($page.attr('data-page'));
    }
});

$('#filterRequest').on('submit', function (event) {
   event.preventDefault();
   ajax_filter();
});