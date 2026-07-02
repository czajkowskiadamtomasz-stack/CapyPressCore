from django.shortcuts import redirect
from apps.core.selectors import get_site_settings


class InstallerMiddleware:
    """
    Redirect to installer if system is not initialized.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/installer"):
            return self.get_response(request)

        try:
            settings = get_site_settings()
            if not settings:
                return redirect("/installer/")
        except Exception:
            return redirect("/installer/")

        return self.get_response(request)
