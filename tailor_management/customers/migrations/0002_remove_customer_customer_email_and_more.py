# Generated by Django 4.2.15 on 2024-08-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_email',
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_address',
            field=models.TextField(max_length=100, null=True),
        ),
    ]