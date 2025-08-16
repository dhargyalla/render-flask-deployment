from flask_bootstrap import Bootstrap4
from flask import Flask, render_template,request, redirect, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()  # Ensure this is called early in the script
app = Flask(__name__)

# Configure Flask-Mail using environment variables
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
app.config['MAIL_RECIPIENT'] = os.getenv('MAIL_RECIPIENT')
app.config['MAIL_RECIPIENT'] = os.getenv('MAIL_RECIPIENT')


mail = Mail(app)
bootstrap = Bootstrap4(app)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')

@app.route("/portfolio", methods=['GET'])
def portfolio():
    return render_template('portfolio.html')

@app.route("/project1", methods=['GET'])
def project1():
    return render_template('project1.html')

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(
            subject=f"Contact Form Submission from {name}",
            recipients=[os.getenv('MAIL_RECIPIENT')],  # Use value from .env file
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
        mail.send(msg)

        flash('Your message has been sent successfully!', 'success')
        return redirect('/contact')

    return render_template('contact.html')

if __name__ == "__main__":
    app.secret_key = 'your_secret_key'  # Required for flash messages
    app.run(debug=True)