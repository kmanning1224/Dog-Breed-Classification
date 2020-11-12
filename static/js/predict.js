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
        console.log(form_data)
        // // Show loading animation
        // $(this).hide();
        // $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predictresult1',
            data: form_data,
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
                var a_one = data
                var a_two = '{{animal[1]}}'
                var a_three = '{{animal[2]}}'
                var a_four = '{{animal[3]}}'
                var one = '{{probs[0]}}'
                var two = '{{probs[1]}}'
                var three = '{{probs[2]}}'
                var four = '{{probs[3]}}'
                var p_one = Math.round(one * 100).toFixed(2);
                var p_two = Math.round(two * 100).toFixed(2);
                var p_three = Math.round(three * 100).toFixed(2);
                var p_four = Math.round(four * 100).toFixed(2);
                console.log(p_four)
        
        
                var trace1 = {
                x: [a_one, a_two, a_three, a_four],
                y: [one, two, three, four],
                type: "bar",
                }
        
                var data = [trace1];
        
                var layout = {
                title: `Probabilities of Dog Breed`,
                // hovermode: 'closest',
                margin: {
                    l:75,
                    r:75,
                    t:75,
                    b:75,
                    }
                }
        
                Plotly.newPlot("barplot", data, layout);
                console.log('Results: ' + data)
                console.log('Success!');
            },
        });
        })
        
    });