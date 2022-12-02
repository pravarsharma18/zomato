# Generated by Django 4.1.3 on 2022-12-02 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_address_alter_user_gst_number_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Buyers',
        ),
        migrations.DeleteModel(
            name='Vendors',
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
    ]