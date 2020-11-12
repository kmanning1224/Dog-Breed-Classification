$(document).ready(function() { 
    
},
$('#btn-predict').click(function () {
    let form_data = new FormData($('#upload-file')[0]);
    let url = "/plotfunc"
    let bar2 = d3.select('#bar-plot')
    bar2.html("")

    $.ajax({
        url: '/plotfunc',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        async: true,
        success: function (data) {
            console.log(data)
            // // Get and display the result
            // $('.loader').hide();
            // $('#result').fadeIn(600);
            // $('#image-preview').show();
            // $('#result').text(' Result:  ' + data);
            // console.log('Results: ' + data)
            // console.log('Success!');}

    // var a_one = data[0]
    // console.log(a_one)
    // var a_two = data[1]
    // var a_three = data[2]
    // var a_four = data[3]
    // var one = data[0]
    // var two = data[1]
    // var three = data[2]
    // var four = data[3]
    // var p_one = Math.round(one * 100).toFixed(2);
    // var p_two = Math.round(two * 100).toFixed(2);
    // var p_three = Math.round(three * 100).toFixed(2);
    // var p_four = Math.round(four * 100).toFixed(2);



    // var trace1 = {
    // x: [a_one, a_two, a_three, a_four],
    // y: [one, two, three, four],
    // type: "bar",
    // }

    var data = data;

    var layout = {
    title: `Probabilities of Dog data`,
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
})
)
