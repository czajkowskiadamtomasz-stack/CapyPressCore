from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, default="CapyPress")
    site_url = models.CharField(max_length=255, default="http://localhost")

    maintenance_mode = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
