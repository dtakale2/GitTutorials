// script.js

// Function to validate registration form
function validateRegistrationForm() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username.trim() === '') {
        alert('Please enter a username.');
        return false;
    }

    if (password.trim() === '') {
        alert('Please enter a password.');
        return false;
    }

    return true;
}

// Function to validate login form
function validateLoginForm() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username.trim() === '') {
        alert('Please enter your username.');
        return false;
    }

    if (password.trim() === '') {
        alert('Please enter your password.');
        return false;
    }

    return true;
}

// Function to validate forgot password form
function validateForgotPasswordForm() {
    var username = document.getElementById('username').value;
    var mobileNumber = document.getElementById('mobile_number').value;

    if (username.trim() === '') {
        alert('Please enter your username.');
        return false;
    }

    if (mobileNumber.trim() === '') {
        alert('Please enter your mobile number.');
        return false;
    }

    return true;
}

// Function to validate change password form
function validateChangePasswordForm() {
    var oldPassword = document.getElementById('old_password').value;
    var newPassword = document.getElementById('new_password').value;

    if (oldPassword.trim() === '') {
        alert('Please enter your old password.');
        return false;
    }

    if (newPassword.trim() === '') {
        alert('Please enter a new password.');
        return false;
    }

    return true;
}

// Function to add product to cart
function addToCart(productId) {
    // Implement functionality to add product to cart via AJAX request
    // For example:
    // var xhr = new XMLHttpRequest();
    // xhr.open('POST', '/add-to-cart', true);
    // xhr.setRequestHeader('Content-Type', 'application/json');
    // xhr.onreadystatechange = function() {
    //     if (xhr.readyState === XMLHttpRequest.DONE) {
    //         if (xhr.status === 200) {
    //             alert('Product added to cart successfully.');
    //         } else {
    //             alert('Failed to add product to cart.');
    //         }
    //     }
    // };
    // xhr.send(JSON.stringify({ productId: productId }));
}

// Add more JavaScript functionality as needed
