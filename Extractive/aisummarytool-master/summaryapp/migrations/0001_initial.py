

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.CharField(max_length=1000)),
                ('device_type', models.CharField(max_length=360)),
                ('device_maker', models.CharField(max_length=360)),
                ('device_type_stemmed', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=360), blank=True, size=None)),
                ('device_maker_stemmed', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=360), blank=True, size=None)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.CharField(max_length=1000)),
                ('disease_type', models.CharField(max_length=50)),
                ('stemmed', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=360), blank=True, size=None)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.CharField(max_length=1000)),
                ('patient_group', models.CharField(max_length=50)),
                ('stemmed', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=360), blank=True, size=None)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcedureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.CharField(max_length=1000)),
                ('procedure_type', models.CharField(max_length=50)),
                ('stemmed', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=360), blank=True, size=None)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.CharField(max_length=1000)),
                ('type_of_study', models.CharField(max_length=500)),
                ('stemmed', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=360), blank=True, size=None)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(blank=True, max_length=50, null=True)),
                ('detail', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
