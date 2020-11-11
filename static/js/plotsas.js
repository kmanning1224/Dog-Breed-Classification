$('#btn-predict').click(function () {
        var form_data = new XMLHttpRequest();
        form_data.open('GET', 'https://dog-cl-ml.herokuapp.com/plotfunc');
        form_data.onload = function(){
            console.log(FormData.responseText);
        };
        form_data.send();
        // console.log(form_data) 

        var bar = d3.select('#barplot');
        bar.html("")

        // Make bar plot by calling api /predict
        $.ajax({
            url: '/plotfunc',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // // Get and display the result
                // $('.loader').hide();
                // $('#result').fadeIn(600);
                // $('#image-preview').show();
                // $('#result').text(' Result:  ' + data);
                // console.log('Results: ' + data)
                // console.log('Success!');}

        var a_one = '{{animal[0]}}'
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
    }
});
    });
