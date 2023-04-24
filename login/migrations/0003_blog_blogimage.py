# Generated by Django 4.1.3 on 2023-04-24 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_rename_type_people_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('mental health', 'Mental Health'), ('heart disease', 'Heart Disease'), ('covid19', 'COVID-19'), ('immunization', 'Immunization')], max_length=100)),
                ('summary', models.CharField(max_length=30)),
                ('content', models.TextField(default='Some Content')),
                ('draft', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images', verbose_name='Blog Image')),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.blog')),
            ],
        ),
    ]