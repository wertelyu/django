import os


def get_var(var_name: str) -> str:
    var = os.environ.get(var_name)
    return var


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "railway",
        "USER": "postgres",
        "PASSWORD": f"{os.environ.get('SECRET_DJANGO_KEY')}",
        "HOST": "containers-us-west-104.railway.app",
        "PORT": "6452",
    }
}


if __name__ == "__main__":
    print(get_var("SECRET_DJANGO_KEY"))
    print(DATABASES["default"]["PASSWORD"])
