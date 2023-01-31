# radioco.frapp
RadioCo extension for Freie Radios App

## Hacking

### Setup dev environment

```
python -m venv .
./bin/python setup.py develop
```

### Run test suite
DJANGO_SETTINGS_MODULE="radioco.frapp.test.settings" ./bin/django-admin test
