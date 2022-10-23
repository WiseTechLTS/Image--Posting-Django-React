# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wr252ttaseafwetrwtqysadfwrg+2rim1nu!2edr=bp0i^*he(t2!7ul_c356@zh=)(pcii&&((sw'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'artwork_application_database',
        'USER': 'root',
        'PASSWORD': 'Root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
