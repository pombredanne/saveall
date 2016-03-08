from django.core.management.base import BaseCommand, CommandError


class SaveAll(BaseCommand):
    args = '<model_name model_name ...>'
    help = 'Gets all model instances and saves it.'

    def handle(self, *args, **options):
        for model in args:
            try:
                foo = model.objects.all()
            except model.DoesNotExist:
                raise CommandError('Model %s does not exist.' % model)

            foo.save()

            self.stdout.write('Successfully saved "%s" instances.' % model)

        self.stdout.write('All instances saved.')
