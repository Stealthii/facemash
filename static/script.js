var fakeHeadBut = document.getElementById('head-file-button'),
realHeadInput = document.getElementById('head-file-input'),
fakeFaceBut = document.getElementById('face-file-button'),
realFaceInput = document.getElementById('face-file-input');

var MAX_SIZE = 600;

var c = document.createElement('canvas'),
  ctx = c.getContext('2d');

function _getResizedImageDataURL(img, maxWidth, maxHeight) {
      var w = img.width,
        h = img.height;
      if(w > h) {
        h *= MAX_SIZE / w;
        w = MAX_SIZE;
      } else {
        w *= MAX_SIZE / h;
        h = MAX_SIZE;
      }
      c.width = w;
      c.height = h;
      ctx.drawImage(img, 0, 0, w, h);
      return c.toDataURL('image/jpeg');
}

function _dataURLtoBlob(dataURL) {
  var PFX = ',base64,';
  if(dataURL.indexOf(PFX) === -1) {
    var ps = dataURL.split(','),
    ctype = ps[0].split(':')[1];,
    r = ps[1];

    return new Blob([r], { type:  ctype });
  }
}

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

    //var postedData = new FormData(this);

    //console.log(this, postedData);

    //return;

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
