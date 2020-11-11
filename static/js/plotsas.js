// create Plot
$('#btn-predict').click(function () {
    var form_data = new FormData($('#upload-file')[0]);
    console.log(form_data)
    // // Show loading animation
    // $(this).hide();
    // $('.loader').show();

    // Make prediction by calling api /predict
    $.ajax({
        type: 'POST',
        url: '/plotfunc',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        async: true,
        success: function (data) {
            // // Get and display the result
            console.log(animals)
            console.log(probs)
            // $('.loader').hide();
            // $('#result').fadeIn(600);
            // $('#image-preview').show();
            // $('#result').text(' Result:  ' + data);
            // console.log('Results: ' + data)
            // console.log('Success!');
        },
    });
    })