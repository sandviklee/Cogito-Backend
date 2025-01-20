# Generated by Django 5.0.1 on 2025-01-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_membercategory_alter_member_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberapplication',
            name='projects_to_join',
            field=models.JSONField(blank=True, default=list, help_text='List of projects the applicant wants to join, in order of preference'),
        ),
    ]