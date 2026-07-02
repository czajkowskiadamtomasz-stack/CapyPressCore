from django import forms


class DatabaseForm(forms.Form):
    db_name = forms.CharField()
    db_user = forms.CharField()
    db_password = forms.CharField(widget=forms.PasswordInput)
    db_host = forms.CharField(initial="db")


class AdminForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class SiteForm(forms.Form):
    site_name = forms.CharField()
    site_url = forms.URLField()
