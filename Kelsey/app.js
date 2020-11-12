var loader = function(e) {
    let file = e.target.files; 

    let show = "<span>Selected image: </span>" + file[0]

    let output = document.getElementById("selector");
    output.innerHTML = show; 
    output.classList.add("active");
}

//add event listener for input 

let fileInput = document.getElementById("file");
fileInput.addEventListener("change", loader);