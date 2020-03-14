// Change later to submit form to database
// Submits form if all fields have been filled
const submitForm = () => {
    let message = document.getElementById("message");
    let username = document.getElementById("username");
    let password = document.getElementById("password");
    
    if (username.value === "" || password.value === "") {
        message.style.color = "#C70039"
        message.innerHTML = "Please fill in all fields"
    }
    else {
        message.style.color = "#9DC700"
        message.innerHTML = "Form Submitted"
    }
}

// Toggle to show the password by clicking the checkbox
const togglePassword = () => {
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
const checkMatchingPassword = () => {
    let password = document.getElementById("password");
    let confpassword = document.getElementById("confpassword");

    if (password.value === confpassword.value) {
        return true
    }
}

// Validate form when submitting
const validateForm = () => {
    let message = document.getElementById("message");
    let signup = document.getElementById("signup");
    
    if (signup) {
        if (checkMatchingPassword()) {
            message.style.color = "#9DC700"
            message.innerHTML = "Form Submitted"
            return true
        }
        else {
            message.style.color = "#C70039"
            message.innerHTML = "Passwords do not match"
            return false
        }
    }
}
