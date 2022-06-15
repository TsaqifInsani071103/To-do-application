# Generated by Django 3.2.9 on 2021-12-05 09:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ToDos', '0004_alter_todos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
