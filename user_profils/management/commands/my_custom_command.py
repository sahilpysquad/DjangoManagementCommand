from django.core.management.base import BaseCommand
from datetime import datetime


class Command(BaseCommand):

    help = "Showing current time"

    def handle(self, *args, **kwargs):
        current_time = datetime.now().strftime('%X')
        self.stdout.write("Current Time is :- %s" % current_time)
