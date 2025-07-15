1. Generate new secret key
```python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"```

2. For runserver:
``` poetry run python manage.py runserver --settings=config.settings.dev ```