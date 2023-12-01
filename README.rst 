# Django-scheduler-field

This django plugin is meant to help the developer to quickly add a DateField to a model
and have it schedule a function run to that date.

You just need a django project, a django model and to write a method for that model to execute in the field's value.

## Compatibility

This project has been tested with Django 4.2 and Python 3.9 only, but should work okay in other versions too.

## Installing

This project is not yet on PyPI, so for now, one can install using the tarball in this github repos, using

`pip install git+https://github.com/davibortolotti/django-scheduler-field.git@v0.1.0`

## Getting started

After setting up your django app and installing djanco-scheduler-field, you should add it to your `INSTALLED_APPS` as `scheduler_field`.

### Run migrations

Django-scheduler-field has its own migrations, so before anything, one should run `python manage.py migrate` in the django project it is installed.

### Add it to a model

You can add the field to any model and it will behave as a DateField (it extends django.db.models.DateField), accepting any of its arguments.
The only thing you need to do differently is pass a model's static method name as string for the scheduler to run. E.g.

```
from django.db import models
from scheduler_field.fields import SchedulerDateField

class TestModel(models.Model):
    name = models.CharField(max_=20)
    reminder_date = SchedulerDateField(method_name='send_reminder_email')

    @static_method
    def send_reminder_email(_id):
        test = TestModel.objects.get(pk=_id)
        email_function(f"Hello {test.name}")
```

### Add the manager function to a job scheduler

Django-scheduler-field will automatically pick up the registered fields, models and methods it needs from the previous step as the app starts up,
and makes available a manager function for you to add to your scheduler of choice. For instance, using celery, one can do:

```
from scheduler_field.commands import run_function_for_date

@app.task(bind=True, ignore_result=True)
def run_scheduled_tasks(self):
    print("running task")
    run_function_for_date(now())
`` 

This will run the `send_reminder_email` method for every row that resolves `reminder_date == now`

## Thanks

This is not production ready and should be used lightly. Feel free to contribute if you like the project, or email me for any suggestions: davibortolotti@gmail.com


