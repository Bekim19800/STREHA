INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.staticfiles',
    ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # 👈 allows any frontend to connect

ALLOWED_HOSTS = ['your-backend-name.onrender.com']
ROOT_URLCONF = 'streha_api.urls'
