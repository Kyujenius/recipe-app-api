"""
Django Command to wait for database to be available
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django Command to wait for database to be available"""

    def handle(self, *args, **options):
        pass