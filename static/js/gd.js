$(document).ready(function () {
    // Init

    // Predict
    $('#pred12').click(function () {
        var img_path = ' '
        console.log(img_path)
        // Make prediction by calling api /predictXception
        $.ajax({
            type: 'POST',
            url: '/manualpreds12',
            data: img_path,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function (data) {
                // Get and display the result
                $('#result13').fadeIn(600);
                $('#result13').text(data);
                console.log(' Result:  ' + data);
                console.log('Xception Success!');
            },
        }).then(PlotDog);
    });

});