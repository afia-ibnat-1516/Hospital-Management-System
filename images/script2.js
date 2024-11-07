document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Basic form validation
    if (username === ""  email === ""  password === "" || confirmPassword === "") {
        displayErrorMessage("All fields are required.");
        return;
    }

    if (password !== confirmPassword) {
        displayErrorMessage("Passwords do not match.");
        return;
    }

    // Here you would typically send the data to the server for account creation
    // For this example, we are just simulating a successful sign-up
    alert("Sign up successful!");
    // Redirect to the sign-in page or another page
    window.location.href = "signin.html";
});

function displayErrorMessage(message) {
    const errorMessageElement = document.getElementById('errorMessage');
    errorMessageElement.textContent = message;
}