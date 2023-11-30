from django.apps import apps

from scheduler_field.models import SchedulerDateManager


def get_model_table_mapping():
    mapping = dict()
    for model in apps.get_models():
        mapping[model._meta.db_table] = model
    return mapping


def run_function_for_date(datetime):
    model_mapping = get_model_table_mapping()
    for row in SchedulerDateManager.objects.all():
        model = model_mapping.get(row.table_name, None)
        if not model:
            raise ValueError('No model found with db_table {}!'.format(row.table_name))
        due_entries = model.objects.filter(**{row.field_name: datetime})
        for i in due_entries:
            getattr(model, row.method_name)(i.pk)
