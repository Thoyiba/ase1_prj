# Generated by Django 2.1.2 on 2018-11-04 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_auto_20181101_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='catagory',
        ),
        migrations.AddField(
            model_name='question',
            name='catagory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='questions.Catagory', verbose_name='Catagories'),
        ),
    ]
