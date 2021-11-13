#!/usr/bin/python3
"""Review Python package"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class declaration"""
    place_id = ""
    user_id = ""
    text = ""
