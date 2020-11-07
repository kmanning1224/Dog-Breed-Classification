window.onload = function() {
    let fileupload = document.getElementById("image-upload-path").value = "File: " + input.files[0].name
    let filepath = document.getElementById("image-upload").click();
    let button = document.getElementById("image-upload").click();

    button.onclick = function() {
        fileupload.click();
    };
    fileupload.onchange = function (){
        let filename = fileupload.nodeValue.split('\\')[fileupload.nodeValue.split('\\').length - 1];
        filepath.innerHTML = "<b> Selected File: </b>" + filename;
    };
};