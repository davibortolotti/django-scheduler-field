from django.db import models


class SchedulerDateManager(models.Model):
    table_name = models.CharField(max_length=100)
    method_name = models.CharField(max_length=50)
    field_name = models.CharField(max_length=50)
