# Generated by Django 3.2.6 on 2021-08-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cds', '0002_auto_20210816_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cds',
            name='caption',
        ),
        migrations.AddField(
            model_name='cds',
            name='result',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='cds',
            name='image',
            field=models.ImageField(blank=True, upload_to='Post'),
        ),
    ]