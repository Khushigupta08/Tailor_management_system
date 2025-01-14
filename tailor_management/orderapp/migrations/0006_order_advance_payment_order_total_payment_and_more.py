# Generated by Django 5.0.4 on 2024-07-22 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0005_alter_order_garment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Advance_Payment',
            field=models.CharField(choices=[('Topwear', 'Topwear'), ('Bottomwear', 'Bottomwear'), ('Top-Bottom', 'Top-Bottom')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Total_payment',
            field=models.CharField(choices=[('Topwear', 'Topwear'), ('Bottomwear', 'Bottomwear'), ('Top-Bottom', 'Top-Bottom')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='deliver_date',
            field=models.CharField(choices=[('Topwear', 'Topwear'), ('Bottomwear', 'Bottomwear'), ('Top-Bottom', 'Top-Bottom')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.CharField(choices=[('Topwear', 'Topwear'), ('Bottomwear', 'Bottomwear'), ('Top-Bottom', 'Top-Bottom')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='due_payment',
            field=models.CharField(choices=[('Topwear', 'Topwear'), ('Bottomwear', 'Bottomwear'), ('Top-Bottom', 'Top-Bottom')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.CharField(choices=[('Topwear', 'Topwear'), ('Bottomwear', 'Bottomwear'), ('Top-Bottom', 'Top-Bottom')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='priority',
            field=models.CharField(choices=[('Topwear', 'Topwear'), ('Bottomwear', 'Bottomwear'), ('Top-Bottom', 'Top-Bottom')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.CharField(choices=[('Topwear', 'Topwear'), ('Bottomwear', 'Bottomwear'), ('Top-Bottom', 'Top-Bottom')], max_length=10, null=True),
        ),
    ]
