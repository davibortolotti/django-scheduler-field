from django.db import models

from scheduler_field.models import SchedulerDateManager


class SchedulerDateField(models.DateField):
    def __init__(self, method_name='', *args, **kwargs):
        if not method_name:
            raise ValueError("One must define method_name for a SchedulerDateTimeField")
        self.method_name = method_name
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["method_name"] = self.method_name
        return name, path, args, kwargs

    def contribute_to_class(self, cls, name, private_only=False):
        SchedulerDateManager.objects.get_or_create(table_name=cls._meta.db_table, method_name=self.method_name, field_name=name)
        super().contribute_to_class(cls, name, private_only=private_only)
