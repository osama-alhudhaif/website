"""
Fixed runserver command that bypasses Django 6.0.4 pathlib issues.
"""

from django.core.management.base import BaseCommand
from django.core.servers.basehttp import run, get_internal_wsgi_application
from django.conf import settings
import os
import sys


class Command(BaseCommand):
    help = 'Fixed runserver that bypasses Django 6.0.4 pathlib issues'

    def add_arguments(self, parser):
        parser.add_argument(
            'addrport', 
            default='127.0.0.1:8000',
            nargs='?',
            help='Optional port number, or ipaddr:port'
        )
        parser.add_argument(
            '--noreload',
            action='store_false',
            dest='use_reloader',
            help='Tells Django to NOT use the auto-reloader.',
        )

    def handle(self, *args, **options):
        addrport = options['addrport']
        use_reloader = options['use_reloader']
        
        if not addrport:
            addrport = '127.0.0.1:8000'
        
        self.stdout.write(f"Starting fixed Django server on {addrport}")
        
        # Run without autoreloader to avoid pathlib issues
        run(
            addrport,
            get_internal_wsgi_application(),
            use_reloader=False,  # Disable autoreloader
            use_ipv6=False,
            use_threading=True,
            use_debugger=settings.DEBUG,
        )
