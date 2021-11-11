#!/usr/bin/python3
"""unique FileStorage instance for your application"""

import file_storage

storage = file_storage.FileStorage()
file_storage.reload(storage)
