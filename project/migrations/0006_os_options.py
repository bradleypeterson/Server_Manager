from django.db import migrations


def add_default_operating_systems(apps, schema_editor):
    OperatingSystem = apps.get_model('project', 'OperatingSystem')

    # Add default operating systems
    OperatingSystem.objects.get_or_create(name='Windows')
    OperatingSystem.objects.get_or_create(name='Linux')
    OperatingSystem.objects.get_or_create(name='Other')


class Migration(migrations.Migration):
    dependencies = [
        ('project', '0005_operatingsystem_alter_server_operating_system'),
    ]

    operations = [
        migrations.RunPython(add_default_operating_systems),
    ]