$(document).ready(function () {
    // Init

    // Predict
    $('#pred1').click(function () {
        var img_path = ' '
        console.log(img_path)
        // Make prediction by calling api /predictXception
        $.ajax({
            type: 'POST',
            url: '/manualpreds1',
            data: img_path,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function (data) {
                // Get and display the result
                $('#result2').fadeIn(600);
                $('#result2').text(data);
                console.log(' Result:  ' + data);
                console.log('Xception Success!');
            },
        }).then(PlotDog);
    });

});