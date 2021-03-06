# Generated by Django 3.0.7 on 2020-06-17 19:22

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0005_auto_20200617_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='initial_db',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AlterField(
            model_name='selectproblem',
            name='expected_result',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
    ]
