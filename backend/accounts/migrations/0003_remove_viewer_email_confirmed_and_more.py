# Generated by Django 4.0.6 on 2022-08-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_viewer_email_confirmed_alter_viewer_about_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewer',
            name='email_confirmed',
        ),
        migrations.AlterField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=False, help_text="Determine if the User's email has been verified.", verbose_name='email verified?'),
        ),
    ]
