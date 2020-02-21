// Change later to submit form to database
let submitForm = () => {
    let message = document.getElementById("message")
    message.innerHTML = "Form Submitted"
}

// Toggle to show the password by clicking the checkbox
let togglePassword = () => {
    let password = document.getElementById("password")

    if (password.type === "password") {
        password.type = "text"
    }
    else {
        password.type = "password"
    }
}