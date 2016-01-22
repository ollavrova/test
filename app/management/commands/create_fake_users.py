from optparse import make_option
from django.contrib.auth.models import User
from django.utils import timezone
import requests
from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'create a fake users number N'
    option_list = BaseCommand.option_list + (
        make_option(
            "-n",
            "--number",
            dest="number",
            help="specify number of users",
            metavar="NUM"
        ),
    )

    def handle(self, *args, **options):
        if options['number'] == None :
                raise CommandError("Option `--number=...` must be specified.")
        n = options['number']
        r = requests.get('https://randomuser.me/api/?results='+n)
        r.raise_for_status()
        if r.status_code != 200:
            self.stderr.write('Error! Wrong response on request: status_code='+r.status_code)
            r.raise_for_status()
        users = r.json()['results']
        for user in users:
            User.objects.create_user(
                username=user['user']['username'],
                first_name=user['user']['name']['first'],
                last_name=user['user']['name']['last'],
                email=user['user']['email'],
                password=user['user']['password'],
                date_joined=timezone.now()
            )
        self.stdout.write('Created '+n+' users.')
