let dogselect = "";


$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                // $('#imagePreview').show('url(' + e.target.result + ')');
                $('#imagePreview').show();
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
    });

    // Predict
    $('#script').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // // Show loading animation
        // $(this).hide();
        // $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/getDataPlot',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#barplot').fadeIn(600);
                $('#image-preview').show();
                $('#barplot').plot(data);
                console.log('Results: ' + data)
                console.log('Success!');
            },
        });
        })
    });