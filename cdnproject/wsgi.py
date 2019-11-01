"""
WSGI config for cdnproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
#from django.core.wsgi import get_wsgi_application

# Djangoプロジェクトへのパスを通す(不要な可能性あり)
#sys.path.append("/Users/okano/Documents/03_dev/GitHub/cdnproject")
#sys.path.append("/Users/okano/Documents/03_dev/GitHub/cdnproject/cdnproject")

# Djangoの環境設定ファイル(settings.py)を指定
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cdnproject.settings')

application = get_wsgi_application()