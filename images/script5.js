document.addEventListener('DOMContentLoaded', function() {
    const signupForm = document.getElementById('signup-form');
    const signinForm = document.getElementById('signin-form');

    if (signupForm) {
        signupForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const username = document.getElementById('username').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            // Placeholder for actual sign-up logic
            console.log('User signed up with:', { username, email, password });
            alert('Sign-up successful!');
            // Redirect to sign-in page
            window.location.href = 'signin.html';
        });
    }

    if (signinForm) {
        signinForm.addEventListener('submit', function(event) {
            event.preventDefault();
            
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            
            // Placeholder for actual sign-in logic
            if (email === 'user@example.com' && password === 'password') {
                alert('Sign-in successful!');
                // Redirect to dashboard or home page
                window.location.href = 'dashboard.html';
            } else {
                alert('Invalid email or password');
            }
        });
    }
});