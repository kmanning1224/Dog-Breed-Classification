$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();
    $('#btn-plot').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').show();
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#btn-plot').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
    });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        // let form_data = "https://finalprojectdogsucf.s3.amazonaws.com/projectdata/american-bulldog.jpg";
        console.log(form_data);
        makeCall(form_data);
    })
    $('.box').click(function (event){
        let url = $(event.target).attr('src');
        console.log(url);
        makeCall(url);
    })
        // Make prediction by calling api /predict
    function makeCall(path){
        console.log(path)
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
        
        }).then(PlotDog);
    };
});