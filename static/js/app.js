var loader = function(e) {
    let file = e.target.files; 
    let output = document.getElementById("selector");

    if (file[0].type.match("image")) {
        //file is image
        let reader = new FileReader();

        reader.addEventListener("load", function(e) {
            let data = e.target.result;
            let image = document.createElement("img");
            image.src = data; 

            output.innerHTML = "";
            output.insertBefore(image, null);
            output.classList.add("image");
        });

        reader.readAsDataURL(file[0]);
    } else {
        //file is not image
        let show = "<span>Selected File: </span>";
        show = show + file[0].name; 

        output.innerHTML = show; 
        output.classList.add("active");

        if (output.classList.contains("image")) {
            output.classList.remove("image");
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
            // let form_data = "https://finalprojectdogsucf.s3.amazonaws.com/projectdata/american-bulldog.jpg";
            console.log(form_data);
            makeCall(form_data);
        })
        $('.box').click(function (event){
            let url = $(event.target).attr('src');
            console.log(url);
            makeCall(url);
        })
            // Make prediction by calling api /predict
        function makeCall(path){
            console.log(path)
            $.ajax({
                type: 'POST',
                url: '/predictresult1',
                data: path,
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
                    console.log('Results: ' + data);
                    console.log('Success!');
                },
            
            }).then(PlotDog);
        };
    }
    }

//add event listener for input 

let fileInput = document.getElementById("file");
fileInput.addEventListener("change", loader);