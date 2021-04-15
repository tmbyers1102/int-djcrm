from django.core.management.base import BaseCommand

# this is how you can create custom commands to run along with the runserver.
# you can use this to create a lead in the system, or audit, clean the database or cron jobs
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str)

    def handle(self, *args, **options):
        print('hello, ' + options['first_name'])