let $request_form = $('#request-form');

function ajax_form_request(preview=true){
    let serializer = $request_form.serialize();
    if (preview === true){
        if (serializer !== ''){
            serializer += '&'
        }
        serializer += 'preview=1'
    }
    $.ajax({
        'method': 'POST',
        'data': serializer,
        success: function (data) {
            if (data.preview){
                $('#preview').html(data.text);
            }
            else{
                if (data.valid){
                    window.location.href = data.redirect;
                }
                else{
                    for (const key in data.errors) {
                        if (key !== '__all__') {
                            let $field = $request_form.find('[name="' + key + '"]');
                            $field.addClass('is-invalid');
                            $request_form.find('#' + key + '_errors').html(data.errors[key]);
                        }
                    }
                }
            }
        }
    })
}

$('.preview').on('click', function (event) {
    ajax_form_request(true);
});

$request_form.on('submit', function (event) {
    event.preventDefault();
    ajax_form_request(false);
});