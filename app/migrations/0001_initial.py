# Generated by Django 3.2.5 on 2021-07-08 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RandomNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number1', models.IntegerField()),
                ('number2', models.IntegerField()),
                ('number3', models.IntegerField()),
                ('number4', models.IntegerField()),
                ('number5', models.IntegerField()),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
    ]
