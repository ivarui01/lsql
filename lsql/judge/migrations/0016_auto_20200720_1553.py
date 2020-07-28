# Generated by Django 3.0.7 on 2020-07-20 13:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0015_auto_20200720_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmlproblem',
            name='solution',
            field=models.TextField(max_length=5000, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='functionproblem',
            name='calls',
            field=models.TextField(default='', max_length=5000, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='functionproblem',
            name='solution',
            field=models.TextField(max_length=5000, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='procproblem',
            name='proc_call',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='procproblem',
            name='solution',
            field=models.TextField(max_length=5000, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='triggerproblem',
            name='tests',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]