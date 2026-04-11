"""
Custom storage class to fix Django 6.0.4 pathlib compatibility issues.
"""

from django.core.files.storage import StaticFilesStorage
from django.core.files.utils import validate_file_name
from pathlib import PurePosixPath


class Django6CompatibleStaticFilesStorage(StaticFilesStorage):
    """
    Custom storage class that handles Django 6.0.4 pathlib compatibility issues.
    Fixes the 'PurePosixPath' object has no attribute 'is_absolute' error.
    """
    
    def save(self, name, content, max_length=None):
        """
        Override save method to handle pathlib objects properly.
        """
        # Convert PurePosixPath to string before validation
        if isinstance(name, PurePosixPath):
            name = str(name)
        
        # Call the parent save method
        return super().save(name, content, max_length)


# Monkey patch validate_file_name to handle pathlib objects
original_validate_file_name = validate_file_name

def patched_validate_file_name(name, allow_relative=False):
    """
    Patched version of validate_file_name that handles pathlib objects.
    """
    # Convert pathlib objects to string
    if hasattr(name, 'as_posix'):
        name = str(name)
    elif isinstance(name, PurePosixPath):
        name = str(name)
    
    return original_validate_file_name(name, allow_relative)

# Apply the monkey patch
import django.core.files.utils
django.core.files.utils.validate_file_name = patched_validate_file_name
