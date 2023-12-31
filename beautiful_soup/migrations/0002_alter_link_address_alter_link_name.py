# Generated by Django 4.2.6 on 2023-10-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautiful_soup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='address',
            field=models.URLField(blank=True, default='Missing address', null=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(blank=True, default='Missing name', max_length=100, null=True),
        ),
    ]
