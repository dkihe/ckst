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
}

// Toggle to show the password by clicking the checkbox
let togglePassword = () => {
    let signup = document.getElementById("signup");
    let password = document.getElementById("password");
    let confpassword = document.getElementById("confpassword");

    if (signup) {
        if (password.type === "password") {
            password.type = "text"
            confpassword.type = "text"
        }
        else {
            password.type = "password"
            confpassword.type = "password"
        }
    }
    else {
        if (password.type === "password") {
            password.type = "text"
        }
        else {
            password.type = "password"
        }
    }
}

// Check if passwords match
let checkMatchingPassword = () => {
    let password = document.getElementById("password");
    let confpassword = document.getElementById("confpassword");

    if (password.value === confpassword.value) {
        return true
    }
}

// Validate form when submitting
let validateForm = () => {
    let message = document.getElementById("message");

    if (checkMatchingPassword()) {
        return true
    }
    else {
        message.innerHTML = "Passwords do not match"
        return false
    }
}
