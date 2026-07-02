from .models import SiteSettings


def get_site_settings() -> SiteSettings:
    obj, _ = SiteSettings.objects.get_or_create(id=1)
    return obj
