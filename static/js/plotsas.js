function PlotDog() {
let queryUrl = '/plotfunc'

d3.json(queryUrl,function(data){
    let bar = d3.select('#barplot');
    bar.html("");
    
    let breed1 = [];
    let breed2 = [];
    let breed3 = [];
    let breed4 = [];
    let p1 = [];
    let p2 = [];
    let p3 = [];
    let p4 = [];

    breed1.push(data[0].Breed);
    breed2.push(data[1].Breed);
    breed3.push(data[2].Breed);
    breed4.push(data[3].Breed);
    console.log(breed3);

    p1.push(data[0].Percentage);
    p2.push(data[1].Percentage);
    p3.push(data[2].Percentage);
    p4.push(data[3].Percentage);
    console.log(p1);  
    
    let one = Math.round(p1[0] * 100).toFixed(2);
    let two = Math.round(p2[0] * 100).toFixed(2);
    let three = Math.round(p3[0] * 100).toFixed(2);
    let four = Math.round(p4[0] * 100).toFixed(2);
    console.log(two);

    let b1 = breed1[0].replace('_', ' ');
    let b2 = breed2[0].replace('_', ' ');
    let b3 = breed3[0].replace('_', ' ');
    let b4 = breed4[0].replace('_', ' ');
    console.log(b3);

    // var yValue = [one, two, three, four];

    var data = [
        {
          x: [b1, b2, b3, b4],
          y: [one, two, three, four],
          type: 'bar',
          marker: {
            color: ['#2171b5', '#6baed6', '#bdd7e7', '#eff3ff'],
            },
        }],

    var layout = {
          title: `Probability of Dog Breeds`,
          font: {
                size: 12
              },
          showlegend: false,
          xaxis: {
                tickangle: -45
              },
          yaxis: {
                zeroline: false,
                gridwidth: 2,
              },
          height:600,
          width: 600,
            }
          

    Plotly.newPlot('barplot', data, layout);

    }); 

}






// $('#btn-plot').click(function () {
//         var form_data = new XMLHttpRequest();
//         form_data.open('GET', '/plotfunc');
//         form_data.onload = function(){
//             console.log(FormData.responseText);
//         };
//         form_data.send();
//         // console.log(form_data) 

//         var bar = d3.select('#barplot');
//         bar.html("")

//         // Make bar plot by calling api /predict
//         $.ajax({
//             url: '/plotfunc',
//             data: form_data,
//             contentType: false,
//             cache: false,
//             processData: false,
//             async: true,
//             success: function (data) {
//                 // // Get and display the result
//                 // $('.loader').hide();
//                 // $('#result').fadeIn(600);
//                 // $('#image-preview').show();
//                 // $('#result').text(' Result:  ' + data);
//                 // console.log('Results: ' + data)
//                 // console.log('Success!');}

//         var a_one = '{{animal[0]}}'
//         var a_two = '{{animal[1]}}'
//         var a_three = '{{animal[2]}}'
//         var a_four = '{{animal[3]}}'
//         var one = '{{probs[0]}}'
//         var two = '{{probs[1]}}'
//         var three = '{{probs[2]}}'
//         var four = '{{probs[3]}}'
//         var p_one = Math.round(one * 100).toFixed(2);
//         var p_two = Math.round(two * 100).toFixed(2);
//         var p_three = Math.round(three * 100).toFixed(2);
//         var p_four = Math.round(four * 100).toFixed(2);
//         console.log(p_four)


//         var trace1 = {
//         x: [a_one, a_two, a_three, a_four],
//         y: [one, two, three, four],
//         type: "bar",
//         }

//         var data = [trace1];

//         var layout = {
//         title: `Probabilities of Dog Breed`,
//         // hovermode: 'closest',
//         margin: {
//             l:75,
//             r:75,
//             t:75,
//             b:75,
//             }
//         }

//         Plotly.newPlot("barplot", data, layout);
//     }
// });
//     });