"""
Settings for DRF OpenAPI.
To override the default values simply define them in your project's
'settings.py' file.

"""
from django.conf import settings

# Permission decorator for the API docs view
DOC_SCHEMA_PERMISSION_DECORATOR = getattr(settings, 'DOC_SCHEMA_PERMISSION_DECORATOR',
                                                  'django.contrib.admin.views.decorators.staff_member_required')
