from django.conf import settings


def main(request):
    protocol = 'https://' if request.is_secure() else 'http://'
    domain = settings.DOMAIN if settings.DOMAIN != 'localhost' else settings.DOMAIN + ':8000'
    data = {
        'site_name': settings.SITE_NAME,
        'domain': protocol + domain,
    }
    return data
