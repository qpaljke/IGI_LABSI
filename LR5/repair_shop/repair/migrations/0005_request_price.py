# Generated by Django 5.0.4 on 2024-05-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repair', '0004_alter_request_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]