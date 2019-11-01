import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '6d0&br-^3t$y_(1p%c$q5#q-^b((9mo6_hyups@*s*svw@j*t@'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True