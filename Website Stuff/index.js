
const a = document.getElementById("test").innerHTML = "New text";


function getHello() {
    const url = '/api'
    fetch(url)
    .then(response => response.json())  
    .then(json => {
        console.log(json);
        document.getElementById("demo").innerHTML = JSON.stringify(json)
    })
}


getHello()


   