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
    // console.log(breed3);

    p1.push(data[0].Percentage);
    p2.push(data[1].Percentage);
    p3.push(data[2].Percentage);
    p4.push(data[3].Percentage);
    // console.log(p1);  
    
    let one = Math.round(p1[0] * 100).toFixed(1);
    let two = Math.round(p2[0] * 100).toFixed(1);
    let three = Math.round(p3[0] * 100).toFixed(1);
    let four = Math.round(p4[0] * 100).toFixed(1);
    // console.log(two);

    let b1 = breed1[0].replace('_', ' ').replace('_', ' ');
    let b2 = breed2[0].replace('_', ' ').replace('_', ' ');
    let b3 = breed3[0].replace('_', ' ').replace('_', ' ');
    let b4 = breed4[0].replace('_', ' ').replace('_', ' ');
    // console.log(b3);

    var xValues = [b1, b2, b3, b4];
    var yValues = [one, two, three, four]

    var trace1 = {
          x: xValues,
          y: yValues,
          type: 'bar',
          text: [`${yValues[0]}%`, `${yValues[1]}%`,`${yValues[2]}%`,`${yValues[3]}%`],
          textposition: 'auto',
          hoverinfo: 'none',
          marker: {
            color: ['#238b45', '#74c476', '#bae4b3', '#edf8e9'],
            line: {
                color: '#00441b',
                width: 1.5
              }
          },
        };
    
    var data = [trace1];

    var layout = {
          title: `Top Four Probabilities of Dog Breed`,
          font: {
                size: 16
              },
          showlegend: false,
          xaxis: {
                // tickangle: -45
              },
          yaxis: {
                zeroline: false,
                gridwidth: 2,
              },
          height: 600,
          width: 1150,
            }
          

    Plotly.newPlot('barplot', data, layout);

    }); 

}
