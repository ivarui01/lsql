# Generated by Django 3.0.7 on 2020-06-17 18:00

from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_md', models.CharField(max_length=100, validators=[django.core.validators.MaxLengthValidator(1)])),
                ('name_html', models.CharField(max_length=200, validators=[django.core.validators.MaxLengthValidator(1)])),
                ('position', models.PositiveIntegerField()),
                ('description_md', models.CharField(max_length=5000, validators=[django.core.validators.MaxLengthValidator(1)])),
                ('description_html', models.CharField(max_length=10000, validators=[django.core.validators.MaxLengthValidator(1)])),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_md', models.CharField(max_length=100)),
                ('title_html', models.CharField(max_length=200, null=True)),
                ('text_md', models.CharField(max_length=5000)),
                ('text_html', models.CharField(max_length=10000, null=True)),
                ('create_sql', models.CharField(max_length=20000)),
                ('insert_sql', models.CharField(max_length=20000)),
                ('initial_db', django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('min_stmt', models.PositiveIntegerField()),
                ('max_stmt', models.PositiveIntegerField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('position', models.PositiveIntegerField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='DMLProblem',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='judge.Problem')),
                ('check_order', models.BooleanField(default=False)),
                ('solution', models.CharField(max_length=5000, validators=[django.core.validators.MaxLengthValidator(1)])),
                ('expected_result', django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
            ],
            bases=('judge.problem',),
        ),
        migrations.CreateModel(
            name='FunctionProblem',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='judge.Problem')),
                ('check_order', models.BooleanField(default=False)),
                ('solution', models.CharField(max_length=5000, validators=[django.core.validators.MaxLengthValidator(1)])),
                ('proc_call', models.CharField(max_length=1000, validators=[django.core.validators.MaxLengthValidator(1)])),
                ('expected_result', django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
            ],
            bases=('judge.problem',),
        ),
        migrations.CreateModel(
            name='SelectProblem',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='judge.Problem')),
                ('check_order', models.BooleanField(default=False)),
                ('solution', models.CharField(max_length=5000, validators=[django.core.validators.MaxLengthValidator(1)])),
                ('expected_result', django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
            ],
            bases=('judge.problem',),
        ),
        migrations.CreateModel(
            name='TriggerProblem',
            fields=[
                ('problem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='judge.Problem')),
                ('check_order', models.BooleanField(default=False)),
                ('solution', models.CharField(max_length=5000, validators=[django.core.validators.MaxLengthValidator(1)])),
                ('tests', models.CharField(max_length=1000, validators=[django.core.validators.MaxLengthValidator(1)])),
                ('expected_result', django.contrib.postgres.fields.jsonb.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
            ],
            bases=('judge.problem',),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(max_length=5000, validators=[django.core.validators.MaxLengthValidator(1)])),
                ('veredict_code', models.PositiveSmallIntegerField()),
                ('veredict_message', models.CharField(max_length=5000, null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='judge.Problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
