from django.core.management.base import BaseCommand

from apps.accounts.models import User


class Command(BaseCommand):
    """
    Create superuser with email 'admin@admin.admin' and password 'admin'.

    python3 manage.py create_superuser
    """

    help = "Create superuser with email 'admin@admin.com' and password 'string'."

    def handle(self, *args, **options):
        superuser = User.objects.filter(is_superuser=True, email="admin@admin.com").first()
        if superuser:
            superuser.set_password("string")
            superuser.save()
            self.stdout.write(self.style.SUCCESS("Superuser already exists."))
            return
        else:
            superuser = User.objects.create(
                email="admin@admin.com", first_name="admin", last_name="admin", is_superuser=True, is_staff=True
            )

            superuser.set_password("string")
            superuser.save()

            self.stdout.write(self.style.SUCCESS("Superuser successfully created."))
