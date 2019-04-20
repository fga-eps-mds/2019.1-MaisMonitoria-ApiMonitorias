rm -rf .coverage
coverage run --source='.' --omit=*/tests/*,*/tests.py,*/migrations/*,*/urls.py,*/settings.py,*/wsgi.py,manage.py manage.py test
coverage report || true