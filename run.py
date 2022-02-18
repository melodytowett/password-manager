#!/usr/bin/env python3.9
from cmath import pi
from user import User
def creat_user(fname,lname,pid,email): 
    new_user = User(fname,lname,pid,email)
    return new_user

def save_users(user):
    user.save_uset()
