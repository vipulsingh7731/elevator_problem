# Generated by Django 4.1.9 on 2023-06-05 10:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("elevators", "0002_alter_elevator_id_alter_elevatorrequest_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="elevator",
            old_name="oprational",
            new_name="operational",
        ),
    ]