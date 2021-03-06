# Generated by Django 2.0.1 on 2018-12-19 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20181213_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name_plural': '课程类',
                'verbose_name': '课程类',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='course_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CourseCategory'),
        ),
    ]
