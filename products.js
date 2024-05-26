const api = "http://127.0.0.1:5000";

window.onload = () => {
    // BEGIN CODE HERE

    // END CODE HERE
}

searchButtonOnClick = () => {
    // BEGIN CODE HERE

    // END CODE HERE
}

productFormOnSubmit = (event) => {
    // BEGIN CODE HERE
    const inputName=document.getElementById("inputName").value;
    const inputProductionYear=document.getElementById("inputProductionYear").value;
    const inputPrice=document.getElementById("inputPrice").value;
    const inputColor=document.getElementById("inputColor").value;
    const inputSize=document.getElementById("inputSize").value;
    //"http://127.0.0.1:5000/add-product?"+"inputName="+name+"inputProductionYear"+year+"inputPrice"+price+"inputColor"+color+"inputSize"+size
    //console.log(name);
    fetch("http://127.0.0.1:5000/add-product?"+"name="+inputName+"/production_year="+inputProductionYear+"/price="+inputPrice+"/color="+inputColor+"/size="+inputSize, {
        method: 'POST',
       body: JSON.stringify()
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        })
    .catch((error) => {
        console.error('Error:', error);
        })
    // END CODE HERE
}