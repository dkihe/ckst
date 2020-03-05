// Change later to submit form to database
// Submits form if all fields have been filled
let submitForm = () => {
    let message = document.getElementById("message");
    let username = document.getElementById("username");
    let password = document.getElementById("password");
    if (username.value === "" || password.value === "") {
        message.innerHTML = "Please fill in all fields"
    }
    else {
        message.innerHTML = "Form Submitted"
    }
};

// Toggle to show the password by clicking the checkbox
let togglePassword = () => {
    let password = document.getElementById("password");

    if (password.type === "password") {
        password.type = "text"
    }
    else {
        password.type = "password"
    }
};