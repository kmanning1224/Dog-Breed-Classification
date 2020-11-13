$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();
})
  function readImage(file) {
    // Check if the file is an image.
    if (file.type && file.type[0]) {
    var reader = new FileReader();
    reader.addEventListener('click', (e) => {
        img.src = e.target.result;
        $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
        $('#imagePreview').show();
    })
    reader.readAsDataURL(file.type[0])
}
    $("#dog").click(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#btn-plot').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
})
document.getElementById("2x2_topleft_image_tag").src=image1;
{
        $.ajax({
            
            type: 'POST',
            url: '/predictresult1',
            data: path,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#result').fadeIn(600);
                $('#image-preview').show();
                $('#result').text(' Result:  ' + data);
                console.log('Results: ' + data);
                console.log('Success!');
            },
        }).then(PlotDog); //dont move this dingus
    }
  }