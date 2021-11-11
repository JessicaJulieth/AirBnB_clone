#!/usr/bin/python3
"""unique FileStorage instance for your application"""

import models.engine.file_storage

storage = models.engine.file_storage.FileStorage()
models.engine.file_storage.reload(storage)
