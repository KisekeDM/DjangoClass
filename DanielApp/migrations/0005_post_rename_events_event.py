# Generated by Django 4.2 on 2023-04-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DanielApp', '0004_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=50)),
                ('Text', models.CharField(max_length=50)),
                ('Createddate', models.DateField(null=True)),
                ('Publisheddate', models.DateField(null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
    ]