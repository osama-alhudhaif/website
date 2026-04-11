#!/usr/bin/env python
"""
Fixed Django server runner that bypasses Django 6.0.4 pathlib issues.
"""

import os
import sys
import django
from django.conf import settings
from django.core.servers.basehttp import run, get_internal_wsgi_application

def main():
    """Run Django development server without autoreloader to avoid pathlib issues."""
    
    # Set up Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    django.setup()
    
    # Get host and port from command line args
    addrport = '127.0.0.1:8000'
    if len(sys.argv) > 1:
        addrport = sys.argv[1]
    
    print(f"Starting Django server on {addrport} (fixed for Django 6.0.4)")
    
    # Run server without autoreloader
    from django.core.management.commands.runserver import Command as RunserverCommand
    
    # Create a runserver command instance and run it manually
    runserver = RunserverCommand()
    runserver.use_reloader = False  # Disable autoreloader
    runserver.addrport = addrport
    runserver.execute(addrport, use_reloader=False)

if __name__ == '__main__':
    main()
