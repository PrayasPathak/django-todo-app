# Generated by Django 4.2.9 on 2024-01-22 05:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('due_date', models.DateField()),
                ('due_time', models.TimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]