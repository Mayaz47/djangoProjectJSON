# Generated by Django 4.2.9 on 2024-01-09 08:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Projint', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mydata',
            old_name='name',
            new_name='trade_code',
        ),
        migrations.RenameField(
            model_name='mydata',
            old_name='age',
            new_name='volume',
        ),
        migrations.AddField(
            model_name='mydata',
            name='close',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='mydata',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='mydata',
            name='high',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='mydata',
            name='low',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='mydata',
            name='open',
            field=models.FloatField(default=0),
        ),
    ]
