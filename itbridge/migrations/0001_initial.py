# Generated by Django 4.0.6 on 2022-07-18 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('image', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('programming_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_programming_language', to='itbridge.programminglanguage')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_teacher', to='itbridge.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('programming_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_programming_language', to='itbridge.programminglanguage')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_student', to='itbridge.user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]