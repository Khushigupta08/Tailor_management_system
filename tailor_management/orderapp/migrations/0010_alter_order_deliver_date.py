# Generated by Django 5.0.4 on 2024-07-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0009_order_remark_shirt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deliver_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
