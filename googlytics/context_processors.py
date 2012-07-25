from django.conf import settings
from django.template.loader import render_to_string


def googlytics(request):
    """Return google analytics code."""
    context = {'googlytics_code': ''}

    ignore = (getattr(settings, 'GOOGLE_ANALYTICS_IGNORE_ADMIN', False)
              and request.user.is_authenticated()
              and request.user.is_staff)

    if not ignore and settings.GOOGLE_ANALYTICS_KEY:
        snippet = render_to_string('googlytics/googlytics.html',
                                   {'google_analytics_key':
                                    settings.GOOGLE_ANALYTICS_KEY})
        context['googlytics_code'] = snippet

    return context
