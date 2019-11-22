# Generated by Django 2.0.1 on 2018-12-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181025_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='template_id',
        ),
    ]
