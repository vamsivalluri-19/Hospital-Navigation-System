from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Flask app initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # SQLite database
app.config['SECRET_KEY'] = 'your_secret_key'

# Database initialization
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check database for the user
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard', username=username))
        else:
            flash('Invalid username or password!', 'error')
    return render_template('login.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'error')
        else:
            # Add user to the database
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

# Dashboard route
@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username)

# Initialize database
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
