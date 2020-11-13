$(document).ready(function () {
    // Init

    // Predict
    $('#pred11').click(function () {
        var img_path = ' '
        console.log(img_path)
        // Make prediction by calling api /predictXception
        $.ajax({
            type: 'POST',
            url: '/manualpreds11',
            data: img_path,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function (data) {
                // Get and display the result
                $('#result12').fadeIn(600);
                $('#result12').text(data);
                console.log(data);
                console.log('Xception Success!');
            },
        }).then(PlotDog);
    });

});