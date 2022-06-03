"""
WSGI config for blog_liis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_liis.settings')

application = get_wsgi_application()




import os
import sys

## assuming your django settings file is at '/home/whaleofthesimon/mysite/mysite/settings.py'
## and your manage.py is is at '/home/whaleofthesimon/mysite/manage.py'
#path = '/home/whaleofthesimon/mysite'
#if path not in sys.path:
#    sys.path.append(path)
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
## then:
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()