# Generated by Django 4.2.2 on 2023-07-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-03-12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
