# Dog Breed Classification Project - Data Analytics UCF 2020
### Project worked on by [Chika Ozodiegwu](https://github.com/chikaozodiegwu) [Katherine Manning](https://github.com/kmanning1224) [Kelsey Wyatt](https://github.com/klw11j) and [Sofia Sotillo](https://github.com/SofiaAS1)
## Overview
Our goal with this project was to use the pre-trained Keras model Xception to run prediction on imported images of dogs and images available to click on the webpage.
We chose this topic out of an interest in becoming stronger in Machine Learning processes and because who doesn't love dogs?

**Due to the current issues that tensorflow has with large memory usage this app is not being hosted. Please clone our repository and run app.py to see the web app locally.**


## Our Process

* We began by deciding on whether to work with a self trained model or pre trained and came to the conclusion that this model could provide the best results for our goal in the least amount of time. 

* We used Python, Javascript, Ajax, HTML, CSS, Google Colab, Amazon S3 and Flask for this project.

### Data Rendering/Predicting
* We began by running our code within our Flask App to create the functions needed to run the Xception process. As you can see below we define our model, our file import request, and the image processing.


```
def load_model():
	# load the pre-trained Keras model
	global model
	model = Xception(weights='imagenet', include_top=True)
load_model()



def getfile(request):
	# Setup file retrieve from post
	f = request.files['file']

	# Save the file to uploads folder
	basepath = os.path.dirname(__file__)
	file_path = os.path.join(
		basepath, 'Uploads', secure_filename(f.filename))
	f.save(file_path)
	return file_path


def prepare_model(image_path, model):
    	# resize the input image and preprocess it
    
    img = image.load_img(image_path, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # predict
    predict = model.predict(x)
    # return the processed plot
    return predict
    
def ImgResult():
    list_of_files = glob.glob('./uploads/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)
    return latest_file
```



* Once these functions were complete we moved on to developing the end points
  - As you can see below, we made a seperate function for the imported files and the files served staticly on the webpage. 
  - We also created a plotting function that uses the main prediction function for file imports to plot the Top 4 results that Xception predicted.




```
@app.route('/',  methods=['GET'])
def index():

    return render_template('final.html')

@app.route('/prediction', methods=['GET','POST'])
def result1():
    results = DataResult1()
    return results


    
@app.route('/plotfunc')
def create_plot():
    img = ImgResult()
    # print(img)
    preds = prepare_model(img, model)

    pclass = decode_predictions(preds, top=4)
    #test prediction
    

    # plot prediction
    a_one = pclass[0][0][1]
    a_two = pclass[0][1][1]
    a_three = pclass[0][2][1]
    a_four = pclass[0][3][1]
    one = pclass[0][0][2]
    two = pclass[0][1][2]
    three = pclass[0][2][2]
    four = pclass[0][3][2]
    # print(a_one, a_two, a_three, a_four)
    animals = [a_one, a_two, a_three, a_four]
    probs = [one, two, three, four]
    dfs = pd.DataFrame({'Breed': animals,'Percentage': probs})
    jsons = dfs.to_json(orient="records")
    jsons = json.loads(jsons)
    jsons = json.dumps(jsons, indent=4)
    print(dfs)
    return jsons

@app.route('/manualpreds1', methods=['POST'])
def manualpred1():
    pred = predict1()
    print(pred)
    return pred		
```




* Once our Flask was somewhat established we moved forward to our Javascript queries and functions.
- We had three main types of Javascript files to create:
  - An Ajax Call to get the POST request.
  - A Plotly Function to plot the Top 4 results recieved from Xception
  - A Ajax Call to get the POST request for static files.
  
  
  
#### Predict File Import Function



```
$(document).ready(function () {
    // Init
    $('#result').hide();


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

        // Make prediction by calling api /predictXception
        $.ajax({
            type: 'POST',
            url: '/prediction',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('#result').fadeIn(600);
                $('#result').text(' Result:  ' + data);
                console.log(' Result:  ' + data);
                console.log('Xception Success!');
            },
        }).then(PlotDog);
    });

});
```


### Plot Imported File


```
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

```



### Predict Static Files


```
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
```


### Conclusion


As you can see from the screenshots below, our app processes static files and imports with Xception to predict results.

 ![Main Page - Static Images](https://i.gyazo.com/2f005769b957d9a104f829291ad67b9a.jpg)
 ![Main Page - Image Import](https://i.gyazo.com/cfa3905feeb769f7c533fe2e4bf80f35.png)


