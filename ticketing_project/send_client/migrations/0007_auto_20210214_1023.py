# Generated by Django 3.1.4 on 2021-02-14 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('send_client', '0006_auto_20210214_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]