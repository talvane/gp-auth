# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-12 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('login', models.CharField(max_length=50, unique=True, verbose_name='Login')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='E-mail')),
                ('is_active', models.BooleanField(default=True, help_text='Only active users can access the system.', verbose_name='Is active?')),
                ('is_staff', models.BooleanField(default=False, help_text='Determines whether the user can access the administrator environment.', verbose_name='Member of the team?')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Registration date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'verbose_name': 'User',
            },
        ),
    ]