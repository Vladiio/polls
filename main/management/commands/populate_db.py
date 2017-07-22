from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates sample questions in database"

    def handle(self, *args, **options):
        q = Question(name="How old are you?")
        q.save()
        for a in ('15 years', '20 years', '25 years'):
            new = Answer(content=a, question=q)
            new.save()
        else:
            self.stdout.write(self.style.SUCCESS("Done!"))

    def add_argumets(self, parser):
        parser.add_argumet("max_count", type=int)
