# Generated by Django 4.2.7 on 2024-01-29 10:05

from django.conf import settings
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
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('call', models.CharField(max_length=10)),
                ('info', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('grade', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='hospital.hospital')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_review', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='hospital',
            index=models.Index(fields=['name'], name='hospital_ho_name_d8f339_idx'),
        ),
        migrations.AddIndex(
            model_name='hospital',
            index=models.Index(fields=['call'], name='hospital_ho_call_261aeb_idx'),
        ),
        migrations.AddIndex(
            model_name='hospital',
            index=models.Index(fields=['-created_at'], name='hospital_ho_created_0c99a1_idx'),
        ),
        migrations.AddIndex(
            model_name='hospital',
            index=models.Index(fields=['-updated_at'], name='hospital_ho_updated_4ea892_idx'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['user'], name='hospital_re_user_id_8de081_idx'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['hospital'], name='hospital_re_hospita_c045ed_idx'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['grade'], name='hospital_re_grade_7b927b_idx'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['-created_at'], name='hospital_re_created_d0a035_idx'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['-updated_at'], name='hospital_re_updated_9de0e3_idx'),
        ),
    ]