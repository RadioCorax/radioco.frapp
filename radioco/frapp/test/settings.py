INSTALLED_APPS = (
    'solo',
    'radioco.frapp',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    },
]

ROOT_URLCONF = 'radioco.frapp.test.urls'

SECRET_KEY = 'xxx'
