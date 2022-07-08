# Generated by Django 4.0.6 on 2022-07-08 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_response_candidate_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='candidate_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.candidate'),
            preserve_default=False,
        ),
    ]