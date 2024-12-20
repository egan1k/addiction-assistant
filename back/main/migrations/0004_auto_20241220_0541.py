# Generated by Django 3.2.12 on 2024-12-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_locked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='last_failed_login_attempt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='locked_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='login_attempts_left',
            field=models.PositiveSmallIntegerField(blank=True, default=5, null=True),
        ),
    ]
