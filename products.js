const api = "http://127.0.0.1:5000";

window.onload = () => {
    // BEGIN CODE HERE
    
    // END CODE HERE
}

searchButtonOnClick = () => {
    // BEGIN CODE HERE
    const search=document.getElementById("inputSearch2000").value;
    
    
    path="http://127.0.0.1:5000/search?"+"search="+search
    fetch(path)
    .then(response =>response.json())
    .then(data =>
     {    
         let table = document.getElementById("dynamic_island").getElementsByTagName('tbody')[0];
         table.innerHTML = '';
         if( data.length/6 <1){
            document.querySelector("."+"results").classList.add("display-results");
            document.querySelector("."+"results").innerHTML="No product was found with this name";
         }
         else{
            temp=data.length/6;
            document.querySelector("."+"results").classList.add("display-results");
            if(temp==1){
                document.querySelector("."+"results").innerHTML=temp+" result";
            }else{
                document.querySelector("."+"results").innerHTML=temp+" results"; 
            }
            
         }
         for (let i = 0; i < data.length/6; i++){    
         let newRow = table.insertRow();
         k=0;
         for (let j = i*6; j < 6*(i+1); j++) {  
          let newCell = newRow.insertCell(k);
          Text="  "+data[j];
          let newText = document.createTextNode(Text)
          newCell.appendChild(newText);
          k++;
          }
       }
     }
     )
    .catch(error => console.error(error));  
    // END CODE HERE
}

productFormOnSubmit = (event) => {
    // BEGIN CODE HERE
    let btn=document.querySelector('button');
    let inputs=document.querySelectorAll('input');

    let form=document.forms['form'];
    const inputName=document.getElementById("inputName").value;
    const inputProductionYear=document.getElementById("inputProductionYear").value;
    const inputPrice=document.getElementById("inputPrice").value;
    const inputColor=document.getElementById("inputColor").value;
    const inputSize=document.getElementById("inputSize").value;
    form.onsubmit=function(event){
        let s=document.querySelectorAll(".success");
        let errors=document.querySelectorAll(".error");
        for (let error of errors){
            error.classList.remove("display-error");
            document.getElementById('form').style.display='none';
        } 
        for (let succes of s){
            succes.classList.remove("display-success");
            document.getElementById('form').style.display='none';
        }   
        if(inputName==="" || inputColor==="" || inputPrice==="" || inputProductionYear==="" || inputSize===""){
            document.querySelector("."+"error").classList.add("display-error");
            document.querySelector("."+"error").innerHTML="All fields are required!"
            document.getElementById('form').style.display='none';

            return false;
        }
        if (!(/^\d+$/.test(inputProductionYear))){
            document.querySelector("."+"error").classList.add("display-error");
            document.querySelector("."+"error").innerHTML="Production year must be a positive integer";
            document.getElementById('form').style.display='none';
            return false;             
        }   
        if (parseInt(inputProductionYear)<0){
            document.querySelector("."+"error").classList.add("display-error");
            document.querySelector("."+"error").innerHTML="Production year must be a positive integer";
            document.getElementById('form').style.display='none';

            return false;  
        }
        if ((isNaN(inputPrice))){
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
        if (!(inputColor.toLowerCase()==="red"||inputColor.toLowerCase()==="blue"||inputColor.toLowerCase()==="yellow"||
            inputColor.toLowerCase()==="κοκκινο"||inputColor.toLowerCase()==="μπλε"||inputColor.toLowerCase()==="κιτρινο"||
            inputColor.toLowerCase()==="κόκκινο"||inputColor.toLowerCase()==="κίτρινο"||inputColor==="1"||inputColor==="2"||inputColor==="3")){
                document.querySelector("."+"error").classList.add("display-error");
                document.querySelector("."+"error").innerHTML="Invalid Color. 1: red, 2:yellow, 3:blue";
                document.getElementById('form').style.display='none';

                return false;
        }
        if (!(inputSize.toLowerCase()==="small"||inputSize.toLowerCase()==="medium"||inputSize.toLowerCase()==="large"||inputSize.toLowerCase()==="extra large"||
            inputSize==="1"||inputSize==="2"||inputSize==="3"||inputSize==="4")){
                document.querySelector("."+"error").classList.add("display-error");
                document.querySelector("."+"error").innerHTML="Invalid Size. 1: small, 2: medium, 3:large, 4: extra large";
                document.getElementById('form').style.display='none';

                return false;                
        }


        event.preventDefault();

        fetch("http://127.0.0.1:5000/add-product?"+"name="+inputName+"/production_year="+inputProductionYear+"/price="+inputPrice+"/color="+inputColor+"/size="+inputSize, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json'
        },
       body: JSON.stringify()
    })
    .then(response => response.json())
    .then(data => {
        alert("OK");
        inputs.forEach(input=>input.value='');    
        event.preventDefault();

        })
    .catch((error) => {
        document.querySelector("."+"error").classList.add("display-error");
        document.querySelector("."+"error").innerHTML="Unexpected Error. Please try again!";
        document.getElementById('form').style.display='none';
        })
    }
    // END CODE HERE
}