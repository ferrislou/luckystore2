# Generated by Django 3.2.16 on 2023-02-11 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultiLang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_us', models.CharField(max_length=200, null=True)),
                ('zh_hant', models.CharField(max_length=200, null=True)),
                ('zh_hans', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]