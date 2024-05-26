const api = "http://127.0.0.1:5000";

window.onload = () => {
    // BEGIN CODE HERE

    // END CODE HERE
}

searchButtonOnClick = () => {
    // BEGIN CODE HERE
    const search=document.getElementById("inputSearch2000").value;
    //console.log(search);
    path="http://127.0.0.1:5000/search?"+"search="+search
    fetch(path)
    .then(response =>response.json())
    .then(data =>
     {    
         let table = document.getElementById("dynamic_island").getElementsByTagName('tbody')[0];
         table.innerHTML = '';
         const x=data;
         console.log(x.length);
         for (let i = 0; i < data.length/6; i++){    
         // Δημιουργία νέας γραμμής
         let newRow = table.insertRow();
         // Δημιουργία κελιών και προσθήκη δεδομένων
         k=0;
         for (let j = i*6; j < 6*(i+1); j++) {  
          let newCell = newRow.insertCell(k);
          Text="  "+data[j];
          let newText = document.createTextNode(Text)
          newCell.appendChild(newText);
          k++;
          }
       }
     } /////MHN ΞΕΧΑΣΩ ΤΑ ΚΕΦΑΛΑΙΑΑΑΑΑΑΑ
     )
    .catch(error => console.error(error));  
    //array=search(name);
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