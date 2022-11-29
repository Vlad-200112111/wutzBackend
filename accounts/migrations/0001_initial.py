# Generated by Django 4.1.3 on 2022-11-29 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('patronymic', models.CharField(max_length=255, null=True)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Cadet'), (3, 'Teacher')], null=True)),
                ('url_image', models.ImageField(null=True, upload_to='profile/%Y-%m-%d/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategoriesForPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ElementsSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=500)),
                ('url_image', models.ImageField(upload_to='elements_slider/%Y-%m-%')),
            ],
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='WorkPrograms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=500)),
                ('url_image', models.FileField(upload_to='work_programs/%Y-%')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=500)),
                ('html', models.TextField(blank=True, max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.categoriesforpages')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=500)),
                ('url_image', models.ImageField(upload_to='news/%Y-%m-%d/')),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('html', models.TextField(blank=True, max_length=1000)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MainInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('html', models.TextField(blank=True, max_length=1000)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profiles',
            name='phone',
            field=models.ManyToManyField(to='accounts.phones'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.positions'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
