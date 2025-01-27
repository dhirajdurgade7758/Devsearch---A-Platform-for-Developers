# Generated by Django 5.1 on 2024-12-20 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_projects_options'),
        ('users', '0005_alter_message_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
