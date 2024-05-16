const api = "http://127.0.0.1:5000";

const KEY = 'put_here_your_API_key';
let query = "";
const numResults = 3;

const input = document.querySelector('input');
const form = document.querySelector('form');

updateInput = (e) => {
    query = e.target.value;
}
input.addEventListener('input', updateInput);

submitted = (event) => {
    event.preventDefault();
    productFormOnSubmit();
}

form.onsubmit = submitted.bind(form);

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

    // END CODE HERE
}
