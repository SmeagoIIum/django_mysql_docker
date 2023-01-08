import django_tables2 as tables
from user.models import User


class UserTable(tables.Table):
    class Meta:
        model = User
        template_name = "django_tables2/bootstrap.html"
        fields = ("first_name", "last_name", "description", "birth_date")
