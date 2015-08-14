var fakeHeadBut = document.getElementById('head-file-button'),
realHeadInput = document.getElementById('head-file-input'),
fakeFaceBut = document.getElementById('face-file-button'),
realFaceInput = document.getElementById('face-file-input');

fakeHeadBut.addEventListener('click', function(e) {
    realHeadInput.click();
});

fakeFaceBut.addEventListener('click', function(e) {
    realFaceInput.click();
});

$(realHeadInput).change(function (){
    var fileName = $(this).val().split('\\').pop();
    $(fakeHeadBut).text(fileName);
});

$(realFaceInput).change(function (){
    var fileName = $(this).val().split('\\').pop();
    $(fakeFaceBut).text(fileName);
});

$('#upload-form').submit( function( e ) {
    $('#submit-btn').text('Mashing...');
    $.ajax( {
        url: '/upload',
        type: 'POST',
        data: new FormData( this ),
        processData: false,
        contentType: false,
        success: function(data) {
            $('#main-content').html(data);
        },
        error: function(xhr, textStatus, errorThrown) {
            console.log(error);
            $('#submit-btn').text('MASH');
            $('#errors').text(xhr.responseText);
        }
    } );
    e.preventDefault();
} );
