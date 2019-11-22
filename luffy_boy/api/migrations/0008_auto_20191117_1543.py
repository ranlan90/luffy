# Generated by Django 2.1.4 on 2019-11-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20191116_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='memo',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uid',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
