# Generated by Django 4.1.6 on 2023-02-19 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0005_alter_skill_options_alter_vacancy_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
