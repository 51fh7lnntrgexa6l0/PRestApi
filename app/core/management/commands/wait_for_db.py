import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand

class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **kwargs):
        self.stdout.write('Waiting for db connections')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError as E:
                self.stdout.write('Database NA, waiting 1 second..')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('DB Available!'))
