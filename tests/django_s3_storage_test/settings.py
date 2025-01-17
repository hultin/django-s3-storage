import os
import uuid

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "test"

USE_TZ = True

TIME_ZONE = "UTC"


# S3 settings.

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_REGION = os.environ.get("AWS_REGION", "eu-central-1")

AWS_S3_KEY_PREFIX = uuid.uuid4().hex

DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage"

# Application definition

INSTALLED_APPS = ("django_s3_storage",)


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
