from django.core.management.base import BaseCommand
from csv import DictReader
from leads.models import Lead, UserProfile

# this is how you can create custom commands to run along with the runserver.
# you can use this to create a lead in the system, or audit, clean the database or cron jobs
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)
        # we need to make sure the created leads have an org though the csv does not specify
        parser.add_argument('organisor_email', type=str)

    # this goes into the file and figures out what all the items are
    def handle(self, *args, **options):
        file_name = options['file_name']
        organisor_email = options['organisor_email']

        organisation = UserProfile.objects.get(user__email=organisor_email)

        with open(file_name, 'r') as read_obj:
            csv_reader = DictReader(read_obj)
            for row in csv_reader:
                first_name = row['first_name']
                last_name = row['last_name']
                age = row['age']
                email = row['email']


                # this actually creates the lead
                Lead.objects.create(
                    organisation=organisation,
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    email=email,
                )
