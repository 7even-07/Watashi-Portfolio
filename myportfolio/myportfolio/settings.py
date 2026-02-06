from pathlib import Path
import os
import cloudinary
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ofnqlb-42e3w&ut-yzewl=&a&*9rxif&f3z5g#+p2o=)uap1u#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # keep this false when you wants to use custom page for 404 pages.
# run this only in development mode, cause if you set DEBUG = False then it does not sever static files
# python manage.py runserver --insecure


ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    ".onrender.com",
]


# Application definition
# note your cloudinary applications should be load before myportfolioapp application..
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'myportfolioapp',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myportfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'myportfolioapp.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'myportfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases


if DEBUG:
    # 🔹 Development (Local)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # 🔹 Production (Render / PostgreSQL)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST'),
            'PORT': os.environ.get('DB_PORT', '5432'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    # You can add other directories here if needed
]

# this is important while dealing with static or images
STATIC_ROOT = BASE_DIR / 'staticfiles'

# for media
cloudinary.config(
    cloud_name = os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key = os.environ.get("CLOUDINARY_API_KEY"),
    api_secret = os.environ.get("CLOUDINARY_API_SECRET"),
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = "/"
if DEBUG:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# self created constants
SITE_NAME = "Shreenivas Rupesh Hadgal - Python Developer"
NAVBAR_NAME = "Shreenivas Hadgal"
SITE_EMAIL = "shreenivashadgal2@gmail.com"
NAV_ITEMS = ["Home", "About", "Projects", "Contact"]
ABOUT_ME_TITLE = "Passionate about creating meaningful digital experiences"
ABOUT_ME_DESCRIPTION = """
            I’m a Python Full-Stack Developer with 2+ years of hands-on experience building scalable, production-ready web applications using Django, FastAPI, and Next.js. I enjoy designing efficient backend architectures, optimizing performance with Redis caching, and creating modern, user-friendly interfaces that deliver real value.

            Over the past few years, I’ve worked on a variety of real-world systems including project management platforms, AI-powered chat and voice applications, file management tools, and internal automation solutions used by hundreds of users. My focus is always on writing clean, maintainable code and building solutions that are secure, reliable, and easy to scale.

            I’m passionate about turning ideas into functional products and continuously improving my skills to build better, faster, and smarter web applications.
"""
SKILLS = ["Django", "FastAPI", "PHP", "SQL", "NextJS", "LLM", "Redis", "RabbitMQ", "Linux & Shell Scripting", "C++", "HTML", "CSS", "JS"]
CONTACT_NUMBER = "9370855778"
EMAIL_ADDRESS = "shreenivashadgal2@gmail.com"