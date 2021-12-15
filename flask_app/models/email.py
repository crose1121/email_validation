from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use below   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
DB = "email_validation_db"

class Email:
    def __init__(self,data):
        self.email_name = data['email_name']

    @classmethod
    def create_email(cls,data):
        query = "INSERT INTO emails (email_name) VALUES (%(email_name)s);"
        result = connectToMySQL(DB).query_db(query,data)
        return result

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM emails"
        result = connectToMySQL(DB).query_db(query)
        return result

    @classmethod
    def delete_email(cls,data):

        query = "DELETE FROM emails WHERE emails.id = %(id)s"
        connectToMySQL(DB).query_db(query,data)



    @staticmethod
    def validate_email(data):
        is_valid = True
        query = "SELECT * FROM emails WHERE emails.email_name = %(email_name)s;"
        result = connectToMySQL(DB).query_db(query,data)

        if not EMAIL_REGEX.match(data['email_name']):
            is_valid = False
            flash("Please enter a valid email")

        if len(result) > 0:
            is_valid = False
            flash("Email taken")
            
        return is_valid
