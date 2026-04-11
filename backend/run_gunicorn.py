#!/usr/bin/env python
"""
Simple WSGI server runner that bypasses Django 6.0.4 pathlib issues.
"""

import os
import sys
import django
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

def main():
    """Run Django using simple WSGI server to avoid autoreloader issues."""
    
    # Set up Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    django.setup()
    
    # Get host and port from command line args
    host = '127.0.0.1'
    port = 8000
    
    if len(sys.argv) > 1:
        addrport = sys.argv[1]
        if ':' in addrport:
            host, port = addrport.split(':')
            port = int(port)
        else:
            port = int(addrport)
    
    print(f"Starting Django WSGI server on {host}:{port} (bypassing Django 6.0.4 pathlib issues)")
    
    # Get WSGI application
    application = get_wsgi_application()
    
    # Create and run server
    with make_server(host, port, application) as httpd:
        print(f"Server running at http://{host}:{port}/")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == '__main__':
    main()
