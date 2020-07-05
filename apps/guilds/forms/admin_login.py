from django.contrib.auth.forms import AuthenticationForm


class HeventUserAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass