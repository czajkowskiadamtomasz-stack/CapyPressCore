from django.core.management import call_command
from django.contrib.auth import get_user_model
from apps.core.models import SiteSettings
import os


User = get_user_model()


class InstallerService:

    def run_migrations(self):
        call_command("migrate")

    def create_admin(self, username, email, password):
        return User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

    def save_site_settings(self, data):
        obj, _ = SiteSettings.objects.get_or_create(id=1)
        obj.site_name = data["site_name"]
        obj.site_url = data["site_url"]
        obj.save()

    def write_env(self, data):
        env_path = ".env"

        content = f"""
DEBUG=0
SECRET_KEY=generated-secret
DB_NAME={data['db_name']}
DB_USER={data['db_user']}
DB_PASSWORD={data['db_password']}
DB_HOST={data['db_host']}
"""

        with open(env_path, "w") as f:
            f.write(content)

    def create_restart_trigger(self):
        path = "/app/shared/.restart_trigger"
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w") as f:
            f.write("restart")
