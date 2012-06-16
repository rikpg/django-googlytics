from django.conf import settings
from django.template.loader import render_to_string

def googlytics(request):
    """Return google analytics code."""
    if settings.GOOGLE_ANALYTICS_KEY:
        code = render_to_string('googlytics/googlytics.html',
                                {'google_analytics_key':
                                 settings.GOOGLE_ANALYTICS_KEY})
    else:
        code = ''

    return {'googlytics_code': code}
