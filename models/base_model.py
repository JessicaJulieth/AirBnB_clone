#!/usr/bin/python3
"""base_Model program"""

import uuid
import datetime
import cmd

class BaseModel:
    """BaseModel that defines all common attributes/methods for other classes"""

    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        