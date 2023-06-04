# Generated by Django 4.1.7 on 2023-06-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=20)),
                ('definition', models.TextField(max_length=200)),
                ('category', models.CharField(max_length=20)),
                ('complexity', models.IntegerField()),
            ],
        ),
    ]