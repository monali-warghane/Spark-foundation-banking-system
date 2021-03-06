# Generated by Django 3.2.6 on 2021-10-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparksapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('transfer_to', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
