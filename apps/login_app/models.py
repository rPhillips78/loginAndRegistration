from __future__ import unicode_literals
from django.db import models

class Validator(models.Manager):
    def register_func(self, data):
        errors = {}

        # Naming validation
        if not data['first_name']:
            errors['first_name'] = "First name is a required field"
        elif len(data['first_name']) < 2:
            errors['first_name'] = "Expecting at least 2 letters for first name."
        if not data['last_name']:
            errors['last_name'] = "Last name is a required field"
        elif len(data['last_name']) < 2:
            errors['last_name'] = "Expecting at least 2 letters for last name."

        # password validation
        if not data['password']:
            errors['password'] = "Password is a required field."
        elif len(data['password']) < 8:
            errors['password'] = "Password should be at least 8 characters."
        if not data['password_confirm']:
            errors['password_confirm'] = "Confirm Password is a required field."
        elif data['password'] != data['password_confirm']:
            errors['password_confirm'] = "Confirmation must match password exactly"

        if data['password'] != data['password_confirm']:
            errors['password'] = "Password does not match!"

        return errors

    
    def login_func(self, data):
        errors = {}

        #login field input validation
        if not data['user_email']:
            errors['user_email'] = "Email is a required field"
        if not data['user_password']:
            errors['user_password'] = "Password is a required field"

        return errors

        
        


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_pw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validator()


