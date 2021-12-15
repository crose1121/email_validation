from flask_app import app
from flask import render_template, redirect, request

from flask_app.models.email import Email 

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/email/create', methods=['POST'])
def create_email():
    data = {
        'email_name': request.form['email_name']
    }
    if Email.validate_email(data):
        Email.create_email(data)
        return redirect('/email/success')
    else:
        return redirect('/')


@app.route('/email/success')
def success():
    all_emails = Email.get_all_emails()
    return render_template('success.html', emails=all_emails)


@app.route('/email/delete/<int:id>')
def delete_email(id):
    data = {
        'id': id
    }
    Email.delete_email(data)
    return redirect('/email/success')
