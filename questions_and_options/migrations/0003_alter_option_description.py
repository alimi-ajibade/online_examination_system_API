# Generated by Django 4.0.6 on 2022-07-07 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_and_options', '0002_rename_options_option_rename_questions_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]