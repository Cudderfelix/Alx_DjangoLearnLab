DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'intro_db',
        'USER': 'alx_client',
        'PASSWORD': 'alx_pass',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
Installed_APPS = [
    ...
    'subscribers',
]