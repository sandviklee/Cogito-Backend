# Generated by Django 5.0.1 on 2025-01-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0010_alter_memberapplication_lead'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberapplication',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='memberapplication',
            name='lead',
            field=models.BooleanField(blank=True, default=False, help_text='Whether the applicant wants to be a project lead', null=True),
        ),
    ]
