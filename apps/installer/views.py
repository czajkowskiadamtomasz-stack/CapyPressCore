from django.views import View
from django.shortcuts import render, redirect
from .forms import DatabaseForm, AdminForm, SiteForm
from .services import InstallerService


class InstallerView(View):
    service = InstallerService()

    def get(self, request):
        step = request.GET.get("step", "db")

        forms = {
            "db": DatabaseForm(),
            "admin": AdminForm(),
            "site": SiteForm(),
        }

        return render(request, "installer.html", {
            "step": step,
            "form": forms.get(step),
        })

    def post(self, request):
        step = request.POST.get("step")

        if step == "db":
            form = DatabaseForm(request.POST)
            if form.is_valid():
                self.service.write_env(form.cleaned_data)
                return redirect("/installer/?step=admin")

        if step == "admin":
            form = AdminForm(request.POST)
            if form.is_valid():
                self.service.create_admin(**form.cleaned_data)
                return redirect("/installer/?step=site")

        if step == "site":
            form = SiteForm(request.POST)
            if form.is_valid():
                self.service.save_site_settings(form.cleaned_data)
                self.service.run_migrations()
                self.service.create_restart_trigger()

                return redirect("/")

        return redirect("/installer/")
