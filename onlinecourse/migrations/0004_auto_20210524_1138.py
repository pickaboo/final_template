# Generated by Django 3.1.3 on 2021-05-24 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20210521_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_grade_mark',
            new_name='grade',
        ),
    ]
