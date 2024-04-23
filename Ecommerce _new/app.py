from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample product data (replace with actual data from the database)
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.99, 'description': 'Description of Product 1', 'image': 'https://example.com/product1.jpg'},
    {'id': 2, 'name': 'Product 2', 'price': 19.99, 'description': 'Description of Product 2', 'image': 'https://example.com/product2.jpg'},
    # Add more products here...
]

# Sample user data (replace with actual data from the database)
users = {
    'existing_username': {
        'password_hash': generate_password_hash('password')
    }
}

# Root URL
@app.route('/')
def index():
    return render_template('index.html')

# Registration Module
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        # Check if username already exists
        if username in users:
            flash('Username already exists. Please choose a different one.', 'error')
        else:
            # Store user data
            users[username] = {'password_hash': generate_password_hash(password)}
            flash('Registration successful. Please login.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

# Login Module
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']
        # Authenticate user
        if username in users and check_password_hash(users[username]['password_hash'], password):
            session['username'] = username
            flash('Login successful.', 'success')
            return redirect(url_for('catalog'))
        else:
            flash('Invalid username or password.', 'error')
    return render_template('login.html')

# Logout Module
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

# Forgot Password
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        # Check if username exists
        if username in users:
            # Generate OTP (replace with actual OTP generation mechanism)
            otp = str(randint(1000, 9999))
            # Send OTP via email or SMS (replace with actual sending mechanism)
            flash(f'OTP sent to {username}.', 'success')
            session['forgot_password_user'] = username
            session['otp'] = otp
            return redirect(url_for('verify_otp'))
        else:
            flash('Username not found.', 'error')
    return render_template('forgot_password.html')

# Verify OTP
@app.route('/verify_otp', methods=['GET', 'POST'])
def verify_otp():
    if 'forgot_password_user' in session:
        if request.method == 'POST':
            otp = request.form['otp']
            if otp == session['otp']:
                return redirect(url_for('change_password'))
            else:
                flash('Invalid OTP. Please try again.', 'error')
        return render_template('verify_otp.html')
    else:
        flash('You need to initiate the forgot password process.', 'error')
        return redirect(url_for('forgot_password'))

# Change Password
@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if 'forgot_password_user' in session:
        if request.method == 'POST':
            new_password = request.form['new_password']
            users[session['forgot_password_user']]['password_hash'] = generate_password_hash(new_password)
            session.pop('forgot_password_user')
            session.pop('otp')
            flash('Password changed successfully. Please login with your new password.', 'success')
            return redirect(url_for('login'))
        return render_template('change_password.html')
    else:
        flash('You need to initiate the forgot password process.', 'error')
        return redirect(url_for('forgot_password'))

# Product Catalog
@app.route('/catalog')
def catalog():
    return render_template('catalog.html', products=products)

# Add to Cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'username' not in session:
        flash('Please login to add items to your cart.', 'error')
        return redirect(url_for('login'))
    # Get product ID from form data
    product_id = int(request.form['product_id'])
    # Add product to cart (replace with actual cart functionality)
    flash('Product added')
