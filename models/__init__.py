#!/usr/bin/python3
"""__init__ is amagic method for models"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
