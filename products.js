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
    let form=document.forms['form'];
    const inputName=document.getElementById("inputName").value;
    const inputProductionYear=document.getElementById("inputProductionYear").value;
    const inputPrice=document.getElementById("inputPrice").value;
    const inputColor=document.getElementById("inputColor").value;
    const inputSize=document.getElementById("inputSize").value;
    form.onsubmit=function(event){
        let errors=document.querySelectorAll(".error");
        for (let error of errors){
            error.classList.remove("display-error");
            document.getElementById('form').style.display='none';
        }    
        if(inputName==="" || inputColor==="" || inputPrice==="" || inputProductionYear==="" || inputSize===""){
            document.querySelector("."+"error").classList.add("display-error");
            document.querySelector("."+"error").innerHTML="All fields are required!"
            document.getElementById('form').style.display='none';

            return false;
        }
        if (!(inputColor.toLowerCase()==="red"||inputColor.toLowerCase()==="blue"||inputColor.toLowerCase()==="yellow"||
            inputColor.toLowerCase()==="κοκκινο"||inputColor.toLowerCase()==="μπλε"||inputColor.toLowerCase()==="κιτρινο"||
            inputColor.toLowerCase()==="κόκκινο"||inputColor.toLowerCase()==="κίτρινο"||inputColor==="1"||inputColor==="2"||inputColor==="3")){
                document.querySelector("."+"error").classList.add("display-error");
                document.querySelector("."+"error").innerHTML="Invalid Color. 1: red, 2:yellow, 3:blue"
                document.getElementById('form').style.display='none';

                return false;
        }
        if (!(inputSize.toLowerCase==="small"||inputSize.toLowerCase==="medium"||inputSize.toLowerCase==="large"||inputSize.toLowerCase==="extra large"||
            inputSize==="1"||inputSize==="2"||inputSize==="3"||inputSize==="4")){
                document.querySelector("."+"error").classList.add("display-error");
                document.querySelector("."+"error").innerHTML="Invalid Size. 1: small, 2: medium, 3:large, 4: extra large"
                document.getElementById('form').style.display='none';

                return false;                
        }
        if (!(/^\d+$/.test(inputProductionYear))){
            document.querySelector("."+"error").classList.add("display-error");
            document.querySelector("."+"error").innerHTML="Production year must be a positive integer"
            document.getElementById('form').style.display='none';
            event.preventDefault();
            return false;             
        }   
        if (parseInt(inputProductionYear)<0){
            document.querySelector("."+"error").classList.add("display-error");
            document.querySelector("."+"error").innerHTML="Production year must be a positive integer";
            document.getElementById('form').style.display='none';

            return false;  
        }
        if ((isNaN(inputPrice))){
            console.log(inputPrice);
            document.querySelector("."+"error").classList.add("display-error");
            document.querySelector("."+"error").innerHTML="Price must be a positive number";
            document.getElementById('form').style.display='none';

            return false;            
        }
        if (parseFloat(inputPrice)<0){
            document.querySelector("."+"error").classList.add("display-error");
            document.querySelector("."+"error").innerHTML="Price must be a positive number";
            document.getElementById('form').style.display='none';

            return false;              
        }
        document.querySelector("."+"success").classList.add("display-success");
        document.querySelector("."+"success").innerHTML="Your request has been completed successfully";
        document.getElementById('form').style.display='none';
        event.preventDefault();
    //"http://127.0.0.1:5000/add-product?"+"inputName="+name+"inputProductionYear"+year+"inputPrice"+price+"inputColor"+color+"inputSize"+size
    //console.log(name);
    fetch("http://127.0.0.1:5000/add-product?"+"name="+inputName+"/production_year="+inputProductionYear+"/price="+inputPrice+"/color="+inputColor+"/size="+inputSize, {
        method: 'POST',
       body: JSON.stringify()
    })
    .then(response => response.json())
    .then(data => {
        })
    .catch((error) => {
        console.error('Error:', error);
        })
    }
    // END CODE HERE
}