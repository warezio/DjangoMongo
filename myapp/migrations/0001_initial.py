# Generated by Django 2.1.5 on 2020-01-21 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mydb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=50)),
                ('default', models.CharField(default='', max_length=255)),
                ('value', models.CharField(default='', max_length=255, null=True)),
            ],
        ),
    ]