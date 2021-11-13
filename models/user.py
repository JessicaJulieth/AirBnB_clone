#!/usr/bin/python3
""" Heredar de base model"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class representing User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
