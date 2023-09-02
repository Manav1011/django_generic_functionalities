# Generated by Django 4.2.4 on 2023-09-01 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUser', '0006_customuser_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backupcodes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
