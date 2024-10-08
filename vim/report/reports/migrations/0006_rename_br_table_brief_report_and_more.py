# Generated by Django 5.1.1 on 2024-09-27 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_rename_toa_table_title_of_activity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='br',
            new_name='brief_report',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='colu',
            new_name='collaborating_units',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='dept',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='fco',
            new_name='faculty_coordinator',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='fund',
            new_name='funded_by',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='nat',
            new_name='nature',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='nop',
            new_name='no_of_participants',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='rp',
            new_name='resource_person',
        ),
        migrations.RenameField(
            model_name='table',
            old_name='sco',
            new_name='student_coordinator',
        ),
    ]
